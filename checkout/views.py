from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm

# Create your views here.
def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There is nothing in your bag at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51Q4QbDBopDiZJQSS5ZiWD72Tmt2ZOjDC4CucdF87A8vmt6JXX2c92FhuFzKPgs051h4sQDp3yDVmwSyNmti3nY6F00WFVx1WaZ',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
