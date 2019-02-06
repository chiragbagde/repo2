from django import template

register = template.Library()

def cut(value,arg):
    """
     cuts all the arguments from the string.
    """
    return value.replace(arg,"")

register.filter('cut',cut)
