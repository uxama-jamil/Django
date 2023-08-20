from rest_framework import serializers
from .models import *

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model= teacher
        fields = '__all__' # for specific field ['name','subject'......]
