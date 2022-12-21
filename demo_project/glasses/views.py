from django.shortcuts import render
from django.views.generic import DetailView
from demo_project.glasses.models import Item


def item_list(request):
    context = {
        'items': Item.objects.all(),
    }
    return render(request, 'shop.html', context)


def catalog(request):
    return render(request, 'glasses.html')


class ItemDetailsView(DetailView):
    model = Item
    template_name = 'product.html'


