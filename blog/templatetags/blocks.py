from django import template
from taggit.models import *
from blog.models import Post

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
