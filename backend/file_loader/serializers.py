from django.core.files import File as File_django
from django.core.files.storage import FileSystemStorage
from pathlib import Path
from rest_framework import serializers

from .models import File
# from .tasks import upload_file

class FileSerializer(serializers.ModelSerializer):
    '''
    Serializer for File model
    id, file, uploaed_at, processed
    '''
 
    class Meta:
        model = File
        fields = ["id", "file", "uploaded_at", "processed"]
        read_only_fields = ("processed",)