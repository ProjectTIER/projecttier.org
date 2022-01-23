#!/bin/sh
set -xe

PROJECT_NAME=$1

PROJECT_DIR=/vagrant
VIRTUALENV_DIR=/home/vagrant/.virtualenvs/$PROJECT_NAME

PYTHON=$VIRTUALENV_DIR/bin/python
PIP=$VIRTUALENV_DIR/bin/pip


# Upgrade postgres to 13 to match Heroku
pg_dropcluster 9.6 main --stop
apt update && apt-get install -y postgresql-13 postgresql-client-13
sudo -Hu postgres psql -c "CREATE ROLE vagrant WITH LOGIN CREATEDB SUPERUSER"


# Create database
set +e
su - vagrant -c "createdb $PROJECT_NAME"
set -e



# Virtualenv setup for project
su - vagrant -c "virtualenv --python=python3 $VIRTUALENV_DIR"
# Replace previous line with this if you are using Python 2
# su - vagrant -c "virtualenv --python=python2 $VIRTUALENV_DIR"

su - vagrant -c "echo $PROJECT_DIR > $VIRTUALENV_DIR/.project"


# Install PIP requirements
su - vagrant -c "$PIP install -r $PROJECT_DIR/requirements.txt"


# Set execute permissions on manage.py as they get lost if we build from a zip file
chmod a+x $PROJECT_DIR/manage.py


# Run syncdb/migrate/update_index
su - vagrant -c "$PYTHON $PROJECT_DIR/manage.py migrate --noinput && \
                 $PYTHON $PROJECT_DIR/manage.py update_index"


# Install Heroku toolbelt
apt-get install -y openssl
su - vagrant -c  "curl https://cli-assets.heroku.com/install-ubuntu.sh | sh"


# Install s3cmd for copying media files from S3-compatible services
su - vagrant -c "$PIP install s3cmd"


# Add a couple of aliases to manage.py into .bashrc
cat << EOF >> /home/vagrant/.bashrc
export PYTHONPATH=$PROJECT_DIR
export DJANGO_SETTINGS_MODULE=$PROJECT_NAME.settings.dev

alias dj="django-admin.py"
alias djrun="dj runserver 0.0.0.0:8000"
alias djcelery="celery -A $PROJECT_NAME worker --loglevel=info -s /tmp/celerybeat-schedule \$1"

source $VIRTUALENV_DIR/bin/activate
export PS1="[$PROJECT_NAME \W]\\$ "
cd $PROJECT_DIR
EOF
