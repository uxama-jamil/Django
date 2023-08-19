from django.shortcuts import render
from rest_framework import viewsets,views
from schoolsys.models import student,teacher
from rest_framework.response import Response

# Create your views here.

#teacher
class FetchTeacherView(views.APIView):

    def get(self,request):
        print("request is ",request.GET.get('teacher_id'))
        tid = request.GET.get('teacher_id')#getting query params
        query=teacher.objects.all().values() #getting whole record
        
        if id:
            query=teacher.objects.filter(id=tid).values() #getting specifc record
            return Response(query) #returning response
        return Response(query)
    
    def post(self,request):
        data=request.data # request body
        data=teacher.objects.create(name=data['name'],subject=data['subject'],age=data['age']) #creating record
        
        return Response("data add sucessfully")


