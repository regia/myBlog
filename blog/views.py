# Create your views here.
from blog.models import Post
from django.shortcuts import render_to_response
from django.template import RequestContext
#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.paginator import EmptyPage, PageNotAnInteger
from utils.mypaginator import MyPaginator


def tagpage(request, tag):
    posts = Post.objects.filter(tags__name=tag)
    return render_to_response("tagpage.html", {'posts': posts, 'tag': tag}, context_instance=RequestContext(request))


def mainpage(request, pages="1"):
    posts_list = Post.objects.all().order_by('-created')
    paginator = MyPaginator(posts_list, 2)

    page = int(pages)
    try:
        posts = paginator.page(page)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    except PageNotAnInteger:
        posts = paginator.page(1)

    return render_to_response('blog.html', {'posts': posts}, context_instance=RequestContext(request))


def post(request, year, month, slug_id):
    post_detail = Post.objects.get(slug=slug_id)
    return render_to_response('post.html', {'post': post_detail}, context_instance=RequestContext(request))