from django.http import HttpResponse
from django.shortcuts import render
from MTV.models import Familiar
from django.template import Context, Template, loader

# Create your views here.

def familiar(self):

    familiar= Familiar(tipo_de_familiar="Padre", nombre="Juan", apellido="Perez", edad=32, fecha_nacimiento="1990-4-15")
    familiar.save()

    hijo=Familiar(tipo_de_familiar="Hijo", nombre="Esteban", apellido="Perez", edad=19, fecha_nacimiento="2003-6-25")
    hijo.save()

    madre=Familiar(tipo_de_familiar="Madre", nombre="Laura", apellido="Rodriguez", edad=30, fecha_nacimiento="1992-3-12")
    madre.save()

    diccionario={"tipo_de_familiar":familiar.tipo_de_familiar, "nombre":familiar.nombre, "apellido":familiar.apellido, "edad":familiar.edad, "fecha_nacimiento":familiar.fecha_nacimiento, "tipo_de_familiarr":hijo.tipo_de_familiar, "nombreHijo":hijo.nombre, "apellidoHijo":hijo.apellido, "edadHijo":hijo.edad, "nacimientoHijo":hijo.fecha_nacimiento, "tipoFamiliar":madre.tipo_de_familiar, "nombreMadre":madre.nombre, "apellidoMadre":madre.apellido, "edadMadre":madre.edad, "nacimientoMadre":madre.fecha_nacimiento}

    plantilla=loader.get_template("template.html")

    documento=plantilla.render(diccionario)
    return HttpResponse(documento)