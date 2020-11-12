from django.test import TestCase
from django.urls import reverse


from .models import Articulo

class ArticuloModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        #Set up non-modified objects used by all test methods
        Articulo.objects.create(tipoArticulo=1, nombre='MK 11', precio=15000, img='null', stock=23)

    def test_first_name_label(self):
        articulo=Articulo.objects.get(id=1)
        field_label = articulo._meta.get_field('nombre').verbose_name
        self.assertEquals(field_label,'nombre')
