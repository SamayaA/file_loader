from django.db import models

import uuid

class File(models.Model):
    '''
    File table
    id
    file - will upload to media/files
    processed - boolean type
    '''
    id =  id = models.BigAutoField(primary_key=True, editable=False)
    file = models.FileField(verbose_name="File", upload_to="files")
    uploaded_at = models.DateTimeField(verbose_name="Uploaded at", auto_now_add=True)
    processed = models.BooleanField(default=False)
