from fabric.api import *


def deploy_staging():
    local('heroku git:remote --remote staging -a projecttier-staging')
    local('git push staging master')


def deploy_production():
    local('heroku git:remote --remote production -a projecttier-production')
    local('git push production master')


def pull_staging_data():
    local('psql -d project_tier -c "ALTER USER vagrant with password \'vagrant\';"')
    local('dropdb project_tier')
    local('heroku pg:pull DATABASE_URL project_tier --app projecttier-staging')
    local('psql -d project_tier -c "alter role vagrant password null;"')


def pull_production_data():
    local('psql -d project_tier -c "ALTER USER vagrant with password \'vagrant\';"')
    local('dropdb project_tier')
    local('heroku pg:pull DATABASE_URL project_tier --app projecttier-production')
    local('psql -d project_tier -c "alter role vagrant password null;"')
