from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import View
from django.views.generic.base import TemplateView, TemplateResponseMixin, ContextMixin
from django.utils.decorators import method_decorator
from django.shortcuts import render, render_to_response, RequestContext
from django.views.generic.edit import ModelFormMixin
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
#http://django-braces.readthedocs.io/en/latest/other.html#orderablelistmixin
from .forms import ProductForm, ManufacturerForm
from .models import Product, Manufacturer

# Create Views --
class InventoryCreateView(CreateView):
    model = Product
    template_name = "forms.html"
    fields = ["item_name", "item_manufacturer", "item_stock_status"]

    def form_valid(self, form):
        self.object = form.save(commit=False)
        print(self.object)
        self.object.slug = self.object
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


# Detail Views
class InventoryDetail(DetailView):
    model = Product


class InventoryListView(ListView):
    model = Product

    def get_queryset(self, *args, **kwargs):
        qs =super(InventoryListView, self).get_queryset(*args, **kwargs)
        # print(qs)
        # print(qs.first().id)
        return qs



class LoginRequiredMixin(object):
    # @classmethod
    # def as_view(cls, **kwargs):
    #     view = super(LoginRequiredMixin, cls).as_view(**kwargs)
    #     return login_required(view)

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)


class InventoryTemplateView(TemplateView):

    def get_context_data(self, **kwargs):
        context = super(InventoryTemplateView, self).get_context_data(**kwargs)
        context['title'] = 'Inventory Title'
        context['manufacturer_list'] = Manufacturer.objects.all()
        context['product_list'] = Product.objects.all()
        return context

class MyView(TemplateResponseMixin, ContextMixin, View):

    def get(self, request, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        context['title'] = 'MyView Title'
        context['manufacturer_list'] = Manufacturer.objects.all()
        context['product_list'] = Product.objects.all()
        return self.render_to_response(context)



class ExampleTemplateView(TemplateView):
        template_name = "inventory.html"

        def get_context_data(self, **kwargs):
            context = super(ExampleTemplateView, self).get_context_data(**kwargs)
            context['title'] = 'This is Example Template'
            return context



