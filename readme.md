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
cd project_tier
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
