from django.shortcuts import render, render_to_response, RequestContext
from . forms import ProductForm
from . models import Product

# Create your views here.
def index(request):
    success_message = False
    if request.user.is_authenticated():
        title = 'Welcome'
        myUser = request.user
        product_form = ProductForm(request.POST or None)
        if product_form.is_valid():
            new_product = product_form.save(commit=False)
            success_message = "Success! Data Saved!"



            # Can do this but you can use the ProductForm.save()
            # item_name = product_form.cleaned_data['item_name']
            # item_manufacturer = product_form.cleaned_data['item_manufacturer']
            # stock_status = product_form.cleaned_data['item_stock_status']
            # new_product = Product.objects.create(item_name=item_name, item_manufacturer=item_manufacturer, stock_status=stock_status)

            # print(product_form.cleaned_data['item_name'])
            # print(product_form.cleaned_data['item_manufacturer'])
            # print(product_form.cleaned_data['item_stock_status'])
        # context = {'title': 'Welcome', 'abc': request.user}
    else:
        title = 'Hello New User!'
        myUser = ''
        product_form = None

    context = {'title': title,
                'myUser': myUser,
               'product_form': product_form,
                   }

    return render(request, 'inventory.html', context)