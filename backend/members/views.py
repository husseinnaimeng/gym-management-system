from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Member, WorkoutPlan, Membership
from .serializers import MemberSerializer, WorkoutPlanSerializer, MembershipSerializer

class MemberCreateAPIView(APIView):
    def get(self,request):
        
        objects = MemberSerializer(Member.objects.all(),many=True).data

        return Response(objects)
        
        return ''
    def post(self, request):
        serializer = MemberSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WorkoutPlanCreateAPIView(APIView):
    def post(self, request):
        serializer = WorkoutPlanSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MembershipCreateAPIView(APIView):
    def post(self, request):
        serializer = MembershipSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
