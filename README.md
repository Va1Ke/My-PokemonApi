# myPokemonApi
Api based on parsed information about pokemons from pokemon-api,<br>
users can add/remove new pokemon to their collection, get information about each pokemon,<br>
check collection of other users and others operations!

* Install requirements:
```
pip install -r requirements.txt
```

* Update requirements:
```
pip freeze > requirements.txt
```
* Run local:
```
uvicorn app.main:app
```
* Run docker-compose:
```
docker-compose up --build
```
* Make migrations:
```
docker exec -it <container_id> bash
alembic revision --autogenerate -m "<migration_name>"
alembic upgrade head
```
### Set environment variables:
**list of environment variables which should be set:**<br>
```
POSTGRES_USER
POSTGRES_PASSWORD
POSTGRES_HOST
POSTGRES_PORT
POSTGRES_DB
APP_HOST
APP_PORT
MY_ALGORITHMS
SECRET
```
if running with docker: 
POSTGRES_HOST should be set as name of container with db<br>
if running local: 
POSTGRES_HOST should be set as localhost

**Windows:**
```
//CMD:
set SOME_VARIABLE=some_value

//Powershell:
$Env:Foo = 'An example'
```
**Linux:**
```
export SOME_VARIABLE=some_value
```

### Endpoints:
* List of all endpoints you can find in Swagger:
```
http://127.0.0.1:8000/docs#/
```

