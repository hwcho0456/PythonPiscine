from django import template

register = template.Library()

@register.filter
def reverse(value):
    return "{:02X}".format(255 - int(value, 16))