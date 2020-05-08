from django.contrib.auth import views


class HomeView(views.TemplateView):
    template_name = "home.html"


class LoginView(views.LoginView):
    template_name = "users/login.html"


class LogoutView(views.LogoutView):
    template_name = "users/logout.html"

