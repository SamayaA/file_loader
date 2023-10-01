from django.db import transaction
from django.http import HttpResponse

from rest_framework import viewsets
from rest_framework.exceptions import APIException
from rest_framework.response import Response

from file_loader.models import File
from file_loader.serializers import FileSerializer
from file_loader.tasks import upload_file

class FileViewSet(viewsets.ModelViewSet):
    serializer_class = FileSerializer
    queryset = File.objects.all()

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.save()
        # change processed to True
        response = upload_file.delay(id = serializer.instance.pk)
        return Response(data=serializer.data,status=201)
    