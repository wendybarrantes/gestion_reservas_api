"""Module providing a function printing python version."""

from django.db import models

class Clientes(models.Model):
    """Clase clientes"""
    nombre_cliente = models.CharField(max_length=100)
    apellido_cliente = models.CharField(max_length=100)
    email_cliente = models.EmailField()
    telefono_cliente = models.CharField(max_length=15)
    clave_cliente = models.CharField(max_length=15)  # Corregido a CharField

class ZonasDisponibles(models.Model):  # Renombrado a CamelCase
    """Clase zonas disponibles"""
    oficinas = models.BooleanField(default=True)  # True indica que está disponible
    salas_de_reuniones = models.BooleanField(default=True)
    escritorios = models.BooleanField(default=True)

    def __str__(self):
        return f"Oficinas: {'Disponibles' if self.oficinas else 'No Disponibles'}, " \
               f"Salas de Reuniones: {'Disponibles' if self.salas_de_reuniones else 'No Disponibles'}, " \
               f"Escritorios: {'Disponibles' if self.escritorios else 'No Disponibles'}"

class EstadoReservas(models.Model):  # Renombrado a CamelCase
    """Clase estado de reservas"""
    ESTADO_OPCIONES = [
        ('activa', 'Activa'),
        ('cancelada', 'Cancelada'),
        ('completada', 'Completada'),
        ('pendiente', 'Pendiente'),
        ('no_show', 'No Show'),
        ('expirada', 'Expirada'),
    ]

    estado = models.CharField(max_length=20, choices=ESTADO_OPCIONES, unique=True)

    def __str__(self):
        return self.estado

class Reservar(models.Model):
    """Clase reserva"""
    fecha_reserva = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    numero_personas = models.IntegerField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    zonas_disponibles = models.ForeignKey(
        ZonasDisponibles,
        on_delete=models.CASCADE)  # Corregido a CamelCase

    def __str__(self):
        return f"Reserva de {self.cliente} para {self.zonas_disponibles} el {self.fecha_reserva}"

class CancelarReserva(models.Model):  # Renombrado a CamelCase
    """Class representing a person"""
    fecha_cancelacion = models.DateTimeField()  # Corregido 'feccha_cancelacion'
    motivo = models.CharField(max_length=100)  # Cambiado a 'motivo'
    reserva = models.ForeignKey(Reservar, on_delete=models.CASCADE)

    def __str__(self):
        return f"Cancelación de reserva ID: {self.reserva.id} - Motivo: {self.motivo}"
