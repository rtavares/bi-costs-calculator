from django.db.models import Sum
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, reverse, resolve_url
from django.views.generic import View, ListView, TemplateView

import json

from .models import Product


class ProductsListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'products/products_list.html'
    context_object_name = 'products'


class BackOfficeView(LoginRequiredMixin, View):
    def get(self, request):
        template_name = 'products/back_office.html'
        return render(request, template_name=template_name)


class CalculatePriceView(LoginRequiredMixin, View):
    template_name = 'products/calculated_prices.html'

    def post(self, request):
        # import pdb; pdb.set_trace()
        products_list = [int(p) for p in request.POST['products_list'].split(',')]
        print(products_list)

        products = Product.objects.filter(pk__in=products_list)
        products_total = products.aggregate(Sum('price'))

        context = {
            'key': 'Value',
            'products': products,
            'products_total': products_total['price__sum'],
        }
        return render(request, template_name=self.template_name, context=context)


def list_calculated_prices(request):
    # import pdb; pdb.set_trace()
    template_name = 'products/calculated_prices.html'
    context = {'key':'Value'}
    # return HttpResponseRedirect('/')
    return render(request, template_name=template_name, context=context)
