from django.db import models
from pygments.lexers import get_all_lexers, get_lexer_by_name
from pygments.styles import get_all_styles
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from django.contrib.auth.models import AbstractUser
import ast

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())


class ListField(models.TextField):
    __metaclass__ = models.SubfieldBase
    description = "Stores a python list"

    def __init__(self, *args, **kwargs):
        super(ListField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value:
            value = []

        if isinstance(value, list):
            return value

        return ast.literal_eval(value)

    def get_prep_value(self, value):
        if value is None:
            return value

        return unicode(value)

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value, None)


class User(AbstractUser):
    def __unicode__(self):
        return self.username


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    display_linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    style = models.CharField(choices=STYLE_CHOICES, default='friendly', max_length=100)
    owner = models.ForeignKey(User, related_name='snippets')
    highlighted = models.TextField()

    class Meta:
        ordering = ('created',)

    def save(self, *args, **kwargs):
        lexer = get_lexer_by_name(self.language)
        display_linenos = self.display_linenos and 'table' or False
        options = self.title and {'title': self.title} or {}
        formatter = HtmlFormatter(style=self.style, linenos=display_linenos, full=True, **options)
        self.highlighted = highlight(self.code, lexer, formatter)
        super(Snippet, self).save(*args, **kwargs)


class Comment(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, related_name='comments')
    snippet = models.ForeignKey(Snippet, related_name='comments')
    body = models.CharField(max_length=2000)
    parent = models.ForeignKey('self', blank=True, null=True)
    edited = models.BooleanField(default=False)
    line_references = ListField(blank=True)

    def score(self):
        score = 0
        for vote in self.votes.all():
            if vote.type:
                score += 1
            else:
                score -= 1
        return score


class Vote(models.Model):
    comment = models.ForeignKey(Comment, related_name='votes')
    voter = models.ForeignKey(User, related_name='votes')
    type = models.BooleanField(default=False) # 1 = upvote, 0 = downvote