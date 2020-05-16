from rest_framework import generics
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import View, UpdateView
from users.forms import CustomUserCreationForm

    # ProfileForm

from django.contrib import messages
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from django.template.loader import render_to_string
from . import models
from . import serializers
from rest_framework.permissions import IsAdminUser

from rest_framework.generics import CreateAPIView, RetrieveAPIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from users.serializers import UserRegistrationSerializer
from users.serializers import UserLoginSerializer
from rest_framework import status

class UserListView(generics.ListAPIView):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.UserSerializer
    permission_classes = [IsAdminUser]


# Sign Up View
class SignUpView(View):

    form_class = CustomUserCreationForm
    template_name = 'commons/signup.html'

    #new
    serializer_class = UserRegistrationSerializer
    permission_classes = (AllowAny,)
    #

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):

        #new
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        #

        # form = self.form_class(request.POST)
        # if form.is_valid():
        #
        #     user = form.save(commit=False)
        #     user.is_active = False # Deactivate account till it is confirmed
        #     user.save()
        #
        #     current_site = get_current_site(request)
        #     subject = 'Activate Your Account'
        #     message = render_to_string('emails/account_activation_email.html', {
        #         'user': user,
        #         'domain': current_site.domain,
        #         'uid': urlsafe_base64_encode(force_bytes(user.pk)),
        #         'token': account_activation_token.make_token(user),
        #     })
        #     user.email_user(subject, message)
        #
        #     messages.success(request, ('Please Confirm your email to complete registration.'))
        #
        #     return redirect('login')
        #
        # return render(request, self.template_name, {'form': form})

# from django.contrib.auth import login
# from .models import CustomUser
# from django.utils.encoding import force_text
# from django.utils.http import urlsafe_base64_decode
# from users.tokens import account_activation_token
#
# class ActivateAccount(View):
#
#     def get(self, request, uidb64, token, *args, **kwargs):
#         try:
#             uid = force_text(urlsafe_base64_decode(uidb64))
#             user = CustomUser.objects.get(pk=uid)
#         except (TypeError, ValueError, OverflowError, CustomUser.DoesNotExist):
#             user = None
#
#         if user is not None and account_activation_token.check_token(user, token):
#             user.is_active = True
#             user.profile.email_confirmed = True
#             user.save()
#             login(request, user)
#             messages.success(request, ('Your account have been confirmed.'))
#             return redirect('home')
#         else:
#             messages.warning(request, ('The confirmation link was invalid, possibly because it has already been used.'))
#             return redirect('home')



# # Edit Profile View
# class ProfileView(UpdateView):
#     model = models.CustomUser
#     form_class = ProfileForm
#     success_url = reverse_lazy('home')
#     template_name = 'commons/profile.html'



#new
# class UserLoginView(RetrieveAPIView):
#
#
#     permission_classes = (AllowAny,)
#     serializer_class = UserLoginSerializer
#
#     def post(self, request):
#         serializer = self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         response = {
#             'success' : 'True',
#             'status code' : status.HTTP_200_OK,
#             'message': 'User logged in  successfully',
#             'token' : serializer.data['token'],
#             }
#         status_code = status.HTTP_200_OK
#
#         return Response(response, status=status_code)

#