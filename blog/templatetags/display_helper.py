from django import template
from django.utils.html import format_html

register = template.Library()

@register.simple_tag
def post_categories(categories, url):
    htmlCategories = ''
    for category in categories:
        htmlCategories += '<a href="' + url + '">' + category.title + '</a>'
    return format_html(htmlCategories)