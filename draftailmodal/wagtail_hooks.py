import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from wagtail.admin.rich_text.converters.html_to_contentstate import InlineStyleElementHandler
from wagtail.admin.rich_text.converters.html_to_contentstate import InlineEntityElementHandler
from wagtail.core import hooks
from draftjs_exporter.dom import DOM
from django.urls import path, include
from . import urls


@hooks.register('register_admin_urls')
def register_admin_urls():
    return [
        path('draftailmodal/', include(urls))
    ]


@hooks.register('register_rich_text_features')
def register_tip_feature(features):
    features.default_features.append('tip')
    """
    Registering the `tip` feature, which uses the `tip` Draft.js entity type,
    and is stored as HTML with a `<span data-tip>` tag.
    """
    feature_name = 'tip'
    type_ = 'TIP'

    control = {
        'type': type_,
        'label': 'ⓘ',
        'description': 'Tip',
    }

    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.EntityFeature(
            control,
            js=['js/tip.js'],
            css={'all': ['css/tip.css']}
        )
    )

    features.register_converter_rule('contentstate', feature_name, {
        # Note here that the conversion is more complicated than for blocks and inline styles.
        'from_database_format': {'span[data-tip]': TipEntityElementHandler(type_)},
        'to_database_format': {'entity_decorators': {type_: tip_entity_decorator}},
    })


def tip_entity_decorator(props):
    """
    Draft.js ContentState to database HTML.
    Converts the tip entities into a span tag.
    """
    return DOM.create_element('span', {
        'data-tip': props['tip'],
    }, props['children'])


class TipEntityElementHandler(InlineEntityElementHandler):
    """
    Database HTML to Draft.js ContentState.
    Converts the span tag into a tip entity, with the right data.
    """
    mutability = 'IMMUTABLE'

    def get_attribute_data(self, attrs):
        """
        Take the ``tip`` value from the ``data-tip`` HTML attribute.
        """
        return {
            'tip': attrs['data-tip'],
        }
