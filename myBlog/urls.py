from django.conf.urls import patterns, include, url
from myBlog import settings
from  django.conf.urls.static import static

# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'myBlog.views.home', name='home'),
                       # url(r'^myBlog/', include('myBlog.foo.urls')),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^blog/', include('blog.urls')),
                       url(r'^ckeditor/', include('ckeditor.urls')),
                       url(r'^$', 'myBlog.views.root'),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
