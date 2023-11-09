from django.template import Library, Node
from django.template.exceptions import TemplateSyntaxError
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.utils.safestring import mark_safe
     
register = Library()
     
@register.simple_tag
def userlink(user_id):
    try:
        user = User.objects.get(id = user_id)
        return mark_safe("<a class=\"userlink\" href=\"/user/" + str(user_id) + "\">" + user.username.upper() + "</a>")
    except ObjectDoesNotExist:
        return "Bad user."