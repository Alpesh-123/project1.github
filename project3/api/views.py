from rest_framework.views import APIView
from .serializers import StudentSerializer
from rest_framework.response import Response


class CalculatePercentage(APIView):
    def post(self, request):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            polity = serializer.validated_data['polity']
            science_technology = serializer.validated_data['science_technology']
            art_culture = serializer.validated_data['art_culture']
            history = serializer.validated_data['history']
            maths = serializer.validated_data['maths']
            reasoning =serializer.validated_data['reasoning']
            ethics = serializer.validated_data['ethics']
            geography = serializer.validated_data['geography']
            literature = serializer.validated_data['literature']
            economics = serializer.validated_data['economics']
            
            total_marks = polity + science_technology + art_culture + history + maths + reasoning+ + ethics + geography + literature + economics
            
            percentage = (total_marks / 1000) * 100
            return Response({'percentage':percentage})
        return Response(serializer.errors)
            
             
            

