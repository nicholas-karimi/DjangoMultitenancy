from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.core.management import call_command
from django.conf import settings

from django_tenants.utils import schema_context
from django.contrib.auth import login
from apps.tenants.models import Tenant, Domain, TenantMember
from apps.users.forms import TenantForm

# Create your views here.


def dashboard_view(request):
    tenants = Tenant.objects.all()
    tenant_form = TenantForm()

    if request.method == 'POST':
        tenant_form = TenantForm(request.POST)
        if tenant_form.is_valid():
            tenant = tenant_form.save()
            # migrate schema
            # call_command('migrate_schemas', schema_name=tenant_form.cleaned_data['schema_name'])
            call_command('migrate_schemas', schema_name=tenant.schema_name)

            # create domain
            domain = Domain.objects.create(
                tenant=tenant,
                domain=f"{tenant_form.cleaned_data['schema_name']}.{settings.BASE_URL}",
                is_primary=True
            )
            # login user to tenant
            with schema_context(tenant.schema_name):
                request.user.backend = 'django.contrib.auth.backends.ModelBackend'
                # login(request, request.user) TODO

            # flash message
            messages.add_message(
                request,
                messages.SUCCESS,
                "Tenant created successfully"
            )
            # send email

            return redirect(f"http://{domain.domain}{settings.PORT}") #redirct THE NEW TENANT
        else:
            messages.add_message(
                request,
                messages.ERROR,
                "Tenant creation failed"
            )
    # check if user is a member of a tenant
    try:
        tenant_member = TenantMember.objects.get(user=request.user, tenant=request.tenant)
    except:
        tenant_member = None 

    # get list of tenants for the user
    if request.user.is_authenticated:
        user_tenants = TenantMember.objects.filter(user=request.user)
    else:
        user_tenants = []
    base_domain = f"{settings.BASE_URL}{settings.PORT}"
    if not hasattr(request, 'tenant'):
        template_name='core/dashboard.html'
    else:
        template_name='core/tenant_dashboard.html'

    context = {
        'tenants': tenants,
        'tenant_form': tenant_form,
        'tenant_member': tenant_member,
        'user_tenants':user_tenants,
        'base_domain':base_domain,
    }
    return render(request, template_name, context)
