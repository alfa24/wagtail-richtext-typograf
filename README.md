# Wagtail richtext typograf

Typograf plugin for RichTextField

Adds the ability typography text using the library [Typograf][typograf]

## Install

```
pip install git+https://github.com/alfa24/wagtail-richtext-typograf.git
```


## Quick start

1. Add "wagtail-richtext-typograf" to your INSTALLED_APPS setting like this:
    
        :::python
        # settings.py
        
        INSTALLED_APPS = [
            ...
            'wagtail_richtext_typograf',
        ]

2. Now we can use typograf in RichTextField.

* Add typograf for all default rich text fields in settings:

        :::python
        # settings.py
        
        WAGTAILADMIN_RICH_TEXT_EDITORS = {
            'default': {
                'WIDGET': 'wagtail.admin.rich_text.DraftailRichTextArea',
                'OPTIONS': {
                    'features': ['typograf']
                }
            }
        }

* Or add for a specific field:

        :::python
        # models.py
        
        text = fields.RichTextField(
            features=['typograf']
        )




[typograf]: https://github.com/typograf/typograf