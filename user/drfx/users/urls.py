from django.urls import path
from users.views import SignUpView
    # ProfileView, ActivateAccount
    # UserLoginView
from . import models
from . import views

urlpatterns = [

    #not working?
    path('', views.UserListView.as_view()),
    path('signup/', SignUpView.as_view(), name='signup'),
    # path('signin/', UserLoginView.as_view(), name='signin'),
    # path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    # path('activate/<uidb64>/<token>/', ActivateAccount.as_view(), name='activate'),
    # path('users/', ListAPIView.as_view(queryset=models.CustomUser.objects.all(), serializer_class=serializers.UserSerializer), name='user-list')

]