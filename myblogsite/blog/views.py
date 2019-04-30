from django.shortcuts import render, get_object_or_404 # render genera archivos html usando una plantilla y datos
from .models import post
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin

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
	
class PostListView(generic.ListView):
    model = post
