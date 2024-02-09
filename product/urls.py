from _ast import Delete

from rest_framework.routers import DefaultRouter

from django.urls import path, include

from .views import (ProductList,
                    CategoryList,
                    ProductDetail,
                    CategoryDetail,
                    ProductCreate,
                    ProductUpdate,
                    ProductDelete,
                    TagViewSet,
                    ReviewCreate,
                    ReviewList)


router = DefaultRouter()

router.register('tags', TagViewSet)


urlpatterns = [
    # Product
    path('products/', ProductList.as_view()),
    path('products/<int:pk>', ProductDetail.as_view()),
    path('products/create/', ProductCreate.as_view()),
    path('products/update/<int:pk>/', ProductUpdate.as_view()),
    path('products/delete/<int:pk>/', ProductDelete.as_view()),

    # Category
    path('categories/', CategoryList.as_view()),
    path('categories/<int:pk>/', CategoryDetail.as_view()),

    # Tag
    path('', include(router.urls)),

    # Reviews
    path('reviews/create/', ReviewCreate.as_view()),
    path('reviews/', ReviewList.as_view())
]
