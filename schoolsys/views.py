from django.shortcuts import render
from rest_framework import viewsets,views
from schoolsys.models import student,teacher
from rest_framework.response import Response
from .serializer import TeacherSerializer

# Create your views here.

#teacher
class FetchTeacherView(views.APIView):

    def get(self,request):
        print("request is ",request.GET.get('teacher_id'))
        tid = request.GET.get('teacher_id')#getting query params
        query=teacher.objects.all() #getting whole record
        ser = TeacherSerializer(query,many=True) # many true means it will have more than one record
        
        if tid:
            query=teacher.objects.get(id=tid) #getting specifc record
            ser = TeacherSerializer(query)  #passing queryset for json coversion

            return Response(ser.data) #returning response
        return Response(ser.data)
    
    def post(self,request):
        data=request.data # request body
        # teacher.objects.create(name=data['name'],subject=data['subject'],age=data['age']) #creating record
        ser = TeacherSerializer(data=data) #using serializer passing request body in data argument which created record 
        if ser.is_valid(): #checking if record is valid
            ser.save() # record creation
            return Response({'status':True,'message':ser.data},200)
            
        else:
            return Response({'status':False,'error':ser.errors},400)
        
    def patch(self,request):
        data=request.data # request body
        tid = request.GET.get('teacher_id')#getting query params , this way not safe

        query=teacher.objects.get(id=data['tid']) #getting specifc record 
        
        ser = TeacherSerializer(query,data=data,partial=True) # partial true mean it will update specific fields if there is a queryset
        if ser.is_valid():
            ser.save()
            return Response({'status':True,'message':ser.data},200)
            
        else:
            return Response({'status':False,'error':ser.errors},400)


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




