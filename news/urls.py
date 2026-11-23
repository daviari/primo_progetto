
from django.urls import path
from .views import home, articoloDetailView, lista_articoli, queryBase, giornalistaDetailView,lista_giornalisti

app_name = "news"  

urlpatterns = [
    path("", home, name="homeview"),
    path("articoli/<int:pk>/", articoloDetailView, name="lista_articoli_detail"), 
    path("lista_articoli/<int:pk>/", articoloDetailView, name="lista_articoli"),  
    path("lista_articoli/", lista_articoli, name="lista_articoli"), 
    path("queryBase/", queryBase, name="queryBase"),
    path("giornalista_detail/<int:pk>", giornalistaDetailView, name="giornalista_detail"), 
    path("lista_giornalisti/", lista_giornalisti, name="lista_giornalisti"), 
]