import json
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from rest_framework.parsers import JSONParser
from django.contrib.auth.hashers import make_password
from django.http.response import JsonResponse
from django.utils.decorators import method_decorator

from Tareasapp.models import Tareas, Usuarios
from Tareasapp.serializers import TareasSerializer
# Create your views here.

# Create your views here.
class UsuarioView(View):
    
    #Esta función corrige el error por csrf, se puede omitir cuando en el formulario se agrega csrf token
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request):
        """
        Con esta función se pueden registrar usuarios en la base de datos, recibe un JSON con los
        atributos: 'name','last_name','email','password'
        La contraseña se encripta con la función make_password()
        Al ser usada con el método POST y con los datos del JSON correctos,
        Retorna un estado 200 y el mensaje "Exito"
        La ruta utilizada es '/api/auth/register'
        """
        if request.method == 'POST':
            jd = json.loads(request.body)
            Usuarios.objects.create(name=jd['name'],last_name=jd['last_name'],email=jd['email'],
            password=make_password(jd['password']))
            datos={'mensaje':'Exito'}
            return JsonResponse(datos) 
        else:
            datos={'mensaje':'Aquí se registran usuarios'}
            return JsonResponse(datos)  

@csrf_exempt
def tareas_api(request,id=0):
    if request.method == 'GET':
        tarea = Tareas.objects.all()
        tarea_serializer = TareasSerializer(tarea,many=True)
        return JsonResponse(tarea_serializer.data,safe=False)
    elif request.method == 'POST':
        tarea_data = JSONParser().parse(request)
        tarea_serializer = TareasSerializer(data=tarea_data)
        if tarea_serializer.is_valid():
            tarea_serializer.save()
            return JsonResponse({"mensaje":"agregada correctamente"},safe=False)
        return JsonResponse({"mensaje":"fallo al agregar"},safe=False)
    elif request.method == 'DELETE':
        tarea = Tareas.objects.get(id_tarea=id)
        tarea.delete()
        return JsonResponse({"mensaje":"tarea eliminada correctamente"},safe=False)

