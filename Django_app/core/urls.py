from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.home, name='home'),
    path('', views.root, name='root'),  # URL para la página de login
    path('login/', views.login, name='login'),  # URL para la página de login
    path('contacto/', views.contacto, name='contacto'),  # URL para la página de contacto
    path('categoria/lucha/', views.categoria_lucha, name='categoria_lucha'),
    path('categoria/accion/', views.categoria_accion, name='categoria_accion'),
    path('categoria/carreras/', views.categoria_carreras, name='categoria_carreras'),
    path('categoria/deporte/', views.categoria_deporte, name='categoria_deporte'),
    
    path('categoria/terror/', views.categoria_terror, name='categoria_terror'),
    path('categoria/shooter/', views.categoria_shooter, name='categoria_shooter'),
   
    # Otras URL de la aplicación
    path('juego/juego_accion1/', views.juego_accion1, name='juego_accion1'),

    path('juego/<int:id>/', views.juego_show, name='juego_show'),
    # path('mostrar/<int:id>/', views.mostrar, name='mostrar')
    
    path('juego/', views.juego_index, name='juego_index'),
    path('juego/create/', views.juego_create, name='juego_create')



]
             