from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
import uuid
from django.db import models
from django.conf import settings
from seats.models import Branch


class BaseProfile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL,
                                primary_key=True)	
    slug = models.UUIDField(default=uuid.uuid4, blank=True, editable=False)
    # Add more user profile fields here. Make sure they are nullable
    # or with default values
    preferences = [(0,'None'),
				   (1,'Preference 1'),
				   (2,'Preference 2'),
				   (3,'Preference 3'),
				  ]
    picture = models.ImageField('Profile picture',
                                upload_to='profile_pics/%Y-%m-%d/',
                                null=True,
                                blank=True)
    rank = models.IntegerField(default=0)
    pref1 = models.ForeignKey(Branch, related_name='%(class)s_pref_1', default=1)
    pref2 = models.ForeignKey(Branch, related_name='%(class)s_pref_2', default=1)
    pref3 = models.ForeignKey(Branch, related_name='%(class)s_pref_3', default=1)
    allotted = models.ForeignKey(Branch, related_name='%(class)s_allotted', default=1)
    allotted_pref = models.IntegerField(choices=preferences, default=0)
    bio = models.CharField("Short Bio", max_length=200, blank=True, null=True)
    email_verified = models.BooleanField("Email verified", default=False)

    class Meta:
        abstract = True


@python_2_unicode_compatible
class Profile(BaseProfile):
    def __str__(self):
        return "{}'s profile". format(self.user)
