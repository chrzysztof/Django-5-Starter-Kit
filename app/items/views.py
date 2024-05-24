from rest_framework import viewsets
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from .models import Category
from .serializers import CategorySerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

# Create your views here.
@login_required
def categories(request):
    return render(request, 'items/categories.html')

@login_required
def items_listing(request):
    return render(request, 'items/items_listing.html')

@login_required
def get_categories_data(request):

    data = serializers.serialize("json", Category.objects.all(), fields=["id", "name", "description"])
    return JsonResponse(data, safe=False)