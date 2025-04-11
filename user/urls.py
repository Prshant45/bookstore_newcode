from django.urls import path, include
from .views import LoginView, HomeView, AddCart


urlpatterns = [
    path('', LoginView.as_view(), name='login'),
    path('login', LoginView.as_view(), name='login'),
    path('home', HomeView.as_view(), name='home'),
    path('add_to_cart', AddCart.as_view(), name='add_to_cart'),
]
