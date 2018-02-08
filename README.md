![Project TIER](project_tier/static/img/logo.svg)

[![Build Status](https://travis-ci.org/project-tier/project-tier.svg?branch=master)](https://travis-ci.org/project-tier/project-tier)
[![Coverage Status](https://coveralls.io/repos/github/project-tier/project-tier/badge.svg?branch=master)](https://coveralls.io/github/project-tier/project-tier?branch=master)
[![Known Vulnerabilities](https://snyk.io/test/github/project-tier/project-tier/badge.svg)](https://snyk.io/test/github/project-tier/project-tier)
[![Requirements Status](https://requires.io/github/project-tier/project-tier/requirements.svg?branch=master)](https://requires.io/github/project-tier/project-tier/requirements/?branch=master)
[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)

**Project TIER** (Teaching Integrity in Empirical Research) promotes the integration of principles and practices related to transparency and replicability in the research training of social scientists.

This repository is Project TIER's website (https://www.projecttier.org/), which is developed in Python using the Django-based [Wagtail](https://wagtail.io/) framework.

## Local development

1. Install [Docker](https://asciinema.org/a/158200) and [docker-compose](https://docs.docker.com/compose/install/), if you haven't already.
2. Clone the project: `git clone https://github.com/project-tier/project-tier.git`
3. Enter the project directory: `cd project-tier`
4. Run migrations: `docker-compose run web python manage.py migrate`
5. Run the development server: `docker-compose up`
6. Visit `localhost:8000` in your browser. **IMPORTANT:** `0.0.0.0:8000` will not work.

## License and credits

Copyright © 2018 Richard Ball.

Licensed under the GNU AGPL 3.0. See the [`LICENSE`](LICENSE) file for the full license.

This project was originally developed by [PromptWorks](https://www.promptworks.com/). In April 2016 the project was inherited by [Torchbox](https://torchbox.com/) who continued its development. In January 2018 the project was transferred to [Candlewaster](https://candlewaster.co/) who continues to develop the project.
