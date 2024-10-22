from django.template import Library
from apps.core.models import SiteSettings

register =  Library()

@register.inclusion_tag('partials/nav.html')
def nav_view(request):
    branding = SiteSettings.objects.first()
    if branding:
        color = branding.color
        logo = branding.logo
    else:
        color = None
        logo = None

    context = {
        'request':request,
        'color':color,
        'logo':logo
    }
    return context