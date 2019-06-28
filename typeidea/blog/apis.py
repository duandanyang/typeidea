from rest_framework import viewsets


from .models import Post
from .serializers import PostSerializer, PostDetailSerializer


class PostViewSet(viewsets.ReadOnlyModelViewSet):
    """提供文章接口"""
    serializer_class = PostSerializer
    queryset = Post.objects.filter(status=Post.STATUS_NORMAL)

    def retrieve(self, request, *args, **kwargs):
        self.serializer_class = PostDetailSerializer
        return super().retrieve(request, *args, **kwargs)
