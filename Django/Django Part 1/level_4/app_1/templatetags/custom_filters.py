from django import template

register = template.Library()


def visit_count(value):
    return value + 1


register.filter(name='visit_count', filter_func=visit_count)
