from dataclasses import fields
from rest_framework import serializers
from Tareasapp.models import Tareas

class TareasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tareas
        fields = ('id_tarea', 'title','dead_line', 'description', 'isCompleted', 'priority_id', 'user_id')