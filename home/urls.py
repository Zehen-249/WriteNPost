from django.urls import path
from home import views

urlpatterns = [
    path('', views.home,name='home'),
    path("account",views.account,name="account"),
    path("login",views.login_user,name="login"),
    path("registration",views.register_user,name="registration"),
    path("logout",views.logout_user,name="logout"),
    path("post",views.post,name="post"),

]
