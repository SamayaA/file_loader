import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from file_loader.models import File


@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def file_factory():
    def factory(*args, **kwargs):
        return baker.make(File, *args, **kwargs)
    return factory
