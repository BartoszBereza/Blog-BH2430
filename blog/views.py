# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from blog.models import Category, News


def index(request):
	news = News.objects.all().order_by('-posted_date')
	return render_to_response('index.html',
   {'blog': news}, 
   context_instance=RequestContext(request))
