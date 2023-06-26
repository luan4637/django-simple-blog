from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.IndexView.as_view(), name='homepage'),
    path('<slug:post_slug>/', views.DetailsView.as_view(), name='post_details'),
    path('category/<slug:category_slug>/', views.CategoryView.as_view(), name='category_posts'),
    # path('comment/<slug:post_slug>/', views.comment, name='comment'),

    # path('category/<slug:category_slug>/', views.index, name='category_posts'),
    # path('category/<slug:category_slug>/', views.IndexView.as_view(), name='products_by_category'),
    # path('<slug:product_slug>/', views.ProductDetailsView.as_view(), name='product_details'),
]