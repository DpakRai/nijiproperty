from django.forms import ModelForm
from buyproperty.models import Comment  

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('message',)