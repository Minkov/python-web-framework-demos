import random
from time import time

from django.core.cache import cache
from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import generic as views
# cache for 15 seconds
from django.views.decorators.cache import cache_page

from common_tools.web.models import Profile

'''
.eJxVjDkOwjAUBe_iGln2d-KFkj5niPwX4wBypCwV4u4oUgpo38y8txrzvtVxX2UZJ1ZXZdXld8NMT2kH4Edu91nT3LZlQn0o-qSrHmaW1-10_w5qXutRIxWfONjCyXVgowf0BgW4GMoQCVNCMQ64j8a5kMmL9YG4ly4FCOrzBfjLOAk:1nUB2c:fDGS61_nASs4piDt21B8bj4eQIOwNmxSHpvi-kRKvuU
'''


# @cache_page(60)
def show_index(request):
    Profile.objects.create(
        name='Doncho Minkov',
        email='doncho@minkov.it',
    )
    profiles = Profile.objects.all()

    if not cache.get('value2'):
        cache.set('value2', random.randint(1, 1024), 30)

    count = request.session.get('count') or 0
    request.session['count'] = count + 1

    paginator = Paginator(profiles, per_page=5)
    current_page = request.GET.get('page', 1)
    context = {
        'value': random.randint(1, 1024),
        'value2': cache.get('value2'),
        'count': request.session.get('count'),
        'profiles': profiles,
        'profiles_page': paginator.get_page(current_page),
    }

    return render(request, 'index.html', context)


class ProfilesListView(views.ListView):
    model = Profile
    template_name = 'profiles-list.html'
    paginate_by = 5

    # def get_paginate_by(self, queryset):
    #     return self.request.GET.get('pages_count', 1)
#
# class ProfilesAndCategoriesView:
#     models =(Profile, Category)
#     template_name = '...'
#     paginate_by = (5, 15)

def show_book_details(request, pk):
    last_viewed = request.session.get('last_viewed_books', [])
    last_viewed.append(pk)


class MeasureTimeMixin(views.TemplateView):
    def dispatch(self, request, *args, **kwargs):
        start_time = time()
        result = super().dispatch(*args, **kwargs)
        end_time = time()
        print(end_time - start_time)
        return result
