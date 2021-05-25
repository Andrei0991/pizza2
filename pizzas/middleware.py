from .models import Order
from django.contrib.auth.models import User

class UserOrderMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        
       
        if not request.session.get('order'):
            order = Order()
            order.save()
            request.session['order'] = order.id
            
        response = self.get_response(request)


        # Code to be executed for each request/response after
        # the view is called.

        return response