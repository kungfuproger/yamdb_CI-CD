from django_filters import CharFilter, FilterSet
from reviews.models import Title


class TitleFilter(FilterSet):
    genre = CharFilter(field_name="genre__slug")
    category = CharFilter(field_name="category__slug")
    name = CharFilter(lookup_expr="icontains")

    class Meta:
        model = Title
        fields = ("genre", "category", "name", "year")
