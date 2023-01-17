from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from library.view_e import BookAPIView, BookListAPIView, BookCreateAPIView, BookUpdateAPIView, BookDestroyAPIView, \
    BookRetrieveAPIView, BookViewSet, BookModelViewSet, BookCustomViewSet, BookQuerysetFilterViewSet, \
    BookFilterListAPIView, BookFilterModelViewSet, BookDjangoFilterViewSet, BookLimitOffsetPaginationViewSet

router = DefaultRouter()
# router.register('book', BookAPIView)
# Пример 4
# router.register('booook', BookViewSet, basename='book')
# # Пример 5
# router.register('book_model', BookModelViewSet)
# # Пример 6
# router.register('book_custom', BookCustomViewSet)
# # фильтрация
# # 1
# router.register('book_filter_1', BookQuerysetFilterViewSet)
# фильтрация
# 3
# router.register('book_filter_3', BookFilterModelViewSet)
# 4
router.register('book_filter_view', BookDjangoFilterViewSet)
# Pagination
router.register('book_pagination', BookLimitOffsetPaginationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),


    # пример 1
    path('api/book/', BookAPIView.as_view()),
    # пример 2
    # path('api/book_get/', get),

    # Пример 3 Generic views
    path('api/list/', BookListAPIView.as_view()),
    path('api/create/', BookCreateAPIView.as_view()),
    path('api/update/<int:pk>/', BookUpdateAPIView.as_view()),
    path('api/delete/<int:pk>/', BookDestroyAPIView.as_view()),
    path('api/detail/<int:pk>/', BookRetrieveAPIView.as_view()),

    # Пример 4
    path('api/', include(router.urls)),

    # фильтрация
    # 2
    path('api/<str:name>/', BookFilterListAPIView.as_view())
]
