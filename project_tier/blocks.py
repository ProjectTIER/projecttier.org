from wagtail.images.blocks import ImageChooserBlock
from wagtail.documents.blocks import DocumentChooserBlock
from wagtail.embeds.blocks import EmbedBlock
from wagtail.core.blocks import (
    StructBlock,
    TextBlock,
    StreamBlock,
    RichTextBlock,
    ChoiceBlock,
    ListBlock,
    PageChooserBlock,
    CharBlock
)
from wagtailfontawesome.blocks import IconBlock


class AccordionBlock(StructBlock):
    panels = ListBlock(StructBlock([
        ('title', TextBlock(help_text='The headline to display when the accordion panel is closed.')),
        ('body', RichTextBlock(help_text='The inner content of this accordion panel. It is initially hidden.'))
    ], label='Panel'))

    class Meta:
        icon = 'emoji-scroll'
        template = 'blocks/accordion.html'
        help_text = 'Accordions are elements that help you organize and navigate multiple documents in a single container. They can be used for switching between items in the container.'


class CallToActionButtonBlock(StructBlock):
    button_target = PageChooserBlock(required=False, help_text='Choose where this button should link to.')
    button_text = CharBlock(required=False, help_text='What should the button say?')

    class Meta:
        icon = 'fa-arrow-right'
        template = 'blocks/button.html'
        help_text = 'Create a cll to action button to help guide users to the next step.'



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


class SimpleFlowBlock(StructBlock):
    title = CharBlock()


class DetailedFlowBlock(StructBlock):
    origin_icon = IconBlock(required=False)
    origin_title = CharBlock(required=False)
    icon = IconBlock(required=False)
    title = CharBlock()


class PeriodicBlock(StructBlock):
    icon = IconBlock(required=False)
    title = CharBlock()
    link = CharBlock(required=False)


class SimpleFlowBlockList(ListBlock):
    def __init__(self, **kwargs):
        super().__init__(SimpleFlowBlock, **kwargs)

    class Meta:
        icon = 'fa-long-arrow-right'
        template = 'blocks/simple_flow_boxes.html'
        help_text = """
                    Displays a flowchart of simple text boxes.
                    It flows left-to-right and uses 2-4 entries to
                    show how one idea can lead to the next.
                    """


class DetailedFlowBlockList(ListBlock):
    def __init__(self, **kwargs):
        super().__init__(DetailedFlowBlock, **kwargs)

    class Meta:
        icon = 'fa-long-arrow-right'
        template = 'blocks/detailed_flow_boxes.html'
        help_text = """
                    Displays a zoomed-in fragment of a flowchart.
                    It flows left-to-right, and uses 2-3 entries to show a
                    cause-and-effect within a broader context.
                    """


class PeriodicBlockList(ListBlock):
    def __init__(self, **kwargs):
        super().__init__(PeriodicBlock, **kwargs)

    class Meta:
        icon = 'fa-th'
        template = 'blocks/periodic_boxes.html'
        help_text = """
                    Displays a series of numbered boxes, flowing left to right.
                    If you include an icon, only one short line of text fits.
                    Fit more text with no icon.
                    """


class HightlightBlock(StructBlock):
    body = RichTextBlock(icon='fa-paragraph')

    class Meta:
        icon = 'fa-square'
        template = 'blocks/highlightblock.html'
        help_text = 'A rich text block with a tan background.'


class LimitedStreamBlock(StreamBlock):
    paragraph = RichTextBlock(icon='fa-paragraph')
    smaller_heading = TextBlock(
        icon='fa-header', template='blocks/smaller_heading.html')

    class Meta:
        template = 'blocks/streamfield.html'


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
    button = CallToActionButtonBlock()
    simple_flow_boxes = SimpleFlowBlockList()
    detailed_flow_boxes = DetailedFlowBlockList()
    periodic_boxes = PeriodicBlockList()
    highlight_block = HightlightBlock()

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
