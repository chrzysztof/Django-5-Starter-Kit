from django.urls import include, path
from django.conf import settings
from .views import categories, items_listing
from django.conf.urls.static import static

app_name='items'

urlpatterns = [

     path('categories/', categories, name='categories'),  
     path('items_listing/', items_listing, name='items_listing'),


]