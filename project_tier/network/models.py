from django.db import models
import datetime


class Person(models.Model):
    """
    A member of the Tier Network, including Fellows and other connections.
    """
    name = models.CharField(max_length=255)
    slug = models.SlugField()
    main_job_title = models.CharField(max_length=255, blank=True)
    academic_title = models.CharField(max_length=255, blank=True)
    affiliation = models.CharField(max_length=255, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    phone = models.CharField(max_length=255, blank=True)
    website = models.URLField(max_length=255, blank=True)
    twitter = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='uploads/', blank=True)
    image_credit = models.CharField(max_length=255, blank=True, help_text="Add credit for photo if necessary. Note: add only their name 'Photo courtesy of' is hardcoded")

    show_in_network = models.BooleanField(default=True, blank=False)
    show_in_people = models.BooleanField(default=False, blank=False)

    CATEGORIES = (
        ('fellows', 'Fellows'),
        ('advisory_board', 'Advisory Board'),
        ('project_directors', 'Project Directors'),
        ('network_other', 'Network Other')
    )
    category = models.CharField(
        max_length=255,
        choices=CATEGORIES,
        default='network_other',
        blank=False,
    )

    YEAR_CHOICES = []
    for r in range(2010, (datetime.datetime.now().year+1)):
        YEAR_CHOICES.append(
            (r, "{}–{}".format(r, r + 1))
        )

    fellowship_year = models.CharField(
        max_length=4,
        choices=YEAR_CHOICES,
        default='',
        blank=True,
    )
