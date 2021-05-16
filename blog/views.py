from rest_framework import generics, permissions

from .models import Post
from .serializers import PostSerializer

# Obtenir tous les posts
class PostList(generics.ListAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.order_by("-date").all()

# Obtenir un seul post
class PostDetail(generics.RetrieveAPIView):
    serializer_class = PostSerializer
    queryset = Post.objects.order_by("-date").all()

# Editer un post
class PostEdit(generics.RetrieveUpdateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PostSerializer
    queryset = Post.objects.order_by("-date").all()

# Créer un post
class PostCreate(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PostSerializer
    queryset = Post.objects.order_by("-date").all()

# Supprimer un post
class PostDelete(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (permissions.IsAuthenticated,)
    serializer_class = PostSerializer
    queryset = Post.objects.order_by("-date").all()