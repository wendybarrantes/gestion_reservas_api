from rest_framework import serializers
from .models import Clientes, ZonasDisponibles, EstadoReservas, Reservar, CancelarReserva

class ClientesSerializer(serializers.ModelSerializer):
    """Serializer para la entidad Clientes"""
    class Meta:
        model = Clientes
        fields = '__all__'  # Incluye todos los campos del modelo Clientes
        
    def validate_nombre(self, value):
        """Valida que el nombre no esté vacío."""
        if not value.strip():
            # Lanza una excepción si el nombre está vacío o solo contiene espacios
            raise serializers.ValidationError("El nombre no puede estar vacío.")
        return value

def validate_email(self, value):
    """Valida que el email no esté en uso."""
    # Verifica si el cliente está siendo actualizado
    if self.instance and self.instance.email == value:
        return value
    
    if Clientes.objects.filter(email=value).exists():
        raise serializers.ValidationError("El email ya está en uso.")
    return value


    def validate_telefono(self, value):
        """Valida que el teléfono tenga 10 dígitos numéricos."""
        if not value.isdigit() or len(value) != 10:
            # Lanza una excepción si el teléfono no es numérico o no tiene 10 dígitos
            raise serializers.ValidationError("El teléfono debe tener 10 dígitos numéricos.")
        return value

class ZonasDisponiblesSerializer(serializers.ModelSerializer):
    """Serializer para la entidad Zonas Disponibles"""
    class Meta:
        model = ZonasDisponibles
        fields = '__all__'
        
    def validate_nombre(self, value):
        """Valida que el nombre de la zona no esté vacío y sea único."""
        if not value.strip():
            # Lanza una excepción si el nombre de la zona está vacío
            raise serializers.ValidationError("El nombre de la zona no puede estar vacío.")
        if ZonasDisponibles.objects.filter(nombre=value).exists():
            # Lanza una excepción si ya existe una zona con el mismo nombre
            raise serializers.ValidationError("Ya existe una zona con ese nombre.")
        return value

class EstadoReservasSerializer(serializers.ModelSerializer):
    """Serializer para la entidad Estado Reservas"""
    class Meta:
        model = EstadoReservas
        fields = '__all__'
        
    def validate_estado(self, value):
        """Valida que el estado no esté vacío."""
        if not value.strip():
            # Lanza una excepción si el estado está vacío
            raise serializers.ValidationError("El estado no puede estar vacío.")
        return value  # Retorna el valor si pasa la validación

class ReservarSerializer(serializers.ModelSerializer):
    """Serializer para la entidad Reservar"""
    class Meta:
        model = Reservar
        fields = '__all__'
        
    def validate(self, attrs):
        """Valida que el cliente y la zona existan antes de hacer la reserva."""
        if not Clientes.objects.filter(id=attrs['cliente_id']).exists():
            # Lanza una excepción si el cliente no existe
            raise serializers.ValidationError("El cliente no existe.")
        if not ZonasDisponibles.objects.filter(id=attrs['zona_id']).exists():
            # Lanza una excepción si la zona no existe
            raise serializers.ValidationError("La zona no existe.")
        # Aquí podrías agregar más validaciones para las fechas, si corresponde
        return attrs  # Retorna los atributos si pasan las validaciones

class CancelarReservaSerializer(serializers.ModelSerializer):
    """Serializer para la entidad Cancelar Reserva"""
    class Meta:
        model = CancelarReserva
        fields = '__all__'
