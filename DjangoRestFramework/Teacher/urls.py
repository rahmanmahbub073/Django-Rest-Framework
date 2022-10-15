from django.urls import path, include
from Teacher import views
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'Teachers', views.TeacherViewSet,basename="Teachers")
router.register(r'groups', views.GroupViewSet,basename="groups")

urlpatterns = [
    path('', include(router.urls)),
    # path('TeacherView/', views.TeacherViewSet),
    # path('GroupView/', views.GroupViewSet),
]