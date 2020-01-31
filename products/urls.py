from django.urls import include,path
# from .views import ProductDetailView, ProductListView,ApiProduct

from products.views import ApiProduct,ApiProductDitais
urlpatterns = [
    # path("list",ProductListView.as_view(),name="list"),
    # path("detail/<int:pk>/",ProductDetailView.as_view(),name="detail"),
    path('api/product',ApiProduct,name='apiProduct'),
    path('api/product/<int:pk>/',ApiProductDitais,name='apiProduct'),
]
