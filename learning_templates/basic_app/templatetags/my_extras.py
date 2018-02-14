

from django import template

register = template.Library()

@register.filter(name='cut_cut')
def cut_cut(value,arg):
    """
    This cuts out all values of "arg" from the string!
    """
    print(value)
    return value.replace(arg,'')

#register.filter('cut_cut',cut_cut)
