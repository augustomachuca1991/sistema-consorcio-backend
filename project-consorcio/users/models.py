from django.db import models
#from tipo_usuario.models import TipoUsuario
#from permiso_usuario.models import PermisoUsuario

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    #id_permiso = models.ForeignKey(PermisoUsuario, on_delete=models.CASCADE)
    #id_tipoUsuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.username
