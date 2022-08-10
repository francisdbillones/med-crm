from django import template
from leads.models import Category

register = template.Library()


@register.filter(name="get_category_color")
def get_category_color(category: Category):
    colors = {"Converted": "green", "Unconverted": "red"}

    return colors[category.name]
