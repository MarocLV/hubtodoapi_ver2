from django.urls import path
from Tareasapp import views

urlpatterns = [
    path('tareas', views.tareas_api),
    path('auth/register',views.UsuarioView.as_view(), name='usuarios_list'),
    path('tareas/eliminar/<id>',views.tareas_api)
]