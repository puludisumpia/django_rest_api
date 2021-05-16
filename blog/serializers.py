from rest_framework import fields
from rest_framework.serializers import ModelSerializer

from .models import Post

# Création de la class PostSerializer 
# Cette opération permet de sélectionner les champs
# A inclure dans la serialisation
class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "title", "author", "content", "image", "date",)