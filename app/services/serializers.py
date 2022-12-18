from rest_framework import serializers

from app.services.models import TypeServices, Package, Deliverables


# It creates a serializer for the Deliverables model.
class DeliverablesSerializer(serializers.ModelSerializer):
    # A serializer class that will be used to serialize the data from the model.
    class Meta:
        model = Deliverables
        fields = '__all__'


# The PackageSerializer class is a ModelSerializer that has a field called deliverables that is a
# DeliverablesSerializer
class PackageSerializer(serializers.ModelSerializer):
    # Creating a serializer for the Deliverables model.
    deliverables = DeliverablesSerializer()

    class Meta:
        model = Package
        fields = ['id', 'description', 'precio', 'deliverables']


# The TypeServicesSerializer serializes the TypeServices model, and includes the PackageSerializer in
# the package field.
class TypeServicesSerializer(serializers.ModelSerializer):
    package = PackageSerializer()

    class Meta:
        model = TypeServices
        fields = ['id', 'name', 'package']
