from django.contrib.auth.models import AbstractUser
from django.db.models import (BooleanField, CASCADE, CharField, FloatField,
                              IntegerField, ManyToManyField, Model,
                              OneToOneField, PositiveSmallIntegerField)
from django.contrib.postgres.fields import ArrayField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)
    # is_customer = BooleanField(default=True) #
    # user = OneToOneField(User, on_delete=CASCADE, primary_key=True)
    skills = ArrayField(CharField(max_length=10, blank=True),
            size=8, null=True,
            )
    # ArrayField(_("A list of skills that user can help with"), null=True,
    #                     base_field=CharField(max_length=255))
    classes_taken = ArrayField(null=True,
                               base_field=CharField(max_length=255),
                               size=20)
    is_teachingassistant = BooleanField(default=False)
    rating = IntegerField(null=True, blank=True)
    avg_reponse = FloatField(null=True, blank=True)
    is_online = BooleanField(default=False)
    messages_received = IntegerField(null=True, blank=True)
    bio = CharField(blank=True, max_length=500)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
