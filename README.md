![Project TIER](project_tier/static/img/logo.svg)

[![Build Status](https://travis-ci.org/project-tier/project-tier.svg?branch=master)](https://travis-ci.org/project-tier/project-tier)
[![Coverage Status](https://coveralls.io/repos/github/project-tier/project-tier/badge.svg?branch=master)](https://coveralls.io/github/project-tier/project-tier?branch=master)

**Project TIER** (Teaching Integrity in Empirical Research) promotes the integration of principles and practices related to transparency and replicability in the research training of social scientists.

This repository is Project TIER's website (https://www.projecttier.org/), which is developed in Python using the Django-based [Wagtail](https://wagtail.io/) framework.

## Local development

Ensure that [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/) are installed. Then, follow the instructions below.

```bash
# Clone the repo locally
git clone https://github.com/project-tier/project-tier.git

# Enter the repo
cd project-tier

# Start the VM
vagrant up

# Shell into the VM
vagrant ssh
```

### Run the development server

Inside of the Vagrant VM, simply run:

```bash
# Start the local development server
djrun
```

**Note:** `djrun` is an alias for `python manage.py runserver 0.0.0.0:8000`. This IP address is needed so the development server can be accessed from the host machine.

You may also run `dj <command>` in place of `python manage.py <command>`.

For example, `dj makemigrations` or `dj migrate`. These aliases are installed into the VM when it's first provisioned by Vagrant. See [`provision.sh`](vagrant/provision.sh) for the full script.

## Deployment

The Project TIER website is hosted on [Heroku](https://www.heroku.com/), and this repo is configured to make deployments to Heroku. It also provides a wrapper script, [`fabfile.py`](fabfile.py), for common deployment commands using [Fabric](http://www.fabfile.org/).

The Vagrant VM provides the Heroku Toolkit preinstalled, so you can make deployments from inside of the VM.

### Heroku setup

Before doing anything, you'll need to login to Heroku and set it up. Follow the steps below.

- Create a Heroku account
- Create an app (or get added to the Project TIER project if you're working with us)
- Install Heroku toolbelt
- Type `heroku` in the command line
- Login with your login details

### Pull production database locally

After logging into Heroku, you can run the following within the VM to pull the production database into your local environment.

```bash
fab pull_production_data

# wait... eventually the progress will freeze
↲ # (e.g. hit the 'enter' key)

# wait... the progress will freeze again.
# You should see the word 'password' about
# 15–20 lines up in the tracestack
vagrant
```

### Pushing code

Within the VM, you may run these commands to push up your code:

```bash
# Push to production
fab deploy_production

# or, push to staging
fab deploy_staging
```

If these don't work, you may have an issue with your local Heroku configuration or you don't have access to the projects on Heroku.

## License and credits

Copyright © 2018 Richard Ball.

Licensed under the GNU AGPL 3.0. See the [`LICENSE`](LICENSE) file for the full license.

This project was originally developed by [PromptWorks](https://www.promptworks.com/). In April 2016 the project was inherited by [Torchbox](https://torchbox.com/) who continued its development. In January 2018 the project was transferred to [Candlewaster](https://candlewaster.co/) who continues to develop the project.
