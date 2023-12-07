from django_filters import FilterSet, DateTimeFilter
from django.forms import DateTimeInput
from .models import Post

class PostFilter(FilterSet):
    added_after = DateTimeFilter(
        field_name='date_time',
        lookup_expr='gt',
        widget = DateTimeInput(
            format='%Y-%m-%dT%H:%M',
            attrs={'type': 'datetime-local'},
        ),
    )
    class Meta:
        model = Post
        fields = {
            'heading': ['icontains'],
            'categories': ['exact'],
            # 'date_time': ['gt']
        }