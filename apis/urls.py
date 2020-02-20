from django.urls import path
from django.urls import include
from rest_framework import routers
from .views import HeroViewSet, SupermanViewSet


router = routers.DefaultRouter()
router.register(r'heroes',HeroViewSet)
superman= routers.DefaultRouter()
superman.register(r'heroes',SupermanViewSet)

urlpatterns =[
    path('', include(router.urls)),
    path('superman/', include(superman.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]