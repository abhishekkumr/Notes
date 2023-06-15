from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Notes
from rest_framework.response import Response
from .serializer import NotesSerializer
from rest_framework import status
from rest_framework.views import APIView

#here we imported a decorater.
#@api_view(['GET','POST','PUT','PATCH','DELETE'])

#Here we define a class Named Notesapi.

class Notesapi(APIView):
#This is the first method post from which we can POST our data. 
    def post(self, request, format=None):
        serializer = NotesSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'}, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#This is the second method get from which we can partially update our data. 
    def get(self, request, pk=None, format=None):
        id = pk
        if id is not None:
            dta = Notes.objects.get(id=id)
            serializer = NotesSerializer(dta)
            return Response(serializer.data)
        dta = Notes.objects.all()
        serializer = NotesSerializer(dta, many=True)
        return Response (serializer.data)

#This is the third method PUT from which we can partially update our data. 
    def put(self,request, pk, format=None):
        id = pk
        dta = Notes.objects.get(pk=id)
        serializer = NotesSerializer(dta, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data updated'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#This is the forth method PATCH from which we can partially update our data.
    def patch(self,request,pk, format=None):
        id = pk
        dta = Notes.objects.get(pk=id)
        serializer = NotesSerializer(dta, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'data patial updated'})
        return Response(serializer.errors)    

#This is the fivth method Detele from which we can partially update our data.
    def delete(request,self, pk, format=None):
        id = pk
        dta = Notes.objects.get(pk=id)
        dta.delete()
        return Response({'msg':'Data Deleted'})