FROM python:3.9
LABEL maintainer="info@projecttier.org"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt

COPY . /app
WORKDIR /app

# Install Heroku toolbelt
RUN wget -O- https://cli-assets.heroku.com/install-ubuntu.sh | sh

# Install PostgreSQL 14 client
RUN apt-get update &&\
    apt-get install -y lsb-release &&\
    sh -c 'echo "deb http://apt.postgresql.org/pub/repos/apt $(lsb_release -cs)-pgdg main" > /etc/apt/sources.list.d/pgdg.list' &&\
    wget --quiet -O - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add - &&\
    apt-get update &&\
    apt-get install -y postgresql-client-14 &&\
    apt-get clean all

EXPOSE 5000
CMD ["gunicorn", "project_tier.wsgi:application", "-b :5000"]
