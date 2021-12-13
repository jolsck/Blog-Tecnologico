from django.shortcuts import render
from .models import Post, Categoria
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator 

# Create your views here.
def home(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(estado = True)
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) | 
            Q(descripcion__icontains = queryset)
        ).distinct() 
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)          
    return render(request, 'index.html',{'posts' : posts})

def detallePost(request, slug):
    post = get_object_or_404(Post, slug = slug)
    return render(request,'post.html',{'detalle_post': post})


def notas(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = 'Notas')
    )
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) | 
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Notas'),
               
        ).distinct()
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)   
    return render(request,'notas.html' ,{'posts' : posts})

def cursos(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = 'Cursos')
    )  
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) | 
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Cursos'), 
        ).distinct()
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page) 
    return render(request,'cursos.html' ,{'posts' : posts})

def foro(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre__iexact = 'Foro')
    )
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) | 
            Q(descripcion__icontains = queryset),
            estado = True,
            categoria = Categoria.objects.get(nombre__iexact = 'Foro'), 
        ).distinct()
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page) 
    return render(request,'foro.html', {'posts' : posts} )