from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtaildocs.blocks import DocumentChooserBlock
from wagtail.wagtailembeds.blocks import EmbedBlock
from wagtail.wagtailcore.blocks import (
    StructBlock,
    TextBlock,
    StreamBlock,
    RichTextBlock,
    ChoiceBlock,
    ListBlock
)


class AccordionBlock(StructBlock):
    panels = ListBlock(StructBlock([
        ('title', TextBlock(help_text='The headline to display when the accordion panel is closed.')),
        ('body', RichTextBlock(help_text='The inner content of this accordion panel. It is initially hidden.'))
    ], label='Panel'))

    class Meta:
        icon = 'emoji-scroll'
        template = 'blocks/accordion.html'
        help_text = 'Accordions are elements that help you organize and navigate multiple documents in a single container. They can be used for switching between items in the container.'


class NoticeBlock(StructBlock):
    message = RichTextBlock(help_text='Write the message text.')
    indicator = ChoiceBlock(choices=[
        ('', 'Standard'),
        ('success', 'Success'),
        ('alert', 'Alert'),
        ('warning', 'Warning')
    ], required=False, help_text='Choose what type of notice this is.')

    class Meta:
        icon = 'fa-exclamation-triangle'
        template = 'blocks/notice.html'
        help_text = "Get the reader's attention using this callout. This is useful for warnings, indications of success, etc."


class CaptionedImageBlock(StructBlock):
    image = ImageChooserBlock()
    caption = TextBlock(required=False)

    class Meta:
        icon = 'fa-image'
        template = 'blocks/captioned_image.html'
        help_text = 'Select an image and add a caption (optional).'


class ContentStreamBlock(StreamBlock):
    paragraph = RichTextBlock(icon='fa-paragraph')
    heading = TextBlock(icon='fa-header', template='blocks/heading.html')
    smaller_heading = TextBlock(
        icon='fa-header', template='blocks/smaller_heading.html')
    smallest_heading = TextBlock(
        icon='fa-header', template='blocks/smallest_heading.html')
    image = CaptionedImageBlock()
    download = DocumentChooserBlock(icon='fa-download', template='blocks/download.html')
    accordion = AccordionBlock()
    notice = NoticeBlock()
    embed = EmbedBlock(icon="media")

    class Meta:
        template = 'blocks/streamfield.html'


class SectionBlock(StructBlock):
    headline = TextBlock(help_text='Write a title for this section.')
    subheadline = TextBlock(required=False, help_text='Write a subheadline for this section (optional).')
    body = ContentStreamBlock(help_text='The section content goes here.')

    class Meta:
        icon = 'emoji-bookmark-tabs'
        template = 'blocks/section.html'
        help_text = 'Sections divide the page into digestible parts.'


class BodyBlock(StreamBlock):
    section = SectionBlock()

    class Meta:
        template = 'blocks/streamfield.html'
        help_text = 'The main page body.'
