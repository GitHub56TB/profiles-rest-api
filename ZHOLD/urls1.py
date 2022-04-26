from django.urls import path, include

from rest_framework.routers import DefaultRouter

from profiles_api import views

router = DefaultRouter()
router.register(r'hello-viewset', views.HelloViewSet,
                basename='hello-viewset')  # Training Class 40 - https://www.django-rest-framework.org/api-guide/viewsets/ (use basename versus base_name; 'r' is optional)


urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('', include(router.urls))
]
