
from django.contrib import admin
from django.urls import path,include
from medicalshop import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.signup_page,name='signup'),
    path('login/', views.login_page, name='login'),
    path('home',views.home_page,name='home'),
    path('create/',views.product_create,name='create'),
    path('retrieved',views.retrieve_items,name='retrieve'),
    path('update/<int:id>/', views.product_update, name='updateproduct'),
    path('logout', views.logout_view, name='logout'),

    path('delete/<int:id>',views.product_delete,name='deleteproduct'),
     path('search/', views.search_medicine, name='search_medicine'),
     path('pharmaapi/', include('pharmaapi.urls')),
    
    ]