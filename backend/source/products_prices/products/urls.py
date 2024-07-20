from django.urls import path

from .views import BackOfficeView, CalculatePriceView, ProductsListView, list_calculated_prices

app_name = 'products'

urlpatterns = [
    path('', ProductsListView.as_view(template_name='products/products_list.html'), name='home'),
    path('calculate/', CalculatePriceView.as_view(), name='calculate'),
    path('list_calculated', list_calculated_prices, name='list_calculated'),
    path('backend/', BackOfficeView.as_view(), name='backoffice')
]

