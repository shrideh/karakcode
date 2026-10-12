from karakcode.decorators.decorators import cache_page_custom
from django.shortcuts import render

@cache_page_custom(60 * 60 * 24 * 30, "home")
def home (request):
    return render(request, 'home/index.html')