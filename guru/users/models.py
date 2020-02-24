from django.contrib.auth.models import AbstractUser
from django.db.models import (BooleanField, CASCADE, CharField, FloatField,
                              IntegerField, ManyToManyField, Model, OneToOneField,
                              PositiveSmallIntegerField)
from django.contrib.postgres.fields import ArrayField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)
    USER_TYPE_CHOICES = (
        (1, 'customer'),
        (2, 'staff'),
        (3, 'admin'),
    )
    user_type = PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})


class Customer(Model):
    user = OneToOneField(User, on_delete=CASCADE, primary_key=True)
    # skills = ArrayField(_("A list of skills that user can help with"), null=True,
    #                     base_field=CharField(max_length=255),
    #                     size=20)
    # classes_taken = ArrayField(null=True,
    #                            base_field=CharField(max_length=255),
    #                            size=20)
    # is_teachingassistant = BooleanField()
    # rating = IntegerField(null=True, blank=True)
    # avg_reponse = FloatField(null=True, blank=True)
    # is_online = BooleanField()
    # messages_received = IntegerField(null=True, blank=True)
    bio = CharField(blank=True, max_length=500)
