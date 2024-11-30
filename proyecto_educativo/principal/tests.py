from django.test import TestCase
from .models import Estudiante
from django.urls import reverse, resolve

# Pruebas para el Modelo
class EstudianteModelTest(TestCase):
    def setUp(self):
        self.estudiante = Estudiante.objects.create(
            nombre="Juan",
            apellido="Pérez",
            correo="juan.perez@gmail.com",
            edad=20,
        )

    def test_estudiante_creation(self):
        """Probar si un estudiante se crea correctamente"""
        self.assertEqual(self.estudiante.nombre, "Juan")
        self.assertEqual(self.estudiante.apellido, "Pérez")
        self.assertEqual(self.estudiante.correo, "juan.perez@gmail.com")
        self.assertEqual(self.estudiante.edad, 20)

    def test_estudiante_str(self):
        """Probar el método __str__ del modelo"""
        self.assertEqual(str(self.estudiante), "Juan Pérez")


# Pruebas para las Vistas
class EstudianteViewTest(TestCase):
    def setUp(self):
        self.estudiante = Estudiante.objects.create(
            nombre="Ana",
            apellido="Gómez",
            correo="ana.gomez@gmail.com",
            edad=22,
        )

    def test_home_view(self):
        """Probar que la vista home carga correctamente"""
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'principal/home.html')
        self.assertContains(response, "Lista de Estudiantes")

    def test_detalle_view(self):
        """Probar que la vista detalle carga correctamente"""
        response = self.client.get(reverse('detalle_estudiante', args=[self.estudiante.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'principal/detalle.html')
        self.assertContains(response, self.estudiante.nombre)
        self.assertContains(response, self.estudiante.apellido)


# Pruebas para las URLs
class EstudianteURLTest(TestCase):
    def test_home_url(self):
        """Probar que la URL de home apunta a la vista correcta"""
        resolver = resolve('/')
        self.assertEqual(resolver.view_name, 'home')

    def test_detalle_url(self):
        """Probar que la URL de detalle apunta a la vista correcta"""
        resolver = resolve(f'/estudiante/{1}/')
        self.assertEqual(resolver.view_name, 'detalle_estudiante')