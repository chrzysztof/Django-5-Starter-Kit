from django.urls import include, path
from django.conf import settings
from rest_framework.routers import DefaultRouter
from .views import categories, items_listing, get_categories_data, CategoryViewSet
from django.conf.urls.static import static

app_name='items'

router = DefaultRouter()
router.register('categories', CategoryViewSet)

urlpatterns = [

     path('categories/', categories, name='categories'),  
     path('items_listing/', items_listing, name='items_listing'),

     # Ajax responces
     # path('api/categories/', get_categories_data, name='categories_api'),
      path('api/', include(router.urls)),

]