from django.urls import path
from . import views
app_name='store'
urlpatterns=[
    
    path('',views.store,name='store_home'),
    path('<slug:category_slug>/',views.store,name='products_by_category'),
    path('<slug:category_slug>/<slug:product_slug>/',views.products_details,name='products_details'),

]