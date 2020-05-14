from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse

from .models import Pizza

def index(request, pid):
    try:
        pizza = Pizza.objects.get(id=pid)
        date = {
            'id': pizza.id,
            'title': pizza.title,
            'description': pizza.description,
        }
    except ObjectDoesNotExist:
        date = {
             'status': 'error',
             'message': 'pizza not found',
        }

    return JsonResponse(date)
