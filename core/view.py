from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render
class HomeView (View):
    def get(self, requets, *args, **kwargs):
        context={}
        return render(requets, 'index.html',context)