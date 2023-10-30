from django.shortcuts import render,redirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from Legal_App.models import UserType,Client_Registration,Lawyer_Registration
from django.contrib.auth import login, authenticate

# Create your views here.

class index(TemplateView):
    template_name='index.html'

class about(TemplateView):
    template_name='about.html'

class contact(TemplateView):
    template_name='contact.html'

class signup(TemplateView):
    template_name='register.html'

    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['number']
        address = request.POST['address']
        district = request.POST['district']
        password = request.POST['Password']

      
        if User.objects.filter(email=email):
            print('pass')
            return render(request, 'register.html' , {'message': "already added the username or email"})
            
        else:
            
            user = User.objects.create_user(username=email, password=password, first_name=name, email=email,
                                            is_staff='0', last_name='1')
            user.save()

            reg = Registration()# call the model
            reg.user = user

            reg.name=name
            reg.email=email
            reg.phone = phone
            reg.address=address
            reg.district=district
            reg.password = password
            
            reg.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "client"
            usertype.save()
            # messages="Registered Successfully"

            return render(request, 'client/index.html', {'message': "successfully added"})



class loginn(TemplateView):
    template_name='login.html'

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

class lawyer_signup(TemplateView):
    template_name='lawyer_reg.html'


    def post(self, request, *args, **kwargs):
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['number']
        barnumber = request.POST['bar_number']
        specialization = request.POST['specialization']
        experience = request.POST['experience']
        password = request.POST['password']

    
        if User.objects.filter(email=email):
            print('pass')
            return render(request, 'lawyer_reg.html' , {'message': "already added the username or email"})
            
        else:
            
            user = User.objects.create_user(username=email, password=password, first_name=name, email=email,
                                            is_staff='0', last_name='1')
            user.save()

            reg = Lawyer_Registration()# call the model
            reg.user = user

            reg.name=name
            reg.email=email
            reg.phone = phone
            reg.barnumber=barnumber
            reg.specialization=specialization
            reg.experience = experience
            
            reg.save()
            usertype = UserType()
            usertype.user = user
            usertype.type = "lawyer"
            usertype.save()
            # messages="Registered Successfully"

            return render(request, 'lawyer/index.html', {'message': "successfully added"})


