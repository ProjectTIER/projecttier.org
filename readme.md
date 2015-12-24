project_tier
==================

## Setting up local development

### Setup your machine

```
brew install python3 postgresql
createdb project_tier
```

### Setup the project
```
git clone git@github.com:promptworks/project_tier.git
cd project-tier
pyvenv venv
source venv/bin/activate
pip install -r requirements.txt
./manage.py migrate
./manage.py createsuperuser
```

### Run the server
```
./manage.py runserver
```

## Setup prod db locally

Assuming the production heroku db is our source of truth, it's simple to download locally

```bash
./bin/download_prod_db # Downloads the latest database to latest.dump
./bin/import_prod_db # Overrides your local db with prods
```

## Bringing in others changes

Make sure, every time you bring in new code from others to run

```bash
pip install -r requirements.txt
./manage.py migrate
```
