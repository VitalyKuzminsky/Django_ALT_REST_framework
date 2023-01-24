from rest_framework.permissions import AllowAny, BasePermission
from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ModelViewSet
from .models import Author, Book, Biographies
from .serializers import AuthorModelSerializer, BookModelSerializer, BiographiesHyperlinkedModelSerializer


class AdminOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser


class AuthorModelViewSet(ModelViewSet):
    # renderer_classes = [JSONRenderer]
    # permission_classes = [AllowAny]
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer


class BookModelViewSet(ModelViewSet):
    # permission_classes = [AdminOnly]
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


class BiographiesModelViewSet(ModelViewSet):
    queryset = Biographies.objects.all()
    serializer_class = BiographiesHyperlinkedModelSerializer
