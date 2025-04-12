from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import authenticate, login
from .models import Users, Books


# Create your views here.
class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        print(request.POST)
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(password)
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
        

class HomeView(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        books = Books.objects.all()
        return render(request, 'home.html', {'books': books})

class AddCart(View):
    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        if 'cart' not in request.session:
            request.session['cart'] = []
        request.session['cart'] += request.POST.getlist('book_ids')
        print(request.session['cart'])
        books = Books.objects.all()
        return render(request, 'home.html', {'books': books})

class ShowCart(View):
    def post(self, request):
        if not request.user.is_authenticated:
            return redirect('login')
        if 'cart' not in request.session:
            return render(request, 'cart.html', {'cart': []})
        return render(request, 'cart.html', {'cart': request.session['cart']})
