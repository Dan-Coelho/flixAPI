from rest_framework import serializers
from django.db.models import Avg
from .models import Movie
from genres.serializers import GenreSerializer
from actors.serializers import ActorSerializer
from genres.models import Genre
from actors.models import Actor


class MovieModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = '__all__'

    def validateRelease_date(self, value):
        if value.year < 1900:
            raise serializers.ValidationError("A data de lançamento não pode ser anterior a 1900.")
        return value

    def validate_resume(self, value):
        if len(value) > 500:
            raise serializers.ValidationError("O resumo não pode ter mais de 500 caracteres.")
        return value


class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    release_date = serializers.DateField()
    genre_id = serializers.PrimaryKeyRelatedField(
        queryset =Genre.objects.all(),
    )
    actors_ids = serializers.PrimaryKeyRelatedField(
        queryset =Actor.objects.all(),
        many=True,
    )
    resume = serializers.CharField()


class MovieListDetailSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)
    genre = GenreSerializer()
    actors = ActorSerializer(many=True)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'genre', 'actors', 'release_date', 'rate', 'resume']

    def get_rate(self, obj):
        rate = obj.reviews.aggregate(Avg('stars'))['stars__avg']
        if rate:
            return round(rate, 1)
        return None
