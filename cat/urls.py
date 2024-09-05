from django.urls import path
from .views import *

urlpatterns = [
    path('', all_cats, name='index'),
    path('contact/', contact, name='contact'),
    path('breed/<str:category>/', all_cats_by_category, name='cats_by_category'),
    path('color/<str:color>/', all_cats_by_color, name='cats_by_color'),
    path('gender/<str:gender>/', all_cats_by_gender, name='cats_by_gender'),
    path('cat/detail/<int:cat_id>/', cat_detail, name='cat_detail'),
    path('cat/add/', cat_create, name='cat_create'),
    path('cat/update/<int:cat_id>/', cat_update, name='cat_update'),
    path('cat/delete/<int:cat_id>/', cat_delete, name='cat_delete'),
    path('login/', user_login, name='login'),
    path('logout/', user_logout, name='logout'),
    path('register/', user_register, name='register'),
    path('profile/<str:username>/', user_profile, name='profile'),
    path('save-comment/<int:cat_id>/', comment, name='save_comment'),
    path('test', test, name='test'),
]
