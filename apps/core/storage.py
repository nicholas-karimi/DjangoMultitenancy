'''
    Select the storage backend for static files based on the tenant.
'''

from django.core.files.storage import FileSystemStorage
from django.db import connection
from django_tenants.files.storage import TenantFileSystemStorage
from django.conf import settings

class CustomSchemaStorage:
    def _get_storage_backend(self):
        schema_name = connection.schema_name
        if schema_name == 'public':
            return FileSystemStorage()
        else:
            return TenantFileSystemStorage()
        
    def save(self, name, context, max_length=None):
        storage_backend = self._get_storage_backend()
        return storage_backend.save(name, context, max_length)
    
    def url(self, name):
        storage_backend = self._get_storage_backend()
        return storage_backend.url(name)
    def generate_filename(self, filename):
        storage_backend = self._get_storage_backend()
        return storage_backend.generate_filename(filename)
    
    def delete(self, name):
        storage_backend = self._get_storage_backend()
        return storage_backend.delete(name)