from django.urls import path, include
from . import views
urlpatterns = [
    path('',include('django.contrib.auth.urls')), 
    path('logout', views.logout, name="logout"), 
    path('registrar', views.registrar, name="registrar"),
    path('recuperar_pass', views.recuperar_pass, name="recuperar_pass"),
    path('cambiar_pass/<user_id>', views.cambiar_pass, name="cambiar_pass")
]