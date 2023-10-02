from django.test import RequestFactory
from django.contrib.auth.models import User
from django.core.files import File as File_django
from mock import MagicMock
import pytest
from model_bakery import baker

from file_loader.models import File

@pytest.mark.django_db
def test_get_files(client, file_factory):
    #Arrange
    count = File.objects.count()
    quantity = 2
    file = file_factory(_quantity=quantity)

    #Act
    responce = client.get("/api/v1/files/")
    data = responce.json()

    #Assert
    assert responce.status_code == 200
    assert File.objects.count() == count + quantity

    
