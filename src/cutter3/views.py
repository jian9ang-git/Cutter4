from django.shortcuts import render, redirect
from .models import UrlShort
from .forms import UrlShortForm
from django.http import HttpResponse, JsonResponse


def home(request):
    if request.method == 'POST':
        form = UrlShortForm(request.POST)
        if form.is_valid():
            form.save()
            all_urls = UrlShort.objects.all()
            return redirect('home')
        return redirect(request, 'testform1.html')
    else:
        all_urls = UrlShort.objects.all()
        return render(request, 'testform1.html', {'all_urls': all_urls})


def redir(request, short_url):

    return redirect()