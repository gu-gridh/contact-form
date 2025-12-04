from django import template
from django.conf import settings

register = template.Library()


@register.inclusion_tag('footer.html')
def render_footer():
    project_info = getattr(settings, 'PROJECT_INFO', {})
    return {
        'links': project_info.get('LINKS', []),
        'partners': project_info.get('PARTNERS', []),
    }


@register.inclusion_tag('navigation.html')
def render_navigation():
    project_info = getattr(settings, 'PAGES_PROJECT_INFO', {})
    return {'nav_urls': project_info.get('NAV_URLS', [])}


@register.simple_tag
def project_name():
    project_info = getattr(settings, 'PROJECT_INFO', {})
    return project_info.get('PROJECT_NAME', 'Default Project')
