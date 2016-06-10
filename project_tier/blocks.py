from wagtail.wagtailimages.blocks import ImageChooserBlock
from wagtail.wagtaildocs.blocks import DocumentChooserBlock
from wagtail.wagtailcore.blocks import (
    StructBlock,
    TextBlock,
    StreamBlock,
    RichTextBlock,
    ChoiceBlock
)


class AccordionBlock(StructBlock):
    title = TextBlock()
    body = RichTextBlock()

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


class HaverfordStreamBlock(StreamBlock):
    paragraph = RichTextBlock(icon='fa-paragraph')
    h3 = TextBlock(icon='fa-header')
    h4 = TextBlock(icon='fa-header')
    h5 = TextBlock(icon='fa-header')
    image = CaptionedImageBlock()
    download = DocumentChooserBlock(icon='fa-download')
    accordion = AccordionBlock()
    notice = NoticeBlock()


class SectionBlock(StructBlock):
    headline = TextBlock()
    subheadline = TextBlock()
    body = HaverfordStreamBlock()

    class Meta:
        icon = 'emoji-bookmark-tabs'
        template = 'blocks/section.html'
