from time import sleep
from celery import shared_task
from django.http import HttpResponse

from .models import File
from django.core.files import File as File_django
from django.core.files.storage import FileSystemStorage
from pathlib import Path

from .serializers import FileSerializer
@shared_task()
def upload_file(id):
    '''
    asynchronous upload of file
    '''
    print('Uploading image...')
    sleep(10)
    instance = File.objects.get(id=id)
    instance.processed = True
    instance.save()
    print("step 2 complete")
