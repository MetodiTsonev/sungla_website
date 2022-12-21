from django.urls import path, include

from demo_project.accounts.views import SignInView, SignUpView, SignOutView, ProfileDetailsView, ProfileEditView, \
    ProfileDeleteView

urlpatterns = (
    path('login/', SignInView.as_view(), name='login user'),
    path('register/', SignUpView.as_view(), name='register user'),
    path('logout/', SignOutView.as_view(), name='logout user'),
    path('profile/<int:pk>/', include([
        path('', ProfileDetailsView.as_view(), name='details profile'),
        path('edit/', ProfileEditView.as_view(), name='edit profile'),
        path('delete/', ProfileDeleteView.as_view(), name='delete profile'),
    ])),
)