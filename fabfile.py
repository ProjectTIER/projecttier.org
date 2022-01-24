from fabric.api import *


def deploy_staging():
    local('heroku git:remote --remote staging -a projecttier-staging')
    local('git push staging master')


def deploy_production():
    local('heroku git:remote --remote production -a projecttier-production')
    local('git push production master')


def pull_staging_data():
    local('psql -d project_tier -c "ALTER USER vagrant with password \'vagrant\';"')
    local('dropdb --if-exists project_tier')
    local('heroku pg:pull DATABASE_URL project_tier --app projecttier-staging')
    local('psql -d project_tier -c "alter role vagrant password null;"')


def pull_production_data():
    # It will prompt you to log in to Heroku. Your Heroku user needs adequate
    # permission on the projecttier-production app.
    local('psql -d project_tier -c "ALTER USER vagrant with password \'vagrant\';"')
    local('dropdb --if-exists project_tier')
    local('heroku pg:pull DATABASE_URL project_tier --app projecttier-production')
    local('psql -d project_tier -c "alter role vagrant password null;"')

def pull_production_media():
    # To use this command, you must put a .s3cfg file into the root of the
    # project directory. Get it from another developer or use
    # `s3cmd --configure` to create it yourself.
    local('mkdir -p media')
    local('s3cmd --config=.s3cfg get s3://bucketeer-82911c16-8ccd-4854-b255-5b3ebba24d7c --recursive --skip-existing --delete-removed media')

def sync_staging():
    # Syncs the staging database with production
    local('heroku pg:copy projecttier-production::DATABASE_URL DATABASE_URL -a projecttier-staging --confirm projecttier-staging')
