from django.shortcuts import render


# Create your views here.
def home(r):
    return render(r, 'home/home.html')


def about(r):
    return render(r, 'home/about.html')