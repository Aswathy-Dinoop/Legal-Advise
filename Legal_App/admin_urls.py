from django.urls import path
from Legal_App.admin_views import index,loginn,viewfeedback,about,contact,viewlawyer,viewclient


urlpatterns = [
    path('', index.as_view()),
    path('login',loginn.as_view()),
    path('about',about.as_view()),
    path('contact',contact.as_view()),
    path('feedbackview',viewfeedback.as_view()),
    path('viewlawyer',viewlawyer.as_view()),
    path('viewclients', viewclient.as_view()),



]

def urls():
    return urlpatterns, 'admin','admin'