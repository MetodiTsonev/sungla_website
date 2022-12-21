from django.urls import path
from demo_project.my_app.views import index, OrderSummaryView, add_to_cart, remove_from_cart, \
    remove_single_item_from_cart, finish_order

urlpatterns = (
    path('', index, name='index'),
    path('cart/', OrderSummaryView.as_view(), name='shopping cart'),
    path('add-to-cart/<slug>/', add_to_cart, name='add to cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove from cart'),
    path('remove-single-item-from-cart/<slug>/', remove_single_item_from_cart, name='remove single item from cart'),
    path('finish-order/', finish_order, name='finish order'),
)
