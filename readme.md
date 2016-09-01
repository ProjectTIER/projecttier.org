Project Tier
==================

## Background

Torchbox inherited this site from PromptWorks in April 2016. Torchbox now has responsibility for the repo and project.

The build is a standard Wagtail build and follows most of the principles that a normal Torchbox-started Wagtail project would have.

We are, however, hosting the site with Heroku, which introduces some differences are pulling data and deployment.

## Local development

### Setup
Ensure that [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/) are installed. Then run:

```bash
git clone git@github.com:torchbox/project-tier.git
vagrant up
vagrant ssh
```

On `vagrant up` all of your dependencies should have been installed. To be doubly sure within your VM

```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```

Note: You can use the alias `dj` e.g. `dj migrate`

### Run the server
(Inside of the Vagrant VM)
```bash
djrun
```

## Heroku
For many things relating to the site - deployments, pulling data etc. - you need to be logged in to Heroku. There is a guide here on how to use Heroku CLI https://devcenter.heroku.com/articles/heroku-command-line

You may also find the blog post Chris Rodgers wrote useful https://wagtail.io/blog/deploying-wagtail-heroku/

 - Create a Heroku account
 - Get added to the Project Tier project (ask Tom Dyson or Karl for rights)
 - Install Heroku toolbelt
 - Type `heroku` in the command line
 - Login with your login details


## Pull production database locally
(Inside of the Vagrant VM)

You have to run `heroku` one time to log into Heroku. Then you can pull the database from Heroku.

```bash
`fab pull_production_data`
(wait... eventually the progress will freeze)
`↲` (e.g. hit the 'enter' key)
(wait... the progress will freeze again. You should see the word 'password' about 15 - 20 lines up in the tracestack)
`vagrant`
```

Fair warning: There is almost certainly a better way of doing this, but for the purpose of development this worked

Heroku is also sometimes slightly inconsistent. At times you need to enter the password ('vagrant') in the first instance, and then just hit enter on the second instance.

## Deploying
### Deploying to production
#### First deployment
```bash
git remote add https://git.heroku.com/project-tier-production.git

# check the remote has been correctly added
git remote -v

# deploy
git push heroku-production
```

#### Subsequent deployments
```bash
git push heroku-production
```

### Deploying to staging
#### First deployment
```bash
git remote add https://git.heroku.com/project-tier-dev.git

# check the remote has been correctly added
git remote -v

# deploy
git push heroku-dev
```

#### Subsequent deployments
```
git push heroku-dev
```

Note: We could (and should), if the users of the Project TIER Heroku project, were given admin rights to the Github repo automate deployments. This is probably useful thing to do in the long run.
