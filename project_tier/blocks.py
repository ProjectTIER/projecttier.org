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


class NoticeBlock(StructBlock):
    message = RichTextBlock()
    indicator = ChoiceBlock(choices=[
        ('', 'Standard'),
        ('success', 'Success'),
        ('alert', 'Alert'),
        ('warning', 'Warning')
    ], required=False)


class CaptionedImageBlock(StructBlock):
    image = ImageChooserBlock()
    caption = TextBlock(required=False)


class HaverfordStreamBlock(StreamBlock):
    paragraph = RichTextBlock(icon='pilcrow')
    h2 = TextBlock()
    h3 = TextBlock()
    h4 = TextBlock()
    h5 = TextBlock()
    image = CaptionedImageBlock()
    download = DocumentChooserBlock()
    accordion = AccordionBlock()
    notice = NoticeBlock()


class SectionBlock(StructBlock):
    headline = TextBlock()
    subheadline = TextBlock()
    body = HaverfordStreamBlock()
