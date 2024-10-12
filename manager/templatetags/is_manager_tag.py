from django import template

register = template.Library()


@register.filter(name='is_manager_tag')
def is_manager_tag(user, group_name='manager'):
    return user.groups.filter(name=group_name).exists() or user.is_staff
