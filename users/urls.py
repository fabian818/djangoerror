from django.urls import include, path

from users import views

urlpatterns = [
    path('test/', views.test),
]
