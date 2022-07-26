from django.db.models import Model
from django.template import Library

register = Library()


@register.filter(name="obj_dmp")
def obj_dmp(obj: Model):
    from django.core import serializers
    from pprint import pformat
    from json import loads

    ret = loads(serializers.serialize("json", (obj,))[1:-1])
    print(ret)
    ret = pformat(ret, indent=2, width=20)
    ret = ret.replace("\n", "<br>")
    return ret
