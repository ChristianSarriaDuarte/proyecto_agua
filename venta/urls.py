from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('registrarPedido/', views.registrarPedido),
    path('home/edicionPedido/<codigo>', views.edicionPedido),
    path('editarPedido/', views.editarPedido),
    path('home/eliminarPedido/<codigo>', views.eliminarPedido),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
    path('venta_de_agua/', views.venta_de_agua, name='venta_de_agua'),
    path('catalogo/', views.catalogo, name='catalogo'),
    path('confirmarCompra/', views.confirmar_compra, name='confirmar_compra')
]
