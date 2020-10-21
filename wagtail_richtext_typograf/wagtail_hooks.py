import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from wagtail.admin.rich_text.converters.html_to_contentstate import InlineEntityElementHandler
from wagtail.core import hooks
from draftjs_exporter.dom import DOM


@hooks.register('register_rich_text_features')
def register_stock_feature(features):
    features.default_features.append('typograf')

    feature_name = 'typograf'
    type_ = 'TYPOGRAF'

    control = {
        'type': type_,
        'label': 'TF',
        'description': 'Типографировать текст',
    }

    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.EntityFeature(
            control,
            js=[
                'richtext-typograf/js/typograf.all.min.js',
                'richtext-typograf/js/richtext.typograf.js'
            ]
        )
    )

    features.register_converter_rule('contentstate', feature_name, {
        'from_database_format': {'span[data-typograf]': TypografEntityElementHandler(type_)},
        'to_database_format': {'entity_decorators': {type_: typograf_entity_decorator}},
    })


def typograf_entity_decorator(props):
    """
    Draft.js ContentState to database HTML.
    """
    return DOM.create_element('span', {
        'data-typograf': props['typograf'],
    }, props['children'])


class TypografEntityElementHandler(InlineEntityElementHandler):
    """
    Database HTML to Draft.js ContentState.
    """
    mutability = 'IMMUTABLE'

    def get_attribute_data(self, attrs):
        """
        Take the ``typograf`` value from the ``data-typograf`` HTML attribute.
        """
        return {
            'typograf': attrs['data-typograf'],
        }
