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
    CharBlock,
    URLBlock,
    BooleanBlock
)
from wagtailfontawesome.blocks import IconBlock


class AccordionBlock(StructBlock):
    compact = BooleanBlock(required=False, help_text='Display a compact accordion for use between paragraphs.')
    panels = ListBlock(StructBlock([
        ('title', TextBlock(help_text='The headline to display when the accordion panel is closed.')),
        ('body', RichTextBlock(help_text='The inner content of this accordion panel. It is initially hidden.'))
    ], label='Panel'))

    class Meta:
        icon = 'emoji-scroll'
        template = 'blocks/accordion.html'
        help_text = 'Accordions are elements that help you organize and navigate multiple documents in a single container. They can be used for switching between items in the container.'


class CardBlock(StructBlock):
    title = CharBlock()
    body = RichTextBlock(help_text='The inner content of this card.')

    class Meta:
        icon = 'fa-square-o'
        help_text = 'A standalone card element.'

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


class SimpleSliderBlock(StructBlock):
    slides = StreamBlock([
        ('slide', StructBlock([
            ('caption', RichTextBlock(icon='fa-paragraph', required=False)),
            ('image_or_video', StructBlock([
                ('image', ImageChooserBlock(help_text='Choose a horizontal photo', required=False)),
                ('link', URLBlock(help_text='A youtube link to a video', required=False)),
            ], help_text= 'Either upload an image, or link to a video. If both fields are present, the video will take precident', blank=False, required=True)),
        ], help_text= 'A single slide', blank=False)),
    ], help_text= 'Add a slide to the slider', blank=True)

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)

        def count_visible_slides():
            count = 0
            for slide in (value['slides']):
                count = count + 1
            return count

        context['visible_slides'] = count_visible_slides()
        return context

    class Meta:
        icon = 'fa-object-group'
        template = 'blocks/simple_slider.html'
        help_text = 'A dynamic slideslow of multiple images or videos.'


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


class GraphicLinkGridItemBlock(StructBlock):
    image = ImageChooserBlock()
    title = TextBlock(required=False)
    subtitle = TextBlock(required=False)
    link = URLBlock(required=False)

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)

        def formatted_title():
            title = value['title']
            if '& ' in title:
                split_title = title.rsplit('& ')
                formatted_title = split_title[0] + '&amp;&nbsp;' + split_title[1]
            else:
                formatted_title = None

            return formatted_title

        context['formatted_title'] = formatted_title()
        return context

    class Meta:
        icon = 'fa-icon-th'
        template = 'blocks/graphic_link_item.html'
        help_text = 'Select an image and add a caption (optional).'


class GraphicLinkGridBlock(StreamBlock):
    item = GraphicLinkGridItemBlock()

    class Meta:
        template = 'blocks/graphic_link_grid.html'


class FeaturedContentBlock(StructBlock):
    headline = TextBlock(help_text='Write a title for this section.', required=False, max_length=60)
    subtitle = TextBlock(help_text='Write a subtitle for this section.', required=False, max_length=22)
    image = ImageChooserBlock(help_text='Choose an image', required=False)

    CTA = StructBlock([
        ('text', CharBlock(help_text='What should the button say?', required=False)),
        ('link', URLBlock(help_text='Where should the button link to?', required=False)),
    ], help_text= 'An optional Call to Action button', blank=True)

    class Meta:
        icon = 'fa-flag'
        template = 'blocks/featured_content_block.html'
        help_text = 'Highlight featured content with this split red banner block'


class LimitedStreamBlock(StreamBlock):
    paragraph = RichTextBlock(icon='fa-paragraph')
    smaller_heading = TextBlock(
        icon='fa-header', template='blocks/smaller_heading.html')

    class Meta:
        icon = 'fa-paragraph'
        template = 'blocks/streamfield.html'


class ContentStreamBlock(StreamBlock):
    paragraph = RichTextBlock(icon='fa-paragraph')
    bigger_heading = TextBlock(icon='fa-header', template='blocks/h2.html', label='H2')
    heading = TextBlock(icon='fa-header', template='blocks/h3.html', label='H3')
    smaller_heading = TextBlock(
        icon='fa-header', template='blocks/h4.html', label='H4')
    smallest_heading = TextBlock(
        icon='fa-header', template='blocks/h5.html', label='H5')
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
    slider_block = SimpleSliderBlock()
    hr_block = StructBlock(icon='fa-window-minimize', template='blocks/hr.html', label='Divider')
    cards = ListBlock(CardBlock(), icon='fa-clone', template='blocks/cards.html')
    graphic_link_grid_grid = GraphicLinkGridBlock()
    featured_content_block = FeaturedContentBlock()

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


class IconHeaderBlock(StructBlock):
    headline = TextBlock(help_text='Write a title for this section.')
    icon = IconBlock(help_text='Optional icon', required=False)
    visible = BooleanBlock(default=True, required=False)

    class Meta:
        icon = 'fa-header'
        template = 'blocks/icon_banner_header.html'
        help_text = 'A red banner headline with optional icon'


class FeaturedEventsBlock(StreamBlock):
    event = PageChooserBlock(page_type='events.EventPage', required=True, help_text='Select an event from your Event Pages')

    class Meta:
        icon = 'fa-calendar'
        template = 'blocks/featured_events.html'
        help_text = 'You will need to complete an event page with all fields before selecting it here'


class MultiSliderBlock(StructBlock):
    orientation = ChoiceBlock(choices=[
        ('left', 'Left'),
        ('right', 'Right'),
    ], required=True, default='left', help_text='Choose which side of the image the text will appear on.')

    slides = StreamBlock([
        ('slide', StructBlock([
            ('headline', TextBlock(help_text='Write a title for this section.', required=False)),
            ('paragraph', RichTextBlock(icon='fa-paragraph', required=False)),
            ('visible', BooleanBlock(default=True, required=False)),
            ('CTA', StructBlock([
                ('text', CharBlock(help_text='What should the button say?', required=False)),
                ('link', URLBlock(help_text='Where should the button link to?', required=False)),
            ], help_text= 'An optional Call to Action button', blank=True)),
            ('image_or_video', StructBlock([
                ('image', ImageChooserBlock(help_text='Choose a horizontal photo', required=False)),
                ('link', URLBlock(help_text='A youtube link to a video', required=False)),
            ], help_text= 'Either upload an image, or link to a video. If both fields are present, the video will take precident', blank=False, required=True)),
        ], help_text= 'A single slide', blank=False)),
    ], help_text= 'Add a slide to the slider', blank=True)

    def get_context(self, value, parent_context=None):
        context = super().get_context(value, parent_context=parent_context)

        def count_visible_slides():
            count = 0
            for slide in (value['slides']):
                print(slide.value)
                if slide.value['visible'] == True:
                    count = count + 1
            return count

        context['visible_slides'] = count_visible_slides()
        return context

    class Meta:
        icon = 'fa-object-group'
        template = 'blocks/multi_slider_section.html'
        help_text = 'A dynamic block with a split red banner background and image. Add multiple slides to seemlessly move between content.'


class SplitBannerSectionBlock(StructBlock):
    orientation = ChoiceBlock(choices=[
        ('left', 'Left'),
        ('right', 'Right'),
    ], required=True, default='left', help_text='Choose which side of the image the text will appear on.')

    headline = TextBlock(help_text='Write a title for this section.', required=False)
    paragraph = RichTextBlock(icon='fa-paragraph', required=False)

    CTA = StructBlock([
        ('text', CharBlock(help_text='What should the button say?', required=False)),
        ('link', URLBlock(help_text='Where should the button link to?', required=False)),
    ], help_text= 'An optional Call to Action button', blank=True)

    image_or_video = StructBlock([
        ('image', ImageChooserBlock(help_text='Choose a horizontal photo', required=False)),
        ('link', URLBlock(help_text='A youtube link to a video', required=False)),
    ], help_text= 'Either upload an image, or link to a video. If both fields are present, the video will take precident', blank=False, required=True)

    visible = BooleanBlock(default=True, required=False)

    class Meta:
        icon = 'fa-object-ungroup'
        template = 'blocks/split_banner_section.html'
        help_text = 'A dynamic block with a split red banner background and image'


class HomeStreamBlock(StreamBlock):
    header = IconHeaderBlock()
    events = FeaturedEventsBlock()
    slider = MultiSliderBlock()
    text = RichTextBlock(icon='fa-paragraph', required=False)

    class Meta:
        template = 'blocks/streamfield.html'
