# Create your views here.
from django.contrib.auth.decorators import permission_required
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


def year_month(request, year="0", month="0"):
    if year != "0" and month == "0":
        posts_list_by_year = Post.objects.filter(created__year=year).order_by('-created')
        if len(posts_list_by_year) > 0:
        #Post.objects.filter(publish_date__year=year,publish_date__month=month).
            return render_to_response('blog.html', {'posts': posts_list_by_year},
                                      context_instance=RequestContext(request))
        else:
            return render_to_response('nocontent.html', {'posts': None}, context_instance=RequestContext(request))
    elif year != "0" and month != "0":
        posts_list_by_year_month = Post.objects.filter(created__year=year, created__month=month).order_by('-created')
        if len(posts_list_by_year_month) > 0:
        #Post.objects.filter(publish_date__year=year,publish_date__month=month).
            return render_to_response('blog.html', {'posts': posts_list_by_year_month},
                                      context_instance=RequestContext(request))
        else:
            return render_to_response('nocontent.html', {'posts': None}, context_instance=RequestContext(request))


@permission_required('blog.add_post')
def add_post(request):
    pass


@permission_required('blog.change_post')
def change_post(request):
    pass


@permission_required('blog.delete_post')
def delete_post(request):
    pass