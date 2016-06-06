from django.shortcuts import render, render_to_response, RequestContext
# from django.views import ListView
#http://django-braces.readthedocs.io/en/latest/other.html#orderablelistmixin
from .forms import ProductForm, ManufacturerForm
from .models import Product, Manufacturer


# Create your views here.
def index(request):
    success_message = False
    if request.user.is_authenticated():
        title = 'Welcome'
        myUser = request.user
        manufacturer_list = Manufacturer.objects.order_by('mfg_name')
        product_list = Product.objects.order_by('item_name')
        product_form = ProductForm(request.POST or None)
        if product_form.is_valid():
            new_product = product_form.save(commit=False)
            new_product.save()
            success_message = "Data Saved!"

    else:
        title = 'Hello New User!'
        myUser = ''
        manufacturer_list = None
        product_list = None
        product_form = None

    context = {'title': title,
               'myUser': myUser,
               'product_form': product_form,
               'success_message': success_message,
               'manufacturer_list': manufacturer_list,
               'product_list': product_list

               }

    return render(request, 'inventory.html', context)