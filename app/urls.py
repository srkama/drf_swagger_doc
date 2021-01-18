from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from app import api

router = routers.DefaultRouter()
router.register(r'tasks', api.TaskViewset)

urlpatterns = [
    path('api/', include(router.urls)),
    path('add_numbers/', api.add_two_numbers)
]
