from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def categories(request):
    return render(request, 'items/categories.html')

@login_required
def items_listing(request):
    return render(request, 'items/items_listing.html')