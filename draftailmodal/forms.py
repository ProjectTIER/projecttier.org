from django import forms
from wagtail.admin.rich_text import get_rich_text_editor_widget


class TipForm(forms.Form):
    """
    Chooser form that appears in Draftail on the admin screen.
    """
    tip_content = forms.CharField(widget=get_rich_text_editor_widget(
        # features=['h2', 'h3', 'bold', 'italic', 'ol', 'ul', 'link', 'image', 'embed']
        features=[]
    ))
