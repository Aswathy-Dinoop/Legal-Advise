from django.shortcuts import redirect, render
from django.views.generic import TemplateView,View
from django.core.files.storage import FileSystemStorage
from Legal_App.models import Client_Registration,Appointment,Record
from django.contrib.auth.models import User

class index(TemplateView):
    template_name='lawyer/index.html'

class about(TemplateView):
    template_name='about.html'

class contact(TemplateView):
    template_name='contact.html'

class viewclient(TemplateView):
    template_name='lawyer/view_client.html'

    def get_context_data(self, **kwargs):


        cli = Client_Registration.objects.all()
        context = {
            'client': cli
        }
        return context

class searchclient(TemplateView):
    template_name='lawyer/search_client.html'

    def get_context_data(self, **kwargs):

        cli = Client_Registration.objects.all()
        context = {
            'client': cli
        }
        return context

    def post(self, request, *args, **kwargs):


        search = self.request.POST['search']
        client = Client_Registration.objects.filter(name__icontains=search)

        return render(request,'lawyer/search_client.html',{'client':client})

class viewappointment(TemplateView):
    template_name='lawyer/view_appointment.html'

    def get_context_data(self, **kwargs):

        appoi = Appointment.objects.all()
        context = {
            'appointment':appoi
        }
        return context


class decline(View):
    
    def dispatch(self,request,*args,**kwargs):

        id = request.GET['id']
        Appointment.objects.get(id=id).delete()
        return redirect(request.META['HTTP_REFERER'],{'message':"Removed"})

# class accept(View):

#     def dispatch(self,request,*args,**kwargs):
#         id=self.request.GET['id']

#         co=Complaint.objects.get(pk=id)
        
#         co.status='Complaint Proceeded'
#         co.save()

class viewrecords(TemplateView):
    template_name='lawyer/view_records.html'

    def get_context_data(self, **kwargs):

        rec = Record.objects.all()
        context = {
            'record': rec
        }
        return context