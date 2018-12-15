from accounts.models import Profile

from django import template

import random

register = template.Library()


@register.filter
def getattribute(obj, value):
    return getattr(obj, value)


@register.filter
def fieldname(obj, field_name):
    return obj._meta.get_field(field_name).verbose_name