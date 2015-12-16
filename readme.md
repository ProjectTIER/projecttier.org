project-tier
==================

## Setting up local development

### Setup your machine

```
brew install python3 postgresql
createdb project-tier
```

### Setup the project
```
git clone git@github.com:promptworks/project-tier.git
pyvenv project-tier
source project-tier/bin/activate
cd project-tier
pip install -r requirements.txt
./manage.py migrate
./manage.py createsuperuser
```

### Run the server
```
./manage.py runserver
```
