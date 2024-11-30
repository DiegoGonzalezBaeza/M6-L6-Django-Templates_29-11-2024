# M6-L6-Django-Templates_29-11-2024 - Explicación de Tests Unitarios
Proyecto educativo

Este documento explica a detalle los tests unitarios implementados en el proyecto educativo, abordando el modelo, las vistas y las URLs. Los tests garantizan que los componentes principales del proyecto funcionen correctamente.

---

## Pruebas Implementadas

### Archivo: `principal/tests.py`

#### Importaciones
```python
from django.test import TestCase
from .models import Estudiante
from django.urls import reverse, resolve
```
- **`TestCase`**: Clase base para escribir tests. Proporciona un entorno aislado con una base de datos temporal.
- **`Estudiante`**: Modelo del que se verifican sus funcionalidades.
- **`reverse`**: Genera URLs basadas en los nombres definidos en `urls.py`.
- **`resolve`**: Mapea URLs a sus vistas correspondientes.

---

### Pruebas del Modelo: `EstudianteModelTest`
Este conjunto de tests verifica que el modelo `Estudiante` funciona como se espera.

#### Código
```python
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
```

#### Explicación
1. **`setUp`**:
   - Crea un objeto `Estudiante` que será usado en los tests.
2. **`test_estudiante_creation`**:
   - Verifica que los datos del modelo se guarden correctamente.
   - Usa `assertEqual` para comparar los valores esperados y los obtenidos.
3. **`test_estudiante_str`**:
   - Comprueba que el método `__str__` devuelva el formato esperado: `nombre` y `apellido`.

---

### Pruebas de las Vistas: `EstudianteViewTest`
Este conjunto de tests evalúa las vistas `home` y `detalle_estudiante`.

#### Código
```python
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
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, "Lista de Estudiantes")

    def test_detalle_view(self):
        """Probar que la vista detalle carga correctamente"""
        response = self.client.get(reverse('detalle_estudiante', args=[self.estudiante.id]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'detalle.html')
        self.assertContains(response, self.estudiante.nombre)
        self.assertContains(response, self.estudiante.apellido)
```

#### Explicación
1. **`setUp`**:
   - Crea un estudiante para usarlo en las pruebas de las vistas.
2. **`test_home_view`**:
   - Verifica que la vista `home`:
     - Devuelva un código HTTP 200.
     - Use el template `home.html`.
     - Contenga el texto "Lista de Estudiantes".
3. **`test_detalle_view`**:
   - Verifica que la vista `detalle_estudiante`:
     - Devuelva un código HTTP 200.
     - Use el template `detalle.html`.
     - Contenga el nombre y apellido del estudiante.

---

### Pruebas de las URLs: `EstudianteURLTest`
Este conjunto de tests evalúa si las URLs están configuradas correctamente.

#### Código
```python
class EstudianteURLTest(TestCase):
    def test_home_url(self):
        """Probar que la URL de home apunta a la vista correcta"""
        resolver = resolve('/')
        self.assertEqual(resolver.view_name, 'home')

    def test_detalle_url(self):
        """Probar que la URL de detalle apunta a la vista correcta"""
        resolver = resolve(f'/estudiante/{1}/')
        self.assertEqual(resolver.view_name, 'detalle_estudiante')
```

#### Explicación
1. **`test_home_url`**:
   - Usa `resolve` para verificar que la URL `/` apunta a la vista `home`.
2. **`test_detalle_url`**:
   - Verifica que la URL `/estudiante/1/` apunta a la vista `detalle_estudiante`.

---

## Cómo Ejecutar los Tests

1. Asegúrate de estar en el entorno virtual:
   ```bash
   source venv/bin/activate  # En Linux/macOS
   venv\Scripts\activate     # En Windows
   ```

2. Ejecuta los tests con el comando:
   ```bash
   python manage.py test
   ```

3. Revisa el resultado. Un ejemplo de salida esperada:
   ```
   Found 6 test(s).
   Creating test database for alias 'default'...
   System check identified no issues (0 silenced).
   ......
   ----------------------------------------------------------------------
   Ran 6 tests in 0.034s

   OK
   Destroying test database for alias 'default'...
   ```

---

## Conclusión

Este conjunto de tests cubre:
- **Modelo**: Verifica la integridad de los datos y el formato del método `__str__`.
- **Vistas**: Garantiza que las vistas funcionen correctamente y rendericen los templates adecuados.
- **URLs**: Comprueba que las rutas estén correctamente configuradas.

Con estos tests, aseguramos que los componentes principales de la aplicación sean confiables y estén libres de errores.

---

## hosting:

https://clientes.v2networks.cl/aff.php?aff=176