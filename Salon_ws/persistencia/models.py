from django.db import models

# Create your models here.
class DatosContacto(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    nombres = models.CharField(db_column='NOMBRES', max_length=50)  # Field name made lowercase.      
    apellido_pat = models.CharField(db_column='APELLIDO_PAT', max_length=50)  # Field name made lowercase.
    apellido_mat = models.CharField(db_column='APELLIDO_MAT', max_length=50)  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=80)  # Field name made lowercase.
    telefono = models.CharField(db_column='TELEFONO', max_length=15)  # Field name made lowercase.     
    asunto = models.CharField(db_column='ASUNTO', max_length=350)  # Field name made lowercase.        

    def __str__(self):
        return 'ID: {0}, NOMBRES {1}, APELLIDO_PATERNO: {2}, APELLIDO_MATERNO: {3}'.format(
            self.id, self.nombres, self.apellido_pat, self.apellido_mat)

    def json_serializer(self):
        return {
                'id': self.id,
                'nombres': self.nombres,
                'apellido_pat': self.apellido_pat,
                'apellido_mat': self.apellido_mat,
                'email': self.email,
                'telefono': self.telefono,
                'asunto': self.asunto,
                }

    class Meta:
        managed = False
        db_table = 'datos_contacto'