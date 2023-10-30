from django.urls import path
from Legal_App.lawyer_views import index,viewclient,searchclient,viewappointment,decline,viewrecords


urlpatterns = [
    path('', index.as_view()),
    path('viewclients', viewclient.as_view()),
    path('search',searchclient.as_view()),
    path('viewappointment',viewappointment.as_view()),
    # path('accept',accept.as_view()),
    path('reject',decline.as_view()),
    path('documents',viewrecords.as_view())
    

]

def urls():
    return urlpatterns, 'lawyer','lawyer'