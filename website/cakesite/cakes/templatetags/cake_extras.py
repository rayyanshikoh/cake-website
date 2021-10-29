from django import template
register = template.Library()

def is_odd_maths(val):
    val1 = val/2
    val = val1 - val
    return val

@register.simple_tag
def is_odd(value):
    value = int(value)
    if (value % 2) == 0:
        odd = False
    else:
        odd = True
    return odd