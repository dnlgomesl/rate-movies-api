# Rate Movies API
## Como executar a API?

1. Faça o clone deste repositório para o seu ambiente local.

```bash
git https://github.com/dnlgomesl/rate-movies-api.git
```

2. Navegue até o diretório do projeto.

```bash
cd rate-movies-api
```
3. Instale o Docker e o docker-compose.

Siga o tutorial do próprio Docker que está nesse [link](https://docs.docker.com/get-docker/).

4. Após instalar o Docker faça o build.

```bash
docker-compose up --build
```

## Endpoints da API

### Status
Endpoint: GET /status/

Esse endpoint retorna o status da api.

Exemplo de resposta:

```json
{
  "status": "online",
  "timestamp": 1690268056,
  "started": 1690268052,
  "service": "api",
  "version": "1.0"
}
```
### Create
Endpoint: POST /movie/

Esse endpoint cria um filme.

Exemplo de body:
```json
{
	"name": "inception",
	"director": "nolan",
	"genre": "action",
	"year":  2010
}
```
Todos os itens são obrigatórios, é retornado erro se faltar algum.

Exemplo de resposta de sucesso:
```json
{
    "_id": "4a6b505a15ce4d9e34e5fdd4655e86472ce11895",
    "name": "inception",
    "director": "nolan",
    "genre": "action",
    "year": 2010,
    "rating": 0,
    "count": 0
}
```

### Read All
Endpoint: GET /movies/

Retorna todos os filmes cadastrados.

Exemplo de resposta de sucesso:
```json
[
	{
		"_id": "df48181c4ef7be134c81316f83a81f930cd714b6",
		"name": "memento",
		"director": "nolan",
		"genre": "action",
		"year": 2000,
		"rating": 0,
		"count": 0
	},
	{
		"_id": "4a6b505a15ce4d9e34e5fdd4655e86472ce11895",
		"name": "inception",
		"director": "nolan",
		"genre": "action",
		"year": 2010,
		"rating": 0,
		"count": 0
	}
]
```

### Read One
Endpoint: GET /movie/<movie_id>

Caso o id exista, retorna o filme.

Exemplo de resposta de sucesso:
```json
{
    "_id": "4a6b505a15ce4d9e34e5fdd4655e86472ce11895",
    "name": "inception",
    "director": "nolan",
    "genre": "action",
    "year": 2010,
    "rating": 0,
    "count": 0
}
```

### Update
Endpoint: PUT /movie/<movie_id>

Caso o id exista, atualiza o filme.

Exemplo de body:
```json
{
    "name": "inception_edited",
    "director": "nolan_edited",
    "genre": "action_edited",
    "year": 2011
}
```
É necessário ter algum dos atributos (name, director, genre, year) no body, se não não é atualizado.

Exemplo de resposta de sucesso:
```json
{
	"_id": "4a6b505a15ce4d9e34e5fdd4655e86472ce11895",
	"name": "inception_edited",
	"director": "nolan_edited",
	"genre": "action_edited",
	"year": 2011,
    "rating": 0,
    "count": 0
}
```

### Delete
Endpoint: DELETE /movie/<movie_id>

Caso o id exista, deleta o filme.

### Rating
Endpoint: POST /movie/<movie_id>

Caso o id exista, avalia o filme.

Exemplo de body:
```json
{
	"rate": 9.3
}
```
É necessário ter que `rate` seja enviado no body.

Exemplo de resposta de sucesso:
```json
{
	"_id": "4a6b505a15ce4d9e34e5fdd4655e86472ce11895",
	"name": "inception_edited",
	"director": "nolan_edited",
	"genre": "action_edited",
	"year": 2011,
	"rating": 9.3,
	"count": 1
}
```
### Not Rating
Endpoint: GET /movie/rating/none

Retorna um filme sem avaliação caso exista. Caso exista mais de um, é retornado aleatoriamente uma das opções.

Exemplo de resposta de sucesso:
```json
{
	"_id": "df48181c4ef7be134c81316f83a81f930cd714b6",
	"name": "memento",
	"director": "nolan",
	"genre": "action",
	"year": 2000,
	"rating": 0,
	"count": 0
}
```