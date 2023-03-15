from django.urls import path
from allauth.account.views import LogoutView
from django.contrib.auth.decorators import login_required
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)
from .views import (
    home, app_detail,
    completed_tasks,
    profile,
    update_profile,
    add_app,
    total_points,
    AppListView,
    LogoutView,
)

urlpatterns = [
    # homepage
    path('', login_required(home), name='home'),

    # add app admin-only
    path('add-app/', add_app, name='add_app'),

    # apps URLS
    path('apps/', login_required(AppListView.as_view()), name='apps'),
    path('app/<int:app_id>/', app_detail, name='app_detail'),

    # tasks and points URLS
    path('completed-tasks/', completed_tasks, name='completed_tasks'),
    path('total-points/', total_points, name='total_points'),

    # user profile URLS
    path('profile/', profile, name='profile'),
    path('profile/update/', update_profile, name='update_profile'),


    # all-auth logout URL
    path('accounts/logout/', LogoutView.as_view(), name='logout'),

    # JWT Tokens URLs
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
