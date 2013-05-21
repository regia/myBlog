from django import template
#from django.http import HttpResponseRedirect
from taggit.models import *
from blog.models import Post
#from django.contrib.auth.forms import AuthenticationForm
#from django.contrib.auth import login

register = template.Library()


@register.inclusion_tag('blocks/tags_list.html')
def tags_list():
    tags = Tag.objects.all()
    return {"tags": tags}


#bad idea but just interesting to do it :)
@register.inclusion_tag('blocks/tags_cloud.html')
def tags_cloud():
    tags = []
    tags_object = Tag.objects.all()
    posts = Post.objects.all().only('pk')
    for tag in tags_object:
        tags.append({'name': tag, 'count': posts.filter(tags__name=tag).count()})
    return {"tags": tags}

@register.inclusion_tag('blocks/latest_posts.html')
def latest_posts():
    posts = Post.objects.all().order_by('-created')[:5]
    return {'posts': posts}

    # @register.inclusion_tag('blocks/login_form.html', takes_context = True)
    # def log_in(context):
    #     request = context['request']
    #     if request.method == 'POST':
    #         form = AuthenticationForm(data=request.POST)
    #         if form.is_valid():
    #             login(request, form.get_user())
    #             return HttpResponseRedirect('/blog/2013/')
    #     else:
    #         form = AuthenticationForm(request)
    #         return {'form': form}