from django.shortcuts import render, render_to_response, get_object_or_404 # render genera archivos html usando una plantilla y datos
from .models import post
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.detail import DetailView

# Create your views here.

def index(request):
    """
    Función vista para la página inicio del sitio.
    """
    
	
    # Renderiza la plantilla HTML index.html con los datos en la variable contexto
    return render(
        request,
        'index.html',
    )
	
	
def post_list(request): #Creamos una función (def)
    posts = post.objects.values();
    numero = post.objects.count();
    return render(request, 'blog/post_list.html', {'posts': posts, 'numero':numero})
	
def post_texto(request, pk): #Creamos una función (def)
    posts = get_object_or_404(post, pk=pk);
    return render(request, 'blog/post_texto.html', {'post': posts})
	
	
def info(request): #Creamos una función (def)
    return render_to_response('blog/info.html');
	
def contacto(request): #Creamos una función (def)
    return render_to_response('blog/contacto.html');
	
class PostListView(generic.ListView):
    model = post

class PostTextoView (DetailView):
    model = post
    template_name='blog/post_texto_view.html'
    slug_url_kwarg='the_slug'
    slug_field='slug'
	
post_texto_view=PostTextoView.as_view()