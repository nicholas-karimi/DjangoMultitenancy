from django.db import models
from django_tenants.models import TenantMixin, DomainMixin

from apps.users.models import User

# Create your models here.
class Tenant(TenantMixin):
    name = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)
    auto_create_schema = True #create schema when the tenant is created
    auto_drop_schema = True #drop the schema when the tenant is deleted

class Domain(DomainMixin):
    pass

class TenantMember(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name="members")
    user= models.ForeignKey(User, on_delete=models.CASCADE)
    is_admin = models.BooleanField(default=False)

    class Meta:
        unique_together = ('user', 'tenant')

    def __str__(self):
        return f"{self.tenant.name} - {'(admin)' if self.is_admin else ''}"
    