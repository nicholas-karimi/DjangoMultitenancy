from django.forms import ModelForm
from django import forms 

from django.core.exceptions import ValidationError

import re

from apps.users.models import User
from apps.tenants.models import Tenant


class TenantForm(ModelForm):
    class Meta:
        model = Tenant
        fields = ['name', 'schema_name']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add Tenant Name'}),
            'schema_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Add Subdomain'}),
        }

        def clean_schema_name(self):
            schema_name = self.cleaned_data['schema_name'].lower()

            if not re.match(r'^[a-z0-9_]+(?:\.[a-z0-9_]+)*$', schema_name):
                raise ValidationError('Subdomain name must contain only lowercase letters, numbers, and underscores.')

            if Tenant.objects.filter(schema_name=schema_name).exists():
                raise ValidationError('Subdomain name already exists.')

            return schema_name