from django import forms
from .models import News_post

class NewsForm(forms.ModelForm):

    class Meta:
        model = News_post
        fields = ('news_title', 'news_description', 'news_snippets', 'news_publisher')
        labels = {
            'news_title': 'News Title (Enter the title please)',
            'news_description': 'News Description (Enter the news description please)',
            'news_snippets': 'News Snippets (Enter the news snippets please)',
            'news_publisher': 'News Publisher (Enter the news publisher please)'
        }

