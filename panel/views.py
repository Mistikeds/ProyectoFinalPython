from django.shortcuts import render, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView, TemplateView, ListView, UpdateView, DeleteView, DetailView
from .models import Perfil, Reserva, Posteo, Tarifa
from .forms import SignUpForm, ReservaForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required

class SignInView(LoginView):
    template_name = 'panel/iniciar_sesion.html'

class SignOutView(LogoutView):
    pass

class SignUpView(CreateView):
    model = Perfil
    form_class = SignUpForm
    

    def form_valid(self, form):
        '''
        En esta parte, si el formulario es valido guardamos lo que se obtiene de él y
        usamos authenticate para que el usuario incie sesión luego de haberse registrado y
        lo redirigimos al index
        '''
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('/')


class BienvenidaView(TemplateView):
   template_name = 'panel/home.html'

@method_decorator(login_required, name='dispatch')
class ReservaCreateView(CreateView):
    model = Reserva
    form_class = ReservaForm
    template_name = "panel/reserva_form.html"
    success_url = reverse_lazy('inicio')


class PosteosView(ListView):
    
    queryset = Posteo.objects.all()
    template_name = "panel/posteo_list.html"    
    context_object_name = "posteos"



class GaleriaView(ListView):
    
    queryset = Posteo.objects.all()
    template_name = "panel/galeria.html"
    context_object_name = "posteos"
    

@method_decorator(staff_member_required, name='dispatch')
class PosteoCreateView(CreateView):
    model = Posteo
    fields = ['titulo','descripcion_corta' , 'contenido', 'foto','es_una_promo']
    template_name = "panel/posteo_form.html"
    success_url = reverse_lazy('posteos')

@method_decorator(staff_member_required, name='dispatch')
class PosteoUpdateView(UpdateView):
    model = Posteo
    fields = ['titulo','descripcion_corta' , 'contenido', 'foto','es_una_promo']
    template_name = "panel/posteo_form.html"
    success_url = reverse_lazy('posteos')

@method_decorator(staff_member_required, name='dispatch')
class PosteoDeleteView(DeleteView):
    model = Posteo
    template_name = "panel/posteo_confirm_delete.html"
    success_url = reverse_lazy('posteos')

class Miperfil(TemplateView):
   template_name = 'panel/perfil.html'


class PosteoDetailView(DetailView):
    model = Posteo
    template_name = "panel/posteo_detalle.html"

class About(TemplateView):
    template_name = "panel/about.html"


class TarifaView(ListView):
    
    queryset = Tarifa.objects.all()
    template_name = "panel/tarifa_list.html"    
    context_object_name = "tarifas"

@method_decorator(staff_member_required, name='dispatch')
class TarifaCreateView(CreateView):
    model = Tarifa
    fields = ['periodo','precio' , 'cantidad_maxima_personas']
    template_name = "panel/tarifa_form.html"
    success_url = reverse_lazy('tarifas')

@method_decorator(staff_member_required, name='dispatch')
class TarifaUpdateView(UpdateView):
    model = Tarifa
    fields = ['periodo','precio' , 'cantidad_maxima_personas']
    template_name = "panel/tarifa_form.html"
    success_url = reverse_lazy('tarifas')

@method_decorator(staff_member_required, name='dispatch')
class TarifaDeleteView(DeleteView):
    model = Tarifa
    template_name = "panel/tarifa_confirm_delete.html"
    success_url = reverse_lazy('tarifas')

class Mantenimiento(TemplateView):
   template_name = 'panel/Proximamente.html'