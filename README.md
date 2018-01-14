# flaskwithuser

Flask App with some basic user management (Login, Signup) on Python3
### Setup

#### Clone repository

```bash
$ git clone https://github.com/mblanchard23/flaskwithuser && cd flaskwithuser
```

#### Install packages

```bash
$ pip3 install -r requirements.txt
```

#### Configure Database
```bash
$ export FLASKSQLALCHEMYURI="SQLAlchemy://dburi" # Defaults to local SQLite
```

#### Set up Database
```python
>>> import main
>>> main.db.create_all() 
```
#### Run application
```bash
$ python3 main.py
```
