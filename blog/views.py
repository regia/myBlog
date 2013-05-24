import json
from django.contrib.auth.decorators import permission_required
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_protect
from blog.models import Post
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.core.paginator import EmptyPage, PageNotAnInteger
from utils.mypaginator import MyPaginator
from django.contrib.auth import authenticate, login, logout
from forms import AddPostForm


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


def view_by_date(request, year, month=None):
    if month is None:
        posts_list_by_date = Post.objects.filter(created__year=year).order_by('-created')
    else:
        posts_list_by_date = Post.objects.filter(created__year=year, created__month=month).order_by('-created')
    if len(posts_list_by_date) > 0:
        return render_to_response('blog.html', {'posts': posts_list_by_date}, context_instance=RequestContext(request))
    else:
        return render_to_response('nocontent.html', {'posts': None}, context_instance=RequestContext(request))


@csrf_protect
def log_in(request):
    # if request.method == 'POST':
    #     form = AuthenticationForm(request.POST)
    #     if form.is_valid():
    #         login(request, form.get_user())
    #         return HttpResponseRedirect('/blog/')
    #     else:
    #         form = AuthenticationForm()
    #         render_to_response('blocks/login_form.html', {'form': form}, context_instance=RequestContext(request))
    # else:
    #     form = AuthenticationForm()
    #     render_to_response('blocks/login_form.html', {'form': form}, context_instance=RequestContext(request))
    if request.is_ajax():
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                if 'login_required' in request.META['HTTP_REFERER']:
                    return HttpResponse(json.dumps({'redirect': '/blog/post/add/'}), content_type="application/json")
                else:
                    return HttpResponse(json.dumps({'redirect': '/blog/'}), content_type="application/json")

            else:
                return HttpResponse(json.dumps({'errors': 'The user account is inactive now!'}),
                                    content_type="application/json")

        else:
            return HttpResponse(json.dumps({'errors': 'Invalid login or password!'}), content_type="application/json")


@csrf_protect
def log_out(request):
    logout(request)
    return HttpResponseRedirect('/blog/')


@csrf_protect
@permission_required('blog.add_post', login_url='/blog/login_required/')
def add_post(request):
    if request.method == 'POST':
        form = AddPostForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/blog')
    else:
        form = AddPostForm()

    return render_to_response('add_post.html', {'form': form}, context_instance=RequestContext(request))


@permission_required('blog.change_post')
def change_post(request):
    pass


@permission_required('blog.delete_post')
def delete_post(request):
    pass


def show_message(request):
    message = {'message': ''}
    if "login_required" in request.path:
        message['message'] = "Please sign in first or you don't have enough rights to add post"
        return render_to_response('login_required.html', {'message': message}, context_instance=RequestContext(request))