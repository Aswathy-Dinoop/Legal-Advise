from django.shortcuts import redirect, render
from django.views.generic import TemplateView,View
from django.core.files.storage import FileSystemStorage
from Legal_App.models import Feedback,Client_Registration,Lawyer_Registration
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

class index(TemplateView):
    template_name='admin/index.html'

class about(TemplateView):
    template_name='admin/about.html'

class contact(TemplateView):
    template_name='admin/contact.html'

class loginn(TemplateView):
    template_name='admin/login.html'

    def post(self, request, *args, **kwargs):
        email = request.POST['email']
        password = request.POST['pw']

        user = authenticate(username=email, password=password)

        if user is not None:
            login(request, user)
            if user.last_name == '1':
                if user.is_superuser:
                    return redirect('/admin')
                elif UserType.objects.get(user_id=user.id).type == "client":
                    return redirect('/client')
                elif UserType.objects.get(user_id=user.id).type == "lawyer":
                    return redirect('/lawyer')
            else:
                return render(request, 'login.html', {'message': " User Account Not Authenticated"})


        else:
            return render(request, 'index.html', {'message': "Invalid Username or Password"})

class viewfeedback(TemplateView):
    template_name='admin/feedback_view.html'

    def get_context_data(self, **kwargs):

        fb = Feedback.objects.all()
        context = {
            'feedback':fb
        }
        return context

class viewclient(TemplateView):
    template_name='admin/view_client.html'

    def get_context_data(self, **kwargs):


        cli = Client_Registration.objects.all()
        context = {
            'client': cli
        }
        return context

class viewlawyer(TemplateView):
    template_name='admin/view_lawyer.html'

    def get_context_data(self, **kwargs):

        law = Lawyer_Registration.objects.all()
        context = {
            'lawyer': law
        }
        return context

