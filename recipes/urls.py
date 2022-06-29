from django.urls import path

from . import views  # da pasta atual import vies

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"),  # Home
    path('recipes/<int:id>/', views.recipe, name="recipe"),
]
