from django.shortcuts import render, redirect
from .models import UrlShort
from .forms import UrlShortForm
from django.http import HttpResponse, JsonResponse
from random import randint


def home(request):
    if request.method == 'POST':
        answer = request.POST.get('radio')
        if answer == "auto":
            current_object = UrlShort()
            current_object.user_url = request.POST.get('user_url')
            current_object.short_url = randint(1, 999666)

            duplicate_short_url = UrlShort.objects.filter(short_url=current_object.short_url) or None
            if duplicate_short_url:
                return HttpResponse('Такой URL уже есть, вернитесь назад и придумайте другой')

            current_object.save()

            all_urls = UrlShort.objects.all()
            return render(request, 'testform1.html', {'all_urls': all_urls})
        else:
            user_url = request.POST.get('user_url')
            num_visits = request.POST.get('num_visits')
            short_url = ''
            request.session['user_url'] = user_url
            request.session['short_url'] = short_url
            request.session['num_visits'] = num_visits
            return redirect('short_url_form')

    else:
        all_urls = UrlShort.objects.all()
        return render(request, 'testform1.html', {'all_urls': all_urls})


def short_url_form(request):
    if request.method == 'POST':
        short_url = request.POST.get('short_url')

        duplicate_short_url = UrlShort.objects.filter(short_url=short_url) or None
        if duplicate_short_url:
            return HttpResponse('Такой URL уже есть, вернитесь назад и придумайте другой')

        request.session['short_url'] = short_url
        UrlShort.objects.create(user_url=request.session['user_url'], short_url=request.session['short_url'])
        all_urls = UrlShort.objects.all()
        return render(request, 'testform1.html', {'all_urls': all_urls})
    else:
        all_urls = UrlShort.objects.all()
        return render(request, 'short_url_form.html', {'all_urls': all_urls})


def redir(request, redirect_url):

    current_object = UrlShort.objects.get(pk=redirect_url)
    current_object.num_visits += 1
    current_object.save()
    return redirect(current_object.user_url)

