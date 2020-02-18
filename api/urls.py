from django.urls import path

from api.views import UserList
#
# urlpatterns = [
#     path('guru/users/', UserList.as_view(), name='user_list'),
#     path('guru/users/<str:username>/', UserDetail.as_view(), name='user_detail')
# ]


urlpatterns = [
    path('guru/', UserList.as_view(), name='guru_list'),
]
