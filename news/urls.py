
from django.urls import path
from .views import home, articoloDetailView

app_name = "news"  

urlpatterns = [
    path("", home, name="homeview"),
    path("articoli/<int:pk>/", articoloDetailView, name="lista_articoli_detail"), 
    path("lista_articoli/<int:pk>/", articoloDetailView, name="lista_articoli"),  
    path("articoli/", articoloDetailView, name="lista_articoli"),  
]