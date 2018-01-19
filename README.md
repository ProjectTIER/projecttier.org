Project TIER
============

**Project TIER (Teaching Integrity in Empirical Research) promotes the integration of principles and practices related to transparency and replicability in the research training of social scientists.**

This repository is Project TIER's website (https://www.projecttier.org/), which is developed in Python using the Django-based [Wagtail](https://wagtail.io/) framework.

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

# wait... eventually the progress will freeze
`↲` (e.g. hit the 'enter' key)

# wait... the progress will freeze again. You should see the word 'password' about 15 - 20 lines up in the tracestack
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

## License and credits

Copyright © 2018 Richard Ball, Some rights reserved.

This project was originally developed by [PromptWorks](https://www.promptworks.com/). In April 2016 the project was inherited by [Torchbox](https://torchbox.com/) who continued its development. In January 2018 the project was transferred to [Candlewaster](https://candlewaster.co/) who continues to develop the project.
