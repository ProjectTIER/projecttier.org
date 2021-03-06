from django import forms
from wagtail.admin.rich_text import get_rich_text_editor_widget


class TipForm(forms.Form):
    """ModalWorkflow popup form that lets you enter the tip text."""

    color = forms.ChoiceField(choices=(
        ('', 'default'),
        ('red', 'red'),
        ('blue', 'blue'),
        ('green', 'green'),
        ('yellow', 'yellow'),
        ('orange', 'orange'),
        ('purple', 'purple'),
        ('grey', 'grey'),
        ('black', 'black'),
    ), required=False)
    tip_content = forms.CharField()  # main text field
    # pass the entityKey on edit
    entity_key = forms.CharField(required=False, widget=forms.HiddenInput)

    def __init__(self, *args, **kwargs):
        """Configure the form fields."""
        super(TipForm, self).__init__(*args, **kwargs)

        # HACK: Set the widget when the form is initialized because otherwise
        # it doesn't work (for unknown reasons) ??
        self.fields['tip_content'].widget = get_rich_text_editor_widget(
            # Use an editor with limited features to avoid modals within modals
            # and other funny stuff.
            features=[
                'h2', 'h3', 'bold', 'italic', 'ol', 'ul', 'link',
                # 'link', 'image', 'embed'  # FIXME: These don't work
            ]
        )
