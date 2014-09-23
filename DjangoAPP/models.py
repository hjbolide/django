from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import ugettext_lazy as e_
from topnotchdev import files_widget

from .util import get_week


class SiteType(models.Model):

    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=200, default='')

    def __unicode__(self):
        return self.name


class Site(models.Model):

    url = models.URLField(max_length=200)
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(blank=True, default=timezone.now())
    modified_at = models.DateTimeField(blank=True, default=timezone.now())
    type = models.ForeignKey(SiteType, null=True, blank=True)
    user = models.ForeignKey(User, blank=True)

    def __unicode__(self):
        return self.name


class Contact(models.Model):

    phone = models.CharField(max_length=10, blank=True)
    mobile = models.CharField(max_length=10, blank=True)
    email = models.EmailField(max_length=75, blank=True)
    address = models.CharField(max_length=125)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    zoom = models.IntegerField(blank=True, null=True)
    heading = models.FloatField(blank=True, null=True)
    pitch = models.FloatField(blank=True, null=True)
    site = models.ForeignKey(Site)


class EntityType(models.Model):

    name = models.CharField(max_length=50)
    desc = models.CharField(max_length=200, default='')
    is_person = models.BooleanField(default=False)

    def __unicode__(self):
        return self.name


class Entity(models.Model):

    class Meta:
        verbose_name_plural = e_('Entities')

    GENDER_CHOICES = (
        ('m', e_('Male')),
        ('f', e_('Female')),
    )

    PERSON_FIELDS = ['dob', 'gender']

    type = models.ForeignKey(EntityType, null=True, blank=True)
    name = models.CharField(max_length=50)
    dob = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    price = models.FloatField(blank=True, null=True)
    data = models.BinaryField(blank=True, null=True)
    # Categories has to be a compulsory field
    # because entity does not have a site field.
    # Entity visibility will be determined by its categories.
    categories = models.ManyToManyField('Category')
    images = files_widget.ImagesField(blank=True, null=True)

    def display_categories(self):
        tag = '<strong>%s</strong>'
        return ', '.join(map(lambda x: tag % x.name, self.categories.all()))

    display_categories.allow_tags = True

    def __unicode__(self):
        return self.name

    @property
    def person_field_selectors(self):
        return 'div.%s' % ', div.'.join(self.PERSON_FIELDS)


class Category(models.Model):

    class Meta:
        verbose_name_plural = e_('Categories')

    name = models.CharField(max_length=16)
    desc = models.CharField(max_length=200, blank=True)
    site = models.ForeignKey(Site)

    def __unicode__(self):
        return self.name


class Page(models.Model):
    html_id = models.CharField(max_length=16, blank=True)
    name = models.CharField(max_length=16)
    display_name = models.CharField(max_length=40)
    desc = models.TextField(blank=True)
    data = models.BinaryField(blank=True, null=True)
    site = models.ForeignKey(Site)


class RosterRule(models.Model):

    week_mask = models.IntegerField(default=0)
    date = models.DateField(blank=True, null=True)
    entity = models.ForeignKey(Entity, blank=True, null=True)
    site = models.ForeignKey(Site)

    def display_week(self):
        return ', '.join(get_week(self.week_mask, translate=True))
