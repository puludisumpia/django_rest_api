from django.urls import path

from .import views

urlpatterns = [
    path("", views.PostList.as_view(), name="index"), # Affiche tous les posts
    path("posts/", views.PostList.as_view(), name="post_list"), # Affiche tous les posts
    path("posts/<int:pk>/", views.PostDetail.as_view(), name="post_detail"), # Detail sur un post
    path("posts/edit/<int:pk>/", views.PostEdit.as_view(), name="post_edit"), # Editer un post
    path("posts/create/", views.PostCreate.as_view(), name="post_create"), # Créer un post
    path("posts/delete/<int:pk>/", views.PostDelete.as_view(), name="post_detele"), # Supprimer un post
]
