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
    path("admindashboard/", views.admindashboard, name="admindashboard"),
    path("delete/<int:id>/", views.delete, name="delete"),
    path("edit/<int:id>/", views.edit, name="edit"),
    path("search", views.search, name="search"),
    path("searchproducts", views.search_products, name="search"),
    path("products/create/", views.create_products, name="create_products"),
    path("products/update/<int:id>/", views.update_products, name="update_products"),
    path("products/delete/<int:id>/", views.delete_products, name="delete_products"),
]
