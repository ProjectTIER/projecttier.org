Project Tier
==================

## Local development

### Setup
Ensure that [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/) are installed. Then run:

```
git clone git@github.com:torchbox/project-tier.git
vagrant up
vagrant ssh
```

### Run the server
(Inside of the Vagrant VM)
```
djrun
```

## Pull production database locally
(Inside of the Vagrant VM)

You have to run `heroku` one time to log into Heroku. Then you can pull the database from Heroku.

```
fab pull_production_data
```

When you run this, the progress will eventually freeze, and you should see the word `Password: ` about 15-20 lines up. This part is sorta weird. You have to type `vagrant` (typing will be invisible) and hit enter. At the very end this will happen a second time; you will see `Password: ` and must type `vagrant` and hit enter.

## Bringing in others changes

Make sure, every time you bring in new code from others to run:

```bash
pip install -r requirements.txt
dj migrate
```
