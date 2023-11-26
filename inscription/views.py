from django.shortcuts import render
from django.http import HttpResponse
from .models import estudiante

# Create your views here.
def insert_student(request):
    if request.method == 'POST':
        nombre = request.POST['NOMBRE']
        cedula = request.POST['CEDULA']
        nacimiento = request.POST['dob']
        direccion = request.POST['DIRECCION']
        correo = request.POST['CORREO']
        # Retrieve other form fields similarly

        # Create a new estudiante object and save it to the database
        new_student = estudiante(nombre_apellido=nombre, cedula=cedula, nacimiento=nacimiento, direccion=direccion, correo=correo)
        new_student.save()
        return HttpResponse('Student inserted successfully')
    else:
        return render(request, 'your_template.html')
