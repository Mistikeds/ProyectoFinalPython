"""final_coder URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from panel.views import  (SignUpView,GaleriaView,
                          SignInView, SignOutView, ReservaCreateView,
                          PosteosView,PosteoCreateView, PosteoUpdateView, PosteoDeleteView,Miperfil, PosteoDetailView, About,
                           TarifaCreateView, TarifaUpdateView, TarifaDeleteView, TarifaView, Mantenimiento)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', SignOutView.as_view(), name='inicio'),
    path('registrate/', SignUpView.as_view(), name='sign_up'),
    path('inicia-sesion/', SignInView.as_view(), name='sign_in'),
    path('cerrar-sesion/', SignOutView.as_view(), name='sign_out'),
    path('reserva/', ReservaCreateView.as_view(), name='reserva'),
    path('posteo/create', PosteoCreateView.as_view(), name='posteo-create'),
    path('posteo/<pk>/update', PosteoUpdateView.as_view(), name ="posteo-update"),
    path('posteos/', PosteosView.as_view(), name ="posteos"),
    path('posteos/<pk>/delete', PosteoDeleteView.as_view(), name ="posteo-delete"),
    path('', GaleriaView.as_view(), name ="galeria"),
    path('Perfilazo', Miperfil.as_view(), name="perfil"),
    path('posteo-detalle/<pk>/', PosteoDetailView.as_view(), name="detalle_posteo"),
    path('about/', About.as_view(), name="about"),
    path('tarifa/create', TarifaCreateView.as_view(), name='tarifa-create'),
    path('tarifa/<pk>/update', TarifaUpdateView.as_view(), name ="tarifa-update"),
    path('tarifas/', TarifaView.as_view(), name ="tarifas"),
    path('tarifas/<pk>/delete', TarifaDeleteView.as_view(), name ="tarifa-delete"),
    path('mantenimiento/', Mantenimiento.as_view(), name="mantenimiento")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

