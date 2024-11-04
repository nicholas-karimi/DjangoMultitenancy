from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

# Create your models here.
class Tenant(TenantMixin):
    name = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)
    auto_create_schema = True #create schema when the tenant is created
    auto_drop_schema = True #drop the schema when the tenant is deleted

class Domain(DomainMixin):
    pass