from django.urls import path
from .views import home, redir, short_url_form


urlpatterns = [
    path('home/', home, name='home'),
    path('redir/<str:redirect_url>', redir, name='redir'),
    path('short_url_form', short_url_form, name='short_url_form'),
]
