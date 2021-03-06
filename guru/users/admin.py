from django.contrib import admin
from guru.users.models import User


class UserAdmin(admin.ModelAdmin):
    """ Show helpful fields on the changelist page. """
    list_display = ('name', 'skills', 'classes_taken', 'is_teachingassistant', 'rating', 'avg_reponse', 'is_online', 'messages_received', 'bio')

admin.site.register(User, UserAdmin)


                
# from django.contrib import admin
# from django.contrib.auth import admin as auth_admin
# from django.contrib.auth import get_user_model
#
# from guru.users.forms import UserChangeForm, UserCreationForm
#
# User = get_user_model()
#
#
# @admin.register(User)
# class UserAdmin(auth_admin.UserAdmin):
#
#     form = UserChangeForm
#     add_form = UserCreationForm
#     fieldsets = (("User", {
#         "fields": ("name",)
#     }),) + auth_admin.UserAdmin.fieldsets
#     list_display = ["username", "name", "is_superuser"]
#     search_fields = ["name"]
