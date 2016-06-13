from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtaildocs.blocks import DocumentChooserBlock
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
        ('title', TextBlock()),
        ('body', RichTextBlock())
    ]))

    class Meta:
        icon = 'emoji-scroll'
        template = 'blocks/accordion.html'


class NoticeBlock(StructBlock):
    message = RichTextBlock()
    indicator = ChoiceBlock(choices=[
        ('', 'Standard'),
        ('success', 'Success'),
        ('alert', 'Alert'),
        ('warning', 'Warning')
    ], required=False)

    class Meta:
        icon = 'fa-exclamation-triangle'
        template = 'blocks/notice.html'


class CaptionedImageBlock(StructBlock):
    image = ImageChooserBlock()
    caption = TextBlock(required=False)

    class Meta:
        icon = 'fa-image'
        template = 'blocks/captioned_image.html'


class ContentStreamBlock(StreamBlock):
    paragraph = RichTextBlock(icon='fa-paragraph')
    heading = TextBlock(icon='fa-header', template='blocks/heading.html')
    smaller_heading = TextBlock(
        icon='fa-header', template='blocks/smaller_heading.html')
    smallest_heading = TextBlock(
        icon='fa-header', template='blocks/smallest_heading.html')
    image = CaptionedImageBlock()
    download = DocumentChooserBlock(icon='fa-download')
    accordion = AccordionBlock()
    notice = NoticeBlock()

    class Meta:
        template = 'blocks/streamfield.html'


class SectionBlock(StructBlock):
    headline = TextBlock()
    subheadline = TextBlock()
    body = ContentStreamBlock()

    class Meta:
        icon = 'emoji-bookmark-tabs'
        template = 'blocks/section.html'


class BodyBlock(StreamBlock):
    section = SectionBlock()

    class Meta:
        template = 'blocks/streamfield.html'
