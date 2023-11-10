from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from digestapi.views.users import UserViewSet
from digestapi.views.books import BookViewSet
from digestapi.views.categories import CategoryViewSet

router = DefaultRouter(trailing_slash=False)

router = DefaultRouter(trailing_slash=False)
router.register(r'books', BookViewSet, 'book')
router.register(r'categories', CategoryViewSet, 'category')

urlpatterns = [
    path('', include(router.urls)),
    path('login', UserViewSet.as_view({'post': 'user_login'}), name='login'),
    path('register', UserViewSet.as_view({'post': 'register_account'}), name='register'),
]