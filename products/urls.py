from django.urls import include,path
from .views import ProductDetailView, ProductListView
urlpatterns = [
    path("list",ProductListView.as_view(),name="list"),
    path("detail/<int:pk>/",ProductDetailView.as_view(),name="detail"),
]
