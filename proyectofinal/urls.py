from django.urls import path, include
from . import views
from .views import UserRegisterView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", views.index, name="index"),
    path('register/', UserRegisterView.as_view(), name="register"),
    path("about", views.about, name="about"),
    path("login", views.login_view, name="login"),
    path("logout", views.logoutUser, name="logout"),
    # path("register", views.register, name="register"),
    path("search", views.search, name="search"),
    path("producto_detalle/<int:id>", views.producto_detalle, name="producto_detalle"),
    # path("search_categorias/<str:cats>", views.categories, name="categories"),
    
]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)