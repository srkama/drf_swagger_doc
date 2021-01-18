from rest_framework import viewsets
from rest_framework.decorators import action, api_view
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from rest_framework import status
from .models import Tasks
from .serialiazers import TaskSerializer, NumbersSerializer

class TaskViewset(viewsets.ModelViewSet):
    queryset = Tasks.objects.all()
    serializer_class = TaskSerializer

    @swagger_auto_schema(
        operation_summary="all completed tasks",
        responses={
            200: TaskSerializer
        }
    )
    @action(detail=False, methods=['GET'], url_path='completed')
    def completed(self, request):
        qs =  Tasks.objects.all()
        serializer = self.serializer_class(qs, many=True).data
        return Response(serializer, status=status.HTTP_200_OK)

    @swagger_auto_schema(
        method='GET',
        operation_summary="subtasks of a particular task",
        responses={
            200: TaskSerializer
        }
    )
    @swagger_auto_schema(
        methods=['POST'],
        operation_summary="add subtasks to a particular task",
        request = TaskSerializer,
        responses={
            200: TaskSerializer
        }
    )       
    @action(detail=True, methods=['GET', 'POST'], url_path='sub_tasks')
    def sub_tasks(self, request, pk=None):
        if request.method == 'GET':
            qs =  Tasks.objects.all()
            serializer = self.serializer_class(qs, many=True).data
            return Response(serializer, status=status.HTTP_200_OK)

        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(
    methods=['POST'],
    operation_summary="Sum of Two numbers",
    request_body = NumbersSerializer,
    responses={
        200: openapi.Schema(
            type=openapi.TYPE_INTEGER,
            title="s"
        )
    }
)
@api_view(['POST'])
def add_two_numbers(request):
    data = request.data
    serializer = NumbersSerializer(data=data)
    if serializer.is_valid():
        s = serializer.data['x'] + serializer.data['y']
        return Response({'sum': s}, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)