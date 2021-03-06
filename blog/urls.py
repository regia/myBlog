#coding: utf-8 
from django.conf.urls import patterns, url, include
from blog.utils.rss import BlogFeed

urlpatterns = patterns('',
                       #url(r'^$', ListView.as_view(queryset=Post.objects.all().order_by('-created'),template_name='blog.html')),
                       url(r'^$', 'blog.views.mainpage'),
                       url(r'page/(\d)/$', 'blog.views.mainpage'),
                       #url(r'^\d{4}\/\d{2}\/(?P<slug>.*)/$', DetailView.as_view(model=Post,template_name='post.html')),
                       url(r'^(?P<year>\d{4})/$', 'blog.views.view_by_date'),
                       url(r'^(?P<year>\d{4})/(?P<month>\d{2})/$', 'blog.views.view_by_date'),
                       url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<slug_id>.*)/$', 'blog.views.post'),
                       url(r'^tag/(?P<tag>.*)/$', 'blog.views.tagpage'),
                       url(r'^comments/', include('django.contrib.comments.urls')),
                       url(r'^feed/', BlogFeed()),
                       url(r'^login/$', 'blog.views.log_in'),
                       url(r'^login_required/$', 'blog.views.show_message'),
                       url(r'^logout/$', 'blog.views.log_out'),
                       url(r'^post/add/$', 'blog.views.add_post'),
                       url(r'^post/delete/(?P<slug_id>.*)/$', 'blog.views.delete_post'),
                       url(r'^registration', 'blog.views.registration'),
                       url(r'^profile/', 'blog.views.profile'),
)
