from django.http import HttpResponseRedirect


def root(request):
    return HttpResponseRedirect('/blog/')