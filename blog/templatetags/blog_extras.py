from django.contrib.auth.models import User
from django import template
from django.utils.html import format_html
from django.utils.safestring import mark_safe
register = template.Library()

@register.filter
def author_details(author, current_user=None):
  if not isinstance(author, User):
    return ''

  if author == current_user:
    return format_html("<strong>me</strong>")

  if author.first_name and author.last_name:
    name = f'{author.first_name} {author.last_name}'
  else:
    name = author.username

  if author.email:
    prefix = format_html('<a href="mailto:{}">', author.email)
    suffix = format_html('</a>')
    return format_html('{}{}{}', prefix, name, suffix) # mark_safe(f"<a href='mailto:{escape(author.email)}'>{escape(name)}</a>")
  else:
    return format_html('{}', name)