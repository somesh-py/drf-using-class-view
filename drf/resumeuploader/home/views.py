from django.shortcuts import render
from home.models import Profile
from home.serializers import ProfileSerializer
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
# Create your views here.

class ProfileView(APIView):
    def post(self,request,format=None):
        serializer=ProfileSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'resume uploaded sucessfully','status':'sucess','candidate':serializer.data},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    
    # def get(self,request,format=None):
    #     candidates=Profile.objects.all()

    def get(self,request,format=None):
        candidates=Profile.objects.all()
        serializer=ProfileSerializer(candidates,many=True)
        return Response({'status':'sucess','candidates':serializer.data},status=status.HTTP_200_OK)

    def delete(self,request,formate=None):
        candidates=Profile.objects.all()
        return Response({'status':'success'})