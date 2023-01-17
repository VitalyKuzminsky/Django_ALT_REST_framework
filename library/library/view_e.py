from rest_framework.decorators import api_view, renderer_classes, action
from rest_framework.generics import CreateAPIView, RetrieveAPIView, DestroyAPIView, UpdateAPIView, ListAPIView, \
    get_object_or_404
from rest_framework.mixins import ListModelMixin, DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet, ModelViewSet, GenericViewSet

from authors.models import Book
from authors.serializers import BookModelSerializer


# Пример 1
class BookAPIView(APIView):  # для кастомного метода, чтобы переопределить get, post используем APIView

    def get(self, request, format=None):
        book = Book.objects.all()
        serializer = BookModelSerializer(book, many=True)

        return Response(serializer.data)

    def post(self, request, format=None):
        pass

# Пример 2 - не заработал ('Request' object has no attribute 'metod')
# реализация на фоне функций
# @api_view(['GET'])  # POST
# # @renderer_classes([JSONRenderer, BrowsableAPIRenderer])
# def get(request):
#     if request.metod == 'GET':
#         book = Book.objects.all()
#         serializer = BookModelSerializer(book, many=True)
#
#         return Response({'test': 1})  # доп пример
#     elif request.metod == 'POST':
#         pass

# Пример 3 Generic views
class BookCreateAPIView(CreateAPIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


class BookListAPIView(ListAPIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


class BookRetrieveAPIView(RetrieveAPIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


class BookDestroyAPIView(DestroyAPIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


class BookUpdateAPIView(UpdateAPIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

# Пример 4
class BookViewSet(ViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    def list(self, request):
        book = Book.objects.all()
        serializer_class = BookModelSerializer(book, many=True)
        return Response(serializer_class.data)

    def retrieve(self, request, pk=None):
        book = get_object_or_404(Book, pk=pk)
        serializer_class = BookModelSerializer(book)
        return Response(serializer_class.data)

    def destroy(self, request, pk=None):
        instance = get_object_or_404(Book, pk=pk)
        instance.delete()
        book = Book.objects.all()
        serializer_class = BookModelSerializer(book, many=True)
        return Response(serializer_class.data)

    @action(detail=True, methods=['get'])
    def only(self, request, pk=None):
        book = Book.objects.all()
        return Response({'book': book.name, 'id': book.id})


# Пример 5
class BookModelViewSet(ModelViewSet):
    # renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

    # def destroy(self, request, *args, **kwargs):
    #     pass
    #
    # @action(detail=True, methods=['get'])
    # def only(self, request, pk=None):
    #     book = Book.objects.all()
    #     return Response({'book': book.name, 'id': book.id})


# Пример 6
class BookCustomViewSet(ListModelMixin, DestroyModelMixin, RetrieveModelMixin, UpdateModelMixin, GenericViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]


# ===================== фильтрация ==========================
# 1 Hardcore!
class BookQuerysetFilterViewSet(ModelViewSet):
    serializer_class = BookModelSerializer
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Book.objects.all()

    def get_queryset(self):
        return Book.objects.filter(name__contains='со')  # содержит


# 2 Получение через параметр
class BookFilterListAPIView(ListAPIView):
    serializer_class = BookModelSerializer

    def get_queryset(self):
        name = self.kwargs['name']
        return Book.objects.filter(name__contains=name)


# 3
class BookFilterModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name', '')
        book = Book.objects.all()
        if name:
            book = book.filter(name__contains=name)
        return book


# 4 DjangoFilter
class BookDjangoFilterViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
    filterset_fields = ['id', 'name']


# Paginator
class BookLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2


class BookLimitOffsetPaginationViewSet(ModelViewSet):
    # renderer_classes = [JSONRenderer]
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer
    pagination_class = BookLimitOffsetPagination
