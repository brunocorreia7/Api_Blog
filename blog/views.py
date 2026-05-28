from rest_framework import generics, viewsets, permissions
from django.contrib.auth.models import User
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Category, Post, Comment
from .serializers import RegisterSerializer, CategorySerializer, PostSerializer, CommentSerializer
from .permissions import IsAuthorOrReadOnly

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    # Permite leitura global, requer admin para criar/editar
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    
    # Filtros, Busca e Ordenação
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['category', 'published'] # Ex: /api/posts/?category=1
    search_fields = ['title']                    # Ex: /api/posts/?search=Django
    ordering_fields = ['created_at']             # Ex: /api/posts/?ordering=-created_at

    def perform_create(self, serializer):
        # Associa automaticamente o autor logado à postagem
        serializer.save(author=self.request.user)

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)