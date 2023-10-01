from rest_framework import generics
from .models import Doctor, Appointment
from .serializers import DoctorSerializer, AppointmentSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class DoctorListCreateView(generics.ListCreateAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class DoctorDetailView(generics.RetrieveAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer


class AppointmentCreateView(APIView):
    def get(self, request):
        obj = Appointment.objects.all()
        serializer = AppointmentSerializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            doc = serializer.validated_data['doctor']
            patient_count = Appointment.objects.filter(doctor=doc).count()
            if doc.max_patients > patient_count:
                apmt = Appointment.objects.filter(doctor=doc.id, date=serializer.validated_data['date'], time=serializer.validated_data['time']).count()
                if apmt == 0:
                    serializer.save()
                else:
                    return Response({'error': 'This time is already scheduled with another patient.'}, status=status.HTTP_400_BAD_REQUEST)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Maximum patients limit is full.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
