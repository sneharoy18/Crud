from django.urls import path
from BRMapp import views
from django.urls import re_path
urlpatterns=[
            re_path(r'view-books',views.viewBooks),
            re_path(r'edit-book',views.editBook),
            re_path(r'delete-book',views.delBook),
            re_path(r'new-books',views.newBook),
            re_path(r'search-books',views.searchBook),
            re_path(r'add',views.add),
            re_path(r'search',views.search),
            re_path(r'edit',views.edit),
            re_path(r'login',views.userLogin),
            re_path(r'logout',views.userLogout),
]
