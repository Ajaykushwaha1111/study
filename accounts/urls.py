

from django.urls import path
from . import views as ac_views
urlpatterns = [
    path('login/', ac_views.login_view, name="login"),
    path('signup/', ac_views.signup_view, name="signup"),
    path('', ac_views.dashborad, name="dashboard"),
    path('logout/', ac_views.logout_view, name="logout"),
]
