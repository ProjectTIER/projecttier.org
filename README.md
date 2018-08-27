![Project TIER](project_tier/static/img/logo.svg)

[![Build Status](https://travis-ci.org/ProjectTIER/projecttier.org.svg?branch=master)](https://travis-ci.org/ProjectTIER/projecttier.org)
[![Coverage Status](https://coveralls.io/repos/github/ProjectTIER/projecttier.org/badge.svg?branch=master)](https://coveralls.io/github/ProjectTIER/projecttier.org?branch=master)
[![Known Vulnerabilities](https://snyk.io/test/github/projecttier/projecttier.org/badge.svg?targetFile=requirements.txt)](https://snyk.io/test/github/projecttier/projecttier.org?targetFile=requirements.txt)
[![Requirements Status](https://requires.io/github/ProjectTIER/projecttier.org/requirements.svg?branch=master)](https://requires.io/github/ProjectTIER/projecttier.org/requirements/?branch=master)
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)

**Project TIER** (Teaching Integrity in Empirical Research) promotes the integration of principles and practices related to transparency and replicability in the research training of social scientists.

This repository is Project TIER's website (https://www.projecttier.org/), which is developed in Python using the Django-based [Wagtail](https://wagtail.io/) framework.

## Local development

1. Install [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/), if you haven't already.
2. Clone the project: `git clone https://github.com/ProjectTIER/projecttier.org.git`
3. Enter the project directory: `cd projecttier.org`
4. Start the Vagrant VM: `vagrant up`
5. Shell into the VM: `vagrant ssh`
6. Run the development server: `djrun`
7. Visit `0.0.0.0:8000` in your browser.

### Pull production data/media

Your local version of the project will have an empty database and no media uploads.
You can copy the production database and files to your local version.

* To pull the database: `fab pull_production_data`
* To pull file uploads: `fab pull_production_media`

See `fabfile.py` for more information.
You'll need authentication to run these commands.

## License and credits

Copyright © 2018 Richard Ball.

Licensed under the GNU AGPL 3.0. See the [`LICENSE`](LICENSE) file for the full license.

This project was originally developed by [PromptWorks](https://www.promptworks.com/).
In April 2016 the project was inherited by [Torchbox](https://torchbox.com/) who continued its development.
In January 2018 the project was transferred to [Candlewaster](https://candlewaster.co/) who continues to develop the project.
