from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('manage/', views.orders_list, name='orders_list'),
    path('', views.dashboard, name='dashboard'),

    path('logout/', views.logout_user),

    path('order/<int:pk>', views.order_detail, name='order_detail'),
    path('order_deliver/<int:pk>', views.order_deliver, name='order_deliver'),
    path('order/create/', views.order_create, name='order_create'),
    path('order/finalize/', views.order_finalize, name='order_finalize'),

    path('pizza/<int:pk>', views.cart_add, name='cart_add'),

    path('cart', views.cart, name='cart'),
    path('cart/clear', views.cart_clear, name='cart_clear'),
    path('cart/remove/<int:pk>', views.cart_remove_item, name='cart_remove_item'),
    path('cart/update/<int:pk>', views.cart_update, name='cart_update')

]