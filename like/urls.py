from django.urls import path,include
from .views import toggel_like,CommentViewSet 
from rest_framework.routers import DefaultRouter

router=DefaultRouter()
router.register('comment',CommentViewSet)

urlpatterns=[
    path('Like/<int:id>/',toggel_like),
    path('',include(router.urls)),
]