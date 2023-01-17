from rest_framework.serializers import ModelSerializer, HyperlinkedModelSerializer, StringRelatedField
from .models import Author, Biographies, Book


class AuthorModelSerializer(ModelSerializer):

    class Meta:
        model = Author
        fields = '__all__'
        # fields = ('first_name', 'last_name')  # если нужно перечислить поля
        # exclude = ('first_name')  # если нужно исключить поле


class BookModelSerializer(ModelSerializer):
    # authors = StringRelatedField(many=True)

    class Meta:
        model = Book
        fields = '__all__'


class BiographiesHyperlinkedModelSerializer(HyperlinkedModelSerializer):

    class Meta:
        model = Biographies
        fields = '__all__'
