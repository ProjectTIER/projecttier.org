from wagtail.wagtailcore.blocks import (
    StructBlock,
    TextBlock,
    StreamBlock,
    RichTextBlock
)


class SectionBlock(StructBlock):
    headline = TextBlock()
    subheadline = TextBlock()
    body = StreamBlock([
        ('text', RichTextBlock())
    ])
