from django import template

register = template.Library()

from search.views import search_pokemon

@register.filter
def foo(value):
    return value.lower()

@register.filter
def rangex(value):
    return range(0,3)

@register.filter
def cut(value, arg):
    """Removes all values of arg from the given string"""
    return value.replace(arg, '')

@register.filter
def is_in(var, args):
    if args is None:
        return False
    arg_list = [arg.strip() for arg in args.split(',')]
    return var in arg_list


@register.assignment_tag
def define(val=None):
  return val


@register.simple_tag
def get_pokemons(return_type):
	#return return_type
    return search_pokemon('*',return_type)