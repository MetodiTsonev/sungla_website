from django.urls import path

from demo_project.glasses.views import item_list, catalog, ItemDetailsView

urlpatterns = (
    path('shop/', item_list, name='shop items'),
    path('product/<slug>', ItemDetailsView.as_view(), name='product'),
    path('catalog/', catalog, name='catalog'),
)
