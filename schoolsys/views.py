from django.shortcuts import render
from rest_framework import viewsets,views
from schoolsys.models import student,teacher
from rest_framework.response import Response
from .serializer import *

# Create your views here.

#teacher
class FetchTeacherView(views.APIView):

    def get(self,request):
        print("request is ",request.GET.get('teacher_id'))
        tid = request.GET.get('tid')#getting query params
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
        
    def delete(self,request):
        tid = request.data.get('tid',False)
        query = teacher.objects.filter(id=tid)
        if not tid:
            return Response("Tid is  requried")
        if query:
            print(query,"teahcersss")

            query.delete()
            return Response("Data deleted")
        else:
            return Response("no record found")


#student    
class FetchStudent(views.APIView):
    def post(self,request):
        try:
            body = request.data
            ser = StudentSerializer(data=body)
            if ser.is_valid():
                ser.save()
                return Response({'status':True,'message':ser.data})
            else:
                return Response({"status":False,"message":ser.errors})
                
        except Exception as e:
            return Response({"status":False,"message":str(e)})

    def patch(self,request):

        body = request.data
        query = student.objects.all().get(id=body['sid'])
        ser = StudentSerializer(query,data=body,partial=True)
        if ser.is_valid():
            ser.save()
            return Response("Data updated")
        else:
            return Response(ser.errors)



    
    def get(self,request):
        try:
            data = request.GET.get('sid') #getting data from query params
            query=student.objects.all() #getting whole record
            ser = StudentSerializer(query,many=True)
            if data:
                query=student.objects.get(id=data) #getting specifc record
                ser = StudentSerializer(query)

                return Response(ser.data) #returning response
            return Response(ser.data)
        except Exception as e:
            return Response({"status":False,"message":ser.errors})
        
    def delete(self,request):
        data = request.data
        query = student.objects.get(id=data['sid'])
        if 'sid' in data:
            query.delete()
            Response("Data deleted")
        else:
            Response("sid is missing")
    





