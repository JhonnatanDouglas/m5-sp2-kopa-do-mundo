# Projeto Copa do Mundo API

Este projeto consiste em uma API para gerenciar informações sobre seleções de futebol que participaram da Copa do Mundo. A API foi desenvolvida em Django e utiliza o Django Rest Framework para criar endpoints que permitem a criação, leitura, atualização e exclusão de seleções.

## Tecnologias Utilizadas

[![Python](https://img.shields.io/badge/Python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/)
[![Django](https://img.shields.io/badge/Django-3.2.6-green)](https://www.djangoproject.com/)
[![Django Rest Framework](https://img.shields.io/badge/Django%20Rest%20Framework-3.12.4-blue)](https://www.django-rest-framework.org/)

## Funcionalidades

### Model Team

A model `Team` representa as seleções de futebol e possui os seguintes atributos:

- `name`: Nome da seleção (obrigatório, até 30 caracteres).
- `titles`: Número de títulos conquistados (opcional, padrão 0).
- `top_scorer`: Nome do artilheiro principal da seleção (obrigatório, até 50 caracteres).
- `fifa_code`: Código FIFA da seleção (obrigatório, único, até 3 caracteres).
- `first_cup`: Data da primeira Copa do Mundo em que a seleção participou (opcional).

A classe `Team` também possui um método `__repr__` personalizado para representar objetos seguindo o seguinte padrão: `"<[1] Brasil - BRA>"`, onde:

- `[1]`: O ID do objeto salvo.
- `Brasil`: O nome da seleção.
- `BRA`: O código FIFA da seleção.

### Rotas

A API possui as seguintes rotas:

#### Listagem de Seleções

- **Endpoint**: `/api/teams/`
- **Método HTTP**: GET
- **Objetivo**: Listar todas as seleções cadastradas no sistema.
- **Retorno**: Lista de seleções com status code 200.

#### Criação de Seleção

- **Endpoint**: `/api/teams/`
- **Método HTTP**: POST
- **Objetivo**: Cadastrar uma nova seleção no sistema.
- **Corpo da Requisição (JSON)**:

```json
{
  "name": "Brasil",
  "titles": 5,
  "top_scorer": "Pelé",
  "fifa_code": "BRA",
  "first_cup": "1930-07-13"
}
```

- **Retorno (JSON)** com status code 201 Created:

```json
{
  "id": 1,
  "name": "Brasil",
  "titles": 5,
  "top_scorer": "Pelé",
  "fifa_code": "BRA",
  "first_cup": "1930-07-13"
}
```

#### Filtragem de Seleção

- **Endpoint**: `/api/teams/<team_id>/`
- **Método HTTP**: GET
- **Objetivo**: Filtrar uma seleção por ID.
- **Retorno (JSON)** com status code 200:

```json
{
  "id": 1,
  "name": "Brasil",
  "titles": 5,
  "top_scorer": "Pelé",
  "fifa_code": "BRA",
  "first_cup": "1930-07-13"
}
```

- **Retorno (JSON)** com status code 404 Not Found, se o ID não existir:

```json
{
  "message": "Team not found"
}
```

#### Atualização de Seleção

- **Endpoint**: `/api/teams/<team_id>/`
- **Método HTTP**: PATCH
- **Objetivo**: Atualizar uma seleção por ID.
- **Corpo da Requisição (JSON)**:

```json
{
  "name": "Brasil 2099",
  "top_scorer": "Alejo"
}
```

- **Retorno (JSON)** com status code 200 OK:

```json
{
  "id": 1,
  "name": "Brasil 2099",
  "titles": 5,
  "top_scorer": "Alejo",
  "fifa_code": "BRA",
  "first_cup": "1930-07-13"
}
```

#### Deleção de Seleção

- **Endpoint**: `/api/teams/<team_id>/`
- **Método HTTP**: DELETE
- **Objetivo**: Deletar uma seleção por ID.
- **Retorno (sem corpo)** com status code 204 No Content.

- **Retorno (JSON)** com status code 404 Not Found, se o ID não existir:

```json
{
  "message": "Team not found"
}
```

## Instalação e Uso

Para executar este projeto em sua máquina local, siga estas etapas:

1. Clone o repositório:

```bash
git clone https://github.com/seu-usuario/seu-repositorio.git
cd seu-repositorio
```

2. Crie um ambiente virtual e ative-o (certifique-se de ter o Python instalado):

```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:

```bash
pip install -r requirements.txt
```

4. Execute as migrações do banco de dados:

```bash
python manage.py migrate
```

5. Execute o servidor de desenvolvimento:

```bash
python manage.py runserver
```

A API estará disponível em `http://localhost:8000/api/teams/`.

## Contribuição

Sinta-se à vontade para contribuir para este projeto abrindo problemas (issues) ou enviando pull requests com melhorias.