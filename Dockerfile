FROM python:3.6
LABEL maintainer="info@projecttier.org"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
RUN pip install gunicorn

COPY . /app
WORKDIR /app

# Install Heroku toolbelt
RUN wget -O- https://cli-assets.heroku.com/install-ubuntu.sh | sh

EXPOSE 5000
CMD ["gunicorn", "project_tier.wsgi:application", "-b :5000", "--workers 3"]
