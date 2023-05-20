from .import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='hom'),
    path('for', views.form, name='for'),
    path('sign', views.signup, name='sign'),
    path('pages', views.page, name='pages'),
    path('abou', views.about, name='abou'),
    path('cont', views.contact, name='cont'),
    path('cour', views.courses, name='cour'),
]
