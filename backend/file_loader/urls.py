from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from file_loader.views import FileViewSet

upload = FileViewSet.as_view({
    'post': 'create',
    'put': 'update',
    'patch': 'partial_update'
})
files = FileViewSet.as_view({
    'get': 'list'
})

urlpatterns = format_suffix_patterns([
    path('api/v1/upload/', upload, name='upload'),
    path('api/v1/files/', files, name='files')
])