from django.db import models

class estudiante(models.Model):
    cod_estudiante = models.IntegerField(primary_key=True)
    nombre_apellido = models.CharField(max_length=255)
    cedula = models.IntegerField()
    nacimiento = models.DateField(null=True, blank=True)
    fecha_inscripcion = models.DateField(null=True, blank=True)
    direccion = models.CharField(max_length=255)
    correo = models.CharField(max_length=255)
    
class asignatura(models.Model):
    cod_asig = models.IntegerField(primary_key=True)
    unidad_credito = models.IntegerField()
    nombre = models.CharField(max_length=255)
    requisito = models.ManyToManyField('self', blank=True)
    
class seccion(models.Model):
    cod_seccion = models.IntegerField(primary_key=True)
    capacidad = models.IntegerField()
    
class profesor(models.Model):
    cod_profesor = models.IntegerField(primary_key=True)
    nombre = models.CharField(max_length=255)
    ci_profesor = models.IntegerField()        

class estudiante_asignatura(models.Model):
    estudiante = models.ForeignKey(estudiante, on_delete=models.CASCADE, db_column='cod_estudiante')
    asignatura = models.ForeignKey(asignatura, on_delete=models.CASCADE, db_column='cod_asig')