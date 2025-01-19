from django.urls import path
from . import views

app_name = 'product'

urlpatterns = [
    path('detail<int:pk>', views.ProductDetailView.as_view(), name="product_detail"),
    path('most_sell_detail<int:pk>', views.MostProductDetailView.as_view(), name="most_product_detail"),
    path('all_products', views.AllProduct.as_view(), name="all_products"),
    path('empty', views.CartEmptyView.as_view(), name="empty"),
    path('detail', views.CartDetailView.as_view(), name="cart_detail"),
    path('add/<int:pk>', views.CartAddView.as_view(), name="cart_add"),
    path('delete/<str:id>', views.CartDeleteView.as_view(), name="cart_delete"),
    path('update/<int:id>/<str:action>/<str:product_type>/', views.CartUpdateQuantityView.as_view(),
         name='update_quantity'),
    path('cart/add/mostsellproduct/<int:pk>/', views.CartAddMostSellProductView.as_view(),
         name='cart_add_mostsellproduct'),
    path('order/detail<int:pk>', views.OrderDetailView.as_view(), name="order_detail"),
    path('apply/', views.OrderCreationView.as_view(), name="order_create"),
    path('product/<int:product_id>/add-comment/', views.add_comment, name='add_comment'),
    path('product/<int:product_id>/', views.comments_view, name='comments_view'),
    path('mostsellproduct/<int:product_id>/comment/', views.add_mostsellproduct_comment, name='add_mostsellproduct_comment'),
    path('order/<int:pk>', views.ApplyDiscountView.as_view(), name="discount_code"),
]
