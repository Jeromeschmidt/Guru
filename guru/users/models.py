from django.contrib.auth.models import AbstractUser
from django.db.models import CharField
# , IntegerField, FloatField
# from django_mysql.models import ListTextField
# from django.contrib.postgres.fields import ArrayField
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = CharField(_("Name of User"), blank=True, max_length=255)
    # support_skills = ArrayField(base_field=CharField(),size=20)
    # support_classes_taken = ArrayField(base_field=CharField(),size=20)
    # email_address = contact_info = CharField(max_length=100, default="")
    # is_teachingassistant = (('F', 'False'), ('T', 'True'))
    # rating = IntegerField()
    # avg_reponse = FloatField()
    # is_online = (('F', 'False'), ('T', 'True'))
    # messages_received = IntegerField()
    # Bio = CharField(max_length=500)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
