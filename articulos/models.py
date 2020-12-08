from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

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



"""
MODELOS PARA AGREGAR USUARIO
"""
class Sexo(models.Model):
    id = models.AutoField(primary_key=True)
    sexo = models.CharField(max_length=50, help_text="Añada descripción del tipo sexo")

    class Meta:
        ordering=['sexo']

    def __str__(self):
        return self.sexo


class UsuarioManager(BaseUserManager):
    def create_user(self, email, nombreUsuario, telefono, sexo, edad, password=None):
        if not email:
            raise ValueError('El usuario debe tener un email!')

        usuario = self.model(
            nombreUsuario = nombreUsuario,
            telefono = telefono,
            email = self.normalize_email(email),
            sexo = Sexo(pk=sexo),
            edad = edad
        )

        usuario.set_password(password)
        usuario.save()
        return usuario

    def create_superuser(self, email, nombreUsuario, telefono, sexo, edad, password):
        usuario = self.create_user(
            email,
            nombreUsuario = nombreUsuario,
            telefono = telefono,
            sexo = sexo,
            edad = edad,
            password = password
        )

        usuario.usuarioAdmin = True
        usuario.save()
        return usuario


class Usuario(AbstractBaseUser):
    email= models.EmailField('Correo Electrónico', unique=True, max_length= 30)
    nombreUsuario = models.CharField('Nombre de usuario', max_length=100)
    telefono = models.CharField('Telefono', max_length=12)
    sexo = models.ForeignKey(Sexo, on_delete=models.CASCADE)
    edad = models.IntegerField()
    password = models.CharField(null=True, max_length=30)
    img = models.ImageField('Imagen de Perfil', upload_to='static/articulos/img/usuarios', null=True, blank=True)
    usuarioActivo = models.BooleanField(default=True)
    usuarioAdmin = models.BooleanField(default=False)
    objects = UsuarioManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombreUsuario', 'telefono', 'sexo', 'edad', 'password']

    def __str__(self):
        return self.email

    # Metodo para acceder a usuario desde admin de django
    def has_perm(self, perm, obj = None):
        return True

    def has_module_perms(self, app_label):
        return True

    # Devuelve si es usuario admin
    @property
    def is_staff(self):
        return self.usuarioAdmin
