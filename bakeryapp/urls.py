from django.urls import path

from . import views
urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("logout/", views.logout, name="logout"),
    path("store/", views.store, name="store"),
    path("menu/", views.menu, name="menu"),
    path("contact/", views.contact, name="contact"),
    path("items/", views.items, name="items"),
    path("delete/<int:id>/", views.delete, name="delete"),
    path("edit/<int:id>/", views.edit, name="edit")
    
]
