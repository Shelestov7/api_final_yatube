# TODO:  Напишите свой вариант
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from .permissions import IsOwnerOrReadOnly
from api.serializers import PostSerializer, CommentSerializer, GroupSerializer, FollowSerializer
from rest_framework import viewsets
from .models import Post, Comment, Group, Follow


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsOwnerOrReadOnly, ]
    filter_backends = [DjangoFilterBackend,]
    filterset_fields = ['group',]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get("post_id"))
        serializer.save(author=self.request.user, post=post)

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get("post_id"))
        return Comment.objects.filter(post=post)


class GroupViewSet(viewsets.ModelViewSet):
    serializer_class = GroupSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Group.objects.all()


class FollowViewSet(viewsets.ModelViewSet):
    serializer_class = FollowSerializer
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Follow.objects.all()
    filter_backends = (SearchFilter,)
    search_fields = ('=user__username', '=following__username')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
