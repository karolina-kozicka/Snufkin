from django.contrib.auth import views


class HomeView(views.TemplateView):
    template_name = "home.html"


# Create your views here.
