from django.urls import path
from .views import home, path_api, student_api,student_api_get_update_delete

urlpatterns = [
    path('', home),
    path('student/', student_api),
    path('student/<int:pk>', student_api_get_update_delete, name='detail'),
    path('path/', path_api),
]