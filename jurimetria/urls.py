from django.urls import path

from . import views


app_name = "jurimetria"
urlpatterns = [
    path("", views.index, name="index"),
    path("resultado/", views.result, name="result"),
    path("<int:sentenca_id>/", views.detail, name="detail"),
]
