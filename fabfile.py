from fabric.api import *


def deploy_staging():
    local('heroku git:remote -a project-tier-dev')
    local('git push heroku master')


def deploy_production():
    local('heroku git:remote -a project-tier-production')
    local('git push heroku master')


def pull_production_data():
    local('psql -d project_tier -c "ALTER USER vagrant with password \'vagrant\';"')
    local('dropdb project_tier')
    local('heroku pg:pull DATABASE_URL project_tier --app project-tier-production')
    local('psql -d project_tier -c "alter role vagrant password null;"')
