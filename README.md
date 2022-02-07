# F1 project
## Installation locally: 
### 1 add .env file to root folder
### 2. run PostgreSQL database inside docker container

```bash
docker-compose up
docker ps

docker exec -it <CONTAINER ID> bash
``` 

### For NEW POSTGRE DB:
```bash
create database carsDB;
psql -h <host> -p 5432 -d <carsdb> -U postgres -W
```

### 3. Create venv
* Python (3.9)
```bash
python -m venv venv
```
### 4. Install requirements
```bash
pip install -r requirements.txt
```
### 5. Check that django has connected to sql-server 
```bash
python manage.py dbshell
```

### 6. Apply migrations to db
```bash
python manage.py makemigrations
python manage.py migrate
```

### 7. Create superuser to populate admin page
```bash
python manage.py createsuperuser
```

### 8. Start server
```bash
python manage.py runserver
```
### 9. Run pytest
```bash
pytest tests/
```

### 10. Run flake8
```bash
flake8
```
