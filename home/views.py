from karakcode.decorators.decorators import cache_page_custom
from django.shortcuts import render

from karakcode.decorators.decorators import cache_page_custom
from django.shortcuts import render




@cache_page_custom(60 * 60 * 24 * 30, "home_mob")
def home_mobile(request):
    return render(request, "home/index_mob.html")

@cache_page_custom(60 * 60 * 24 * 30, "home_pc")
def home_pc(request):
    return render(request, "home/index.html")


def home(request):
    if request.user_agent.is_mobile:
        return home_mobile(request)
    else:
        return home_pc(request)