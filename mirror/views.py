from django.shortcuts import render

from django.views.generic.base import TemplateView
from django.views.generic.dates import MonthArchiveView
from django.views.generic.edit import CreateView
from mirror.models import *
from django.db.models import Q

from django.http import JsonResponse
# Create your views here.

class HomeView(TemplateView):
    template_name='home.html'

class CalenderCreateFeed(CreateView):
    model = CalendarFeed
    fields = '__all__'
    template_name = 'mirror/calendar_create.html'

    def form_valid(self, form):
        form.save()
        response_data={}
        response_data['result']='등록되었습니다.'
        return JsonResponse(response_data)


def CalenderMAV(request, year, month):
    if request.method=='GET':
        feeds=CalendarFeed.objects.filter(start__year=2017).filter(Q(start__month=month) | Q(end__month=month))
        feed_array=[]
        for feed in feeds:
            feed_array.append({'title':feed.title,'start':feed.start,'end':feed.end})
        response_data = {}
        response_data['data']=feed_array
        response_data['year']=year
        return JsonResponse(response_data)
