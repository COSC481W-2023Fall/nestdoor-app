from django.template import Library, Node
from django.db.models import get_model
from django.template.exceptions import TemplateSyntaxError
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
     
register = Library()
     
class LatestContentNode(Node):
    def __init__(self, id):
        self.id = id    
        
    def render(self, context):
        try:
            user = User.objects.get(id = self.id)
            return "<a href=\"/User/" + str(self.id) + "\">" + user.username + "</a>"
        except ObjectDoesNotExist:
            return "Bad user."
 
def userlink(parser, token):
    bits = token.contents.split()
    if len(bits) != 2:
        raise TemplateSyntaxError, "user_link tag takes one argument, a user ID"
    return LatestContentNode(bits[1])
    
userlink = register.tag(userlink)