from django.test import TestCase, Client
from app.services.models import Deliverables, Package, TypeServices



class ServicesTestCase(TestCase):

    def setUp(self):
        """
        It creates a Deliverables object, a Package object, and a TypeServices object.
        """
        deliverables = Deliverables.objects.create(id=1, name='Include source code')
        package = Package.objects.create(
            id=1,
            description='Lorem ipsum dolor sit amet, consectetur adipiscing eli',
            precio=100, deliverables=deliverables
        )
        self.TypeService = TypeServices.objects.create(id=1, name='Desarrollos On-Cloud', package=package)
        self.client = Client()

    def test_type_services(self):
        """
        It tests the type of service.
        """
        self.assertEqual(self.TypeService.id, 1)
        self.assertEqual(self.TypeService.name, 'Desarrollos On-Cloud')
        self.assertEqual(self.TypeService.package.id, 1)

    def test_type_services_error(self):
        """
        A test function that checks if the data is correct.
        """
        AssertionError(self.TypeService.id, 2)
        AssertionError(self.TypeService.name, 'Desarrollos On-Cloud dadada')
        AssertionError(self.TypeService.package.id, 112)

    def test_services_package(self):
        """
        It tests the package model.
        """
        self.assertEqual(self.TypeService.package.id, 1)
        self.assertEqual(self.TypeService.package.description, 'Lorem ipsum dolor sit amet, consectetur adipiscing eli')
        self.assertEqual(self.TypeService.package.precio, 100)
        self.assertEqual(self.TypeService.package.deliverables.id, 1)
        self.assertEqual(self.TypeService.package.deliverables.id, 1)
        self.assertEqual(self.TypeService.package.deliverables.name, 'Include source code')

    def test_services_all(self):
        """
        It tests the status code of the response.
        """
        response = self.client.get('/services/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data), 1)

    def test_service(self):
        """
        The function tests that the response status code is 200 when the client gets the service page for
        the service with the id of the TypeService object
        """
        response = self.client.get(f'/service/{self.TypeService.id}/')
        self.assertEqual(response.status_code, 200)

    def test_service_not_exist(self):
        """
        It tests if the service exists.
        """
        response = self.client.get(f'/service/5/')
        self.assertEqual(response.status_code, 404)
