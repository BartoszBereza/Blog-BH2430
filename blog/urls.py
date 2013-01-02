from django.conf.urls.defaults import patterns, include, url
#from django.views.generic import ListView, DetailView
#from blog.models import admin
#admin.autodiscover()
urlpatterns = patterns('blog.views',
    #url(r'^$', ListView.as_view(
    #                       queryset=Post.objects.all().order_by("-created")[:2],
    #                       template_name="blog.html")),
                         
	#url(r'^admin/', include(admin.site.urls)),
	#url(r'^/?$', 'blog.views.index'),
)