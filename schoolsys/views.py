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
        
        if tid:
            query=teacher.objects.filter(id=tid).values() #getting specifc record
            return Response(query) #returning response
        return Response(query)
    
    def post(self,request):
        data=request.data # request body
        teacher.objects.create(name=data['name'],subject=data['subject'],age=data['age']) #creating record
        
        return Response("data add sucessfully")


#student    
class FetchStudent(views.APIView):
    def post(self,request):
        try:
            body = request.data
            print(body)
            res=student.objects.create(name=body['name'],subject=body['subject'],class_name=body['class'],teacher_id_id=body['teacher']) # creating record for student and teacher_id_id is foriegn key of teacher id
            return Response("data added successfully")
        except Exception as e:
            return Response({"status":False,"message":str(e)})

    
    def get(self,request):
        try:
            sid = request.GET.get('student_id')#getting query params
            query=student.objects.all().values() #getting whole record
            
            if sid:
                query=student.objects.filter(id=sid).values() #getting specifc record
                return Response(query) #returning response
            return Response(query)
        except Exception as e:
            return Response({"status":False,"message":str(e)})




