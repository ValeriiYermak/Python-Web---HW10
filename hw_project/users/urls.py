from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("new_author/", views.new_author, name="new_author"),
    path("new_quote/", views.new_quote, name="new_quote"),
    path("success/", views.success_url, name="success_url"),
]
