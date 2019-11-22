from django.db import models

# Create your models here.

class Alumno(models.Model):
	ApellidoPaterno = models.CharField(max_length=35)
	ApellidoMaterno = models.CharField(max_length=35)
	Nombres = models.CharField(max_length=35)
	DN1 = models.CharField(max_length=8)
	

	def NombreCompleto(self):
		cadena="{0} {1},{2}"
		return cadena.format(self.ApellidoPaterno,self.ApellidoMaterno,self.Nombres)


	def __str__(self):
		return self.NombreCompleto()

class Curso(models.Model):
	NombreCurso = models.CharField(max_length=50)
	Creditos = models.PositiveSmallIntegerField()

	def __str__(self):
		return "{0}".format(self.NombreCurso)


class Matricula(models.Model):
	Alumno=models.ForeignKey(Alumno,default=False,blank=False,on_delete=models.CASCADE)
	Curso=models.ForeignKey(Curso,default=False,blank=False,on_delete=models.CASCADE)

	def __str__(self):
		cadena = "{0} => {1}"
		return cadena.format(self.Alumno,self.Curso.NombreCurso)
