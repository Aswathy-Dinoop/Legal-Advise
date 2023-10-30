from django.urls import path
from Legal_App.client_views import index,appointment,viewlawyer,upload,feedback


urlpatterns = [
    path('', index.as_view(),name='index'),
    path('appointment',appointment.as_view(),name='index'),
    path('viewlawyer',viewlawyer.as_view()),
    path('upload',upload.as_view()),
    path('feedback',feedback.as_view())

]

def urls():
    return urlpatterns, 'client','client'