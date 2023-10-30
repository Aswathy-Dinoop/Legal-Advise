from django.shortcuts import redirect, render
from django.views.generic import TemplateView,View
from django.core.files.storage import FileSystemStorage
from Legal_App.models import Lawyer_Registration,Appointment,Feedback,Record,Client_Registration
from django.contrib.auth.models import User

class index(TemplateView):
    template_name='client/index.html'

class about(TemplateView):
    template_name='about.html'

class contact(TemplateView):
    template_name='contact.html'

class appointment(TemplateView):
    template_name='client/appointment.html'

    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        date = request.POST['date']
        time = request.POST['time']
        venue = request.POST['venue']

        reg = Appointment()# call the model
        # reg.user = user

        reg.name=name
        reg.email=email
        reg.phone=phone
        reg.date=date
        reg.time=time
        reg.venue=venue

            
            
        reg.save()
        # usertype = UserType()
        # usertype.user = user
        # usertype.type = "lawyer"
        # usertype.save()
        # messages="Registered Successfully"

        # return render(request, 'client/index.html', {'message': "successfully added"})
        return redirect(request.META['HTTP_REFERER'],'index')

        
class viewlawyer(TemplateView):
    template_name='client/view_lawyer.html'

    def get_context_data(self, **kwargs):

        law = Lawyer_Registration.objects.all()
        context = {
            'lawyer': law
        }
        return context


class upload(TemplateView):
    template_name='client/upload.html'

    def post(self, request, *args, **kwargs):
    
        document = request.FILES['file']
        fil= Record()
        client=Client_Registration.objects.get(client_id=self.request.user.id)
        fil.user_id=client.id

        fil.document=document
        fil.save()
        return render(request, 'client/index.html', {'message': "successfully added"})



class feedback(TemplateView):
    template_name='client/feedbackform.html'

    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        email = request.POST['email']
        feedback = request.POST['feedback']
        

        fb=Feedback()
        fb.name=name
        fb.email=email
        fb.feedback=feedback
        fb.save()
        
        # return render(request, 'client/index.html', {'message': "successfully added"}) 
        return redirect(request.META['HTTP_REFERER'],{'message':"Added"})

