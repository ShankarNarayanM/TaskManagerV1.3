from django.urls import path
from . import views

app_name = 'app'

urlpatterns = [
    path('', views.landing_view, name="landingPage"),
    path('pricing', views.pricing_view, name="pricingPage"),
    path('contact', views.contact_view, name="contactPage"),
    path('register', views.register_view, name="registerPage"),
    path('login', views.login_view, name="loginPage"),
    path('dashboard', views.dashboard_view, name="dashboardPage"),
    path('logout', views.logout_view, name="logoutPage"),

]
