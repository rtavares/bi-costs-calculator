from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Sum
from django.shortcuts import render
from django.views.generic import ListView, View

from .models import Product


class ProductsListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "products/products_list.html"
    context_object_name = "products"


class BackOfficeView(LoginRequiredMixin, View):
    def get(self, request):
        template_name = "products/back_office.html"
        return render(request, template_name=template_name)


class CalculatePriceView(LoginRequiredMixin, View):
    template_name = "products/calculated_prices.html"

    def post(self, request):
        products_to_price = [int(p) for p in request.POST["products_list"].split(",")]

        products = Product.objects.filter(pk__in=products_to_price)
        products_total = products.aggregate(Sum("price"))

        context = {
            "key": "Value",
            "products": products,
            "products_total": products_total["price__sum"],
        }
        return render(request, template_name=self.template_name, context=context)


def list_calculated_prices(request):
    # import pdb; pdb.set_trace()
    template_name = "products/calculated_prices.html"
    context = {"key": "Value"}
    # return HttpResponseRedirect('/')
    return render(request, template_name=template_name, context=context)
