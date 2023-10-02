from rest_framework.views import APIView, Request, Response, status
from django.forms.models import model_to_dict
from teams.models import Team
from utils import data_processing
from exceptions import NegativeTitlesError, InvalidYearCupError, ImpossibleTitlesError


class TeamView(APIView):
    def get(self, request: Request) -> Response:
        teams_to_dict = [model_to_dict(team) for team in Team.objects.all()]

        return Response(teams_to_dict, status.HTTP_200_OK)

    def post(self, request: Request) -> Response:
        try:
            team = Team.objects.create(**request.data)
            team_to_dict = model_to_dict(team)
            valid_team = data_processing(team_to_dict)
        except NegativeTitlesError:
            return Response(
                {"error": "titles cannot be negative"}, status.HTTP_400_BAD_REQUEST
            )
        except InvalidYearCupError:
            return Response(
                {"error": "there was no world cup this year"},
                status.HTTP_400_BAD_REQUEST,
            )
        except ImpossibleTitlesError:
            return Response(
                {"error": "impossible to have more titles than disputed cups"},
                status.HTTP_400_BAD_REQUEST,
            )

        return Response(valid_team, status.HTTP_201_CREATED)


class TeamDetailView(APIView):
    def get(self, request: Request, team_id: int) -> Response:
        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        team_to_dict = model_to_dict(team)

        return Response(team_to_dict, status.HTTP_200_OK)

    def patch(self, request: Request, team_id: int) -> Response:
        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        for keys, values in request.data.items():
            setattr(team, keys, values)

        team.save()
        team_to_dict = model_to_dict(team)

        return Response(team_to_dict, status=status.HTTP_200_OK)

    def delete(self, request: Request, team_id: int) -> Response:
        try:
            team = Team.objects.get(pk=team_id)
        except Team.DoesNotExist:
            return Response({"message": "Team not found"}, status.HTTP_404_NOT_FOUND)

        team.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
