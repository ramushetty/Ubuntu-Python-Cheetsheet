# generating  random hex string
import secrets
print(secrets.token_hex(12)) # 001cb8ef4da7b9ae57d27d38

# context shell processor
# export FLASK_APP=main.py
# flask shell
# create tables in db = db.create_all()


#flask migrate
# https://flask-migrate.readthedocs.io/en/latest/
# pipenv install flask_migrate
# flask db init
# flask db migrate -m "Initial migration."
# flask db upgrade


