from django.shortcuts import render, render_to_response, RequestContext
from . forms import ProductForm, ManufacturerForm
from . models import Product

# Create your views here.
def index(request):
    success_message = False
    if request.user.is_authenticated():
        title = 'Welcome'
        myUser = request.user
        manufacturer_form = ManufacturerForm(request.POST or None)
        if manufacturer_form.is_valid():
            new_manufacturer = manufacturer_form.save(commit=False)
            new_manufacturer.save()
            success_message = "Data Saved!"
    else:
        title = 'Hello New User!'
        myUser = ''
        product_form = None


    context = {'manufacturer_form': manufacturer_form,
            'success_message': success_message,
               }

    return render(request, 'inventory.html', context)