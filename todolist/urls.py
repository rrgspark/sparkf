from django.urls import path, include
from . import views
urlpatterns = [ 
    path('', views.main, name='main'),
    path('registrar_item', views.registrar_item, name='registrar_item'),
    path('actualizar_item', views.actualizar_item, name='actualizar_item'),
    path('delete_item/<item_id>', views.delete_item, name='delete_item')
]