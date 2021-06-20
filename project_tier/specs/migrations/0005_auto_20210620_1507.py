# Generated by Django 2.2.9 on 2021-06-20 19:07

from django.db import migrations
import project_tier.blocks
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.documents.blocks
import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('specs', '0004_auto_20210620_1456'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filepage',
            name='body',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph')), ('bigger_heading', wagtail.core.blocks.TextBlock(icon='fa-header', label='H2', template='blocks/h2.html')), ('heading', wagtail.core.blocks.TextBlock(icon='fa-header', label='H3', template='blocks/h3.html')), ('smaller_heading', wagtail.core.blocks.TextBlock(icon='fa-header', label='H4', template='blocks/h4.html')), ('smallest_heading', wagtail.core.blocks.TextBlock(icon='fa-header', label='H5', template='blocks/h5.html')), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.TextBlock(required=False))])), ('download', wagtail.documents.blocks.DocumentChooserBlock(icon='fa-download', template='blocks/download.html')), ('accordion', wagtail.core.blocks.StructBlock([('panels', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(help_text='The headline to display when the accordion panel is closed.')), ('body', wagtail.core.blocks.RichTextBlock(help_text='The inner content of this accordion panel. It is initially hidden.'))], label='Panel')))])), ('notice', wagtail.core.blocks.StructBlock([('message', wagtail.core.blocks.RichTextBlock(help_text='Write the message text.')), ('indicator', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Standard'), ('success', 'Success'), ('alert', 'Alert'), ('warning', 'Warning')], help_text='Choose what type of notice this is.', required=False))])), ('embed', wagtail.embeds.blocks.EmbedBlock(icon='media')), ('button', wagtail.core.blocks.StructBlock([('button_target', wagtail.core.blocks.PageChooserBlock(help_text='Choose where this button should link to.', required=False)), ('button_text', wagtail.core.blocks.CharBlock(help_text='What should the button say?', required=False))])), ('simple_flow_boxes', project_tier.blocks.SimpleFlowBlockList()), ('detailed_flow_boxes', project_tier.blocks.DetailedFlowBlockList()), ('periodic_boxes', project_tier.blocks.PeriodicBlockList()), ('highlight_block', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph'))])), ('slider_block', wagtail.core.blocks.StructBlock([('slides', wagtail.core.blocks.StreamBlock([('slide', wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph', required=False)), ('image_or_video', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='Choose a horizontal photo', required=False)), ('link', wagtail.core.blocks.URLBlock(help_text='A youtube link to a video', required=False))], blank=False, help_text='Either upload an image, or link to a video. If both fields are present, the video will take precident', required=True))], blank=False, help_text='A single slide'))], blank=True, help_text='Add a slide to the slider'))])), ('hr_block', wagtail.core.blocks.StructBlock([], icon='fa-window-minimize', label='Divider', template='blocks/hr.html'))], blank=True),
        ),
        migrations.AlterField(
            model_name='folderpage',
            name='body',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph')), ('bigger_heading', wagtail.core.blocks.TextBlock(icon='fa-header', label='H2', template='blocks/h2.html')), ('heading', wagtail.core.blocks.TextBlock(icon='fa-header', label='H3', template='blocks/h3.html')), ('smaller_heading', wagtail.core.blocks.TextBlock(icon='fa-header', label='H4', template='blocks/h4.html')), ('smallest_heading', wagtail.core.blocks.TextBlock(icon='fa-header', label='H5', template='blocks/h5.html')), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.TextBlock(required=False))])), ('download', wagtail.documents.blocks.DocumentChooserBlock(icon='fa-download', template='blocks/download.html')), ('accordion', wagtail.core.blocks.StructBlock([('panels', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(help_text='The headline to display when the accordion panel is closed.')), ('body', wagtail.core.blocks.RichTextBlock(help_text='The inner content of this accordion panel. It is initially hidden.'))], label='Panel')))])), ('notice', wagtail.core.blocks.StructBlock([('message', wagtail.core.blocks.RichTextBlock(help_text='Write the message text.')), ('indicator', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Standard'), ('success', 'Success'), ('alert', 'Alert'), ('warning', 'Warning')], help_text='Choose what type of notice this is.', required=False))])), ('embed', wagtail.embeds.blocks.EmbedBlock(icon='media')), ('button', wagtail.core.blocks.StructBlock([('button_target', wagtail.core.blocks.PageChooserBlock(help_text='Choose where this button should link to.', required=False)), ('button_text', wagtail.core.blocks.CharBlock(help_text='What should the button say?', required=False))])), ('simple_flow_boxes', project_tier.blocks.SimpleFlowBlockList()), ('detailed_flow_boxes', project_tier.blocks.DetailedFlowBlockList()), ('periodic_boxes', project_tier.blocks.PeriodicBlockList()), ('highlight_block', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph'))])), ('slider_block', wagtail.core.blocks.StructBlock([('slides', wagtail.core.blocks.StreamBlock([('slide', wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph', required=False)), ('image_or_video', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='Choose a horizontal photo', required=False)), ('link', wagtail.core.blocks.URLBlock(help_text='A youtube link to a video', required=False))], blank=False, help_text='Either upload an image, or link to a video. If both fields are present, the video will take precident', required=True))], blank=False, help_text='A single slide'))], blank=True, help_text='Add a slide to the slider'))])), ('hr_block', wagtail.core.blocks.StructBlock([], icon='fa-window-minimize', label='Divider', template='blocks/hr.html'))], blank=True),
        ),
        migrations.AlterField(
            model_name='optionalfilepage',
            name='body',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph')), ('bigger_heading', wagtail.core.blocks.TextBlock(icon='fa-header', label='H2', template='blocks/h2.html')), ('heading', wagtail.core.blocks.TextBlock(icon='fa-header', label='H3', template='blocks/h3.html')), ('smaller_heading', wagtail.core.blocks.TextBlock(icon='fa-header', label='H4', template='blocks/h4.html')), ('smallest_heading', wagtail.core.blocks.TextBlock(icon='fa-header', label='H5', template='blocks/h5.html')), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.TextBlock(required=False))])), ('download', wagtail.documents.blocks.DocumentChooserBlock(icon='fa-download', template='blocks/download.html')), ('accordion', wagtail.core.blocks.StructBlock([('panels', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(help_text='The headline to display when the accordion panel is closed.')), ('body', wagtail.core.blocks.RichTextBlock(help_text='The inner content of this accordion panel. It is initially hidden.'))], label='Panel')))])), ('notice', wagtail.core.blocks.StructBlock([('message', wagtail.core.blocks.RichTextBlock(help_text='Write the message text.')), ('indicator', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Standard'), ('success', 'Success'), ('alert', 'Alert'), ('warning', 'Warning')], help_text='Choose what type of notice this is.', required=False))])), ('embed', wagtail.embeds.blocks.EmbedBlock(icon='media')), ('button', wagtail.core.blocks.StructBlock([('button_target', wagtail.core.blocks.PageChooserBlock(help_text='Choose where this button should link to.', required=False)), ('button_text', wagtail.core.blocks.CharBlock(help_text='What should the button say?', required=False))])), ('simple_flow_boxes', project_tier.blocks.SimpleFlowBlockList()), ('detailed_flow_boxes', project_tier.blocks.DetailedFlowBlockList()), ('periodic_boxes', project_tier.blocks.PeriodicBlockList()), ('highlight_block', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph'))])), ('slider_block', wagtail.core.blocks.StructBlock([('slides', wagtail.core.blocks.StreamBlock([('slide', wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph', required=False)), ('image_or_video', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='Choose a horizontal photo', required=False)), ('link', wagtail.core.blocks.URLBlock(help_text='A youtube link to a video', required=False))], blank=False, help_text='Either upload an image, or link to a video. If both fields are present, the video will take precident', required=True))], blank=False, help_text='A single slide'))], blank=True, help_text='Add a slide to the slider'))])), ('hr_block', wagtail.core.blocks.StructBlock([], icon='fa-window-minimize', label='Divider', template='blocks/hr.html'))], blank=True),
        ),
        migrations.AlterField(
            model_name='specslandingpage',
            name='body',
            field=wagtail.core.fields.StreamField([('paragraph', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph')), ('bigger_heading', wagtail.core.blocks.TextBlock(icon='fa-header', label='H2', template='blocks/h2.html')), ('heading', wagtail.core.blocks.TextBlock(icon='fa-header', label='H3', template='blocks/h3.html')), ('smaller_heading', wagtail.core.blocks.TextBlock(icon='fa-header', label='H4', template='blocks/h4.html')), ('smallest_heading', wagtail.core.blocks.TextBlock(icon='fa-header', label='H5', template='blocks/h5.html')), ('image', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock()), ('caption', wagtail.core.blocks.TextBlock(required=False))])), ('download', wagtail.documents.blocks.DocumentChooserBlock(icon='fa-download', template='blocks/download.html')), ('accordion', wagtail.core.blocks.StructBlock([('panels', wagtail.core.blocks.ListBlock(wagtail.core.blocks.StructBlock([('title', wagtail.core.blocks.TextBlock(help_text='The headline to display when the accordion panel is closed.')), ('body', wagtail.core.blocks.RichTextBlock(help_text='The inner content of this accordion panel. It is initially hidden.'))], label='Panel')))])), ('notice', wagtail.core.blocks.StructBlock([('message', wagtail.core.blocks.RichTextBlock(help_text='Write the message text.')), ('indicator', wagtail.core.blocks.ChoiceBlock(choices=[('', 'Standard'), ('success', 'Success'), ('alert', 'Alert'), ('warning', 'Warning')], help_text='Choose what type of notice this is.', required=False))])), ('embed', wagtail.embeds.blocks.EmbedBlock(icon='media')), ('button', wagtail.core.blocks.StructBlock([('button_target', wagtail.core.blocks.PageChooserBlock(help_text='Choose where this button should link to.', required=False)), ('button_text', wagtail.core.blocks.CharBlock(help_text='What should the button say?', required=False))])), ('simple_flow_boxes', project_tier.blocks.SimpleFlowBlockList()), ('detailed_flow_boxes', project_tier.blocks.DetailedFlowBlockList()), ('periodic_boxes', project_tier.blocks.PeriodicBlockList()), ('highlight_block', wagtail.core.blocks.StructBlock([('body', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph'))])), ('slider_block', wagtail.core.blocks.StructBlock([('slides', wagtail.core.blocks.StreamBlock([('slide', wagtail.core.blocks.StructBlock([('caption', wagtail.core.blocks.RichTextBlock(icon='fa-paragraph', required=False)), ('image_or_video', wagtail.core.blocks.StructBlock([('image', wagtail.images.blocks.ImageChooserBlock(help_text='Choose a horizontal photo', required=False)), ('link', wagtail.core.blocks.URLBlock(help_text='A youtube link to a video', required=False))], blank=False, help_text='Either upload an image, or link to a video. If both fields are present, the video will take precident', required=True))], blank=False, help_text='A single slide'))], blank=True, help_text='Add a slide to the slider'))])), ('hr_block', wagtail.core.blocks.StructBlock([], icon='fa-window-minimize', label='Divider', template='blocks/hr.html'))]),
        ),
    ]
