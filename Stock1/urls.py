from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('',views.home,name="home"),
    path('bonne_de_sortie',views.bonne_de_sortie,name="bonne_de_sortie"),
    path('auth/login/',views.loginView,name="login"),
    path('auth/logout/',views.logoutView,name="logout"),
    path("create/",views.create,name="create")
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

