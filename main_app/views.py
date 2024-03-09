# views.py
from rest_framework import status,generics
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import Reminder
from .serializers import ReminderSerializer
from django.shortcuts import get_object_or_404

@api_view(['POST'])
def reminder_create_view(request, format=None):
    if request.method == 'POST':
        serializer = ReminderSerializer(data=request.data)

        if serializer.is_valid():
            # Check reminder type and ask for mobile number or email accordingly
            reminder_type = serializer.validated_data.get('reminder_type')
            if reminder_type == 'SMS':
                mobile_number = request.data.get('mobile_number')
                serializer.validated_data['mobile_number'] = mobile_number
            elif reminder_type == 'Email':
                email = request.data.get('email')
                serializer.validated_data['email'] = email

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['PUT', 'PATCH'])
def reminder_update_view(request, pk):
    reminder = get_object_or_404(Reminder, pk=pk)

    if request.method == 'PUT':
        serializer = ReminderSerializer(reminder, data=request.data)
    else:
        return Response({'error': 'Method not allowed'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ReminderListView(generics.ListAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer

class ReminderDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Reminder.objects.all()
    serializer_class = ReminderSerializer