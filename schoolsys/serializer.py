from rest_framework import serializers
from .models import *

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model= teacher
        fields = '__all__' # for specific field ['name','subject'......]


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = student
        fields = "__all__"

    def validate_age(self,val): #single field validation 
        print("value is ", val)
        if val>100:
            raise serializers.ValidationError({"age":"age cannot be greater than 100"})
        return val
    
    def validate(self,val): # multi field validation
        if val['subject'].lower() in ['urdu','sindhi'] and len(val['name'])>10:
            raise serializers.ValidationError({'subject':f"subject cannot be {val['subject']}",
                                               'name':'name cannot be greater than 10'})
        return val
