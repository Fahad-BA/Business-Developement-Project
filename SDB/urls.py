from logistic import views
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),

    #General Pages
    path('', views.home, name='home'),
    path('about', views.about, name='about'),
    path('story', views.story, name='story'),
    path('support', views.support, name='support'),
    path('support_success', views.support_success, name='support_success'),
    

    #User Pages
    path('signup', views.signupuser, name='signup'),
    path('login', views.loginuser, name='login'),
    path('logout', views.logoutuser, name="logout"),
    path('tracking', views.tracking, name='tracking'),
    path('shipments', views.shipments, name='shipments'),
    path('profile', views.profile, name='profile'),
    path('orders', views.orders, name='orders'),
    path('address', views.address, name='address'),
    path('order_success', views.order_success, name='success'),
    path('Packages', views.Packs, name='Packs'),

]
