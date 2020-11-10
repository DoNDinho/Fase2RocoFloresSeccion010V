from django.db import models

class Tipo_Articulo(models.Model):
    id = models.AutoField(primary_key=True)
    descripcion = models.CharField(max_length=50, help_text="Añada descripción del tipo artículo")

    class Meta:
        ordering=['descripcion']

    def __str__(self):
        return self.descripcion


class Articulo(models.Model):
    #id 
    tipoArticulo = models.ForeignKey(Tipo_Articulo, on_delete=models.CASCADE) 
    nombre = models.CharField(max_length=100)
    precio = models.IntegerField()
    img = models.ImageField(upload_to='static/articulos/img/articulos', null=True, blank=True)
    stock = models.IntegerField()

    class Meta:
        ordering=['nombre']

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    #id 
    nombre = models.CharField(max_length=100)
    telefono = models.CharField(max_length=12)
    email= models.EmailField(max_length= 30)
    sexo = models.CharField()
    contraseña = models.CharField(min=8 ,max_length=15)
    edad = models.IntegerField(max_length=2)
    img = models.ImageField(upload_to='static/articulos/img/usuarios', null=True, blank=True)
    

    class Meta:
        ordering=['nombre']

    def __str__(self):
        return self.nombre