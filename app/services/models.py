from django.db import models


# Create your models here.

class Deliverables(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'services_deliverables'


class Package(models.Model):
    description = models.CharField(max_length=200, blank=True, null=True)
    precio = models.IntegerField()
    deliverables = models.ForeignKey(Deliverables, related_name='deliverables', on_delete=models.CASCADE)

    def __str__(self):
        return self.description

    class Meta:
        db_table = 'services_package'


class TypeServices(models.Model):
    name = models.CharField(max_length=150, blank=True, null=True)
    package = models.ForeignKey(Package, related_name='package', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'services_typeservices'
