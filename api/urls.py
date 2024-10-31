from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    # URLs para Clientes
path('clientes/', views.ClientesListCreate.as_view(), name='clientes-list'),
path('clientes/<int:pk>/', views.ClientesDetail.as_view(), name='clientes-detail'),
    # URLs para ZonasDisponibles
path('zonas/',views.ZonasDisponiblesListCreate.as_view(), name='zonasDisponibles-list'),
path('zonasDisponibles/<int:pk>/', views.ZonasDisponiblesDelete.as_view(),name='zonasDisponibles-detail'),
    # URLs para EstadoReservas
path('EstadoReservas/', views.EstadoReservasListCreate.as_view(), name='EstadoReservas-list'),
path('EstadosReservas/<int:pk>/', views.EstadoReservasDelete.as_view(), name='EstadoReservas-detail'),
    # URLs para Reservar
path('reservar/', views.ReservarListCreate.as_view, name='reservar-list-'),
path('reservar/<int:pk>/', views.ReservarDelete.as_view(), name='reservar-detail'),
    # URLs para CancelarReserva
path('cancelarReserva/', views.CancelarReservaListCreate.as_view, name= 'cancelarReserva-detail'),
path('cancelarReserva/<int:pk>/', views.CancelarReservaDetail.as_view(), name='cancelarReservar-detail'),
    #URLs para token   
path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
path('token/resfresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
]