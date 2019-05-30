from django import forms
from django.utils.safestring import mark_safe

from django.conf import settings


class DadataWidget(forms.TextInput):

    def __init__(self, suggestion_type, linked_fields, count=5, attrs=None):
        super().__init__(attrs)
        self.type = suggestion_type
        self._linked_fields = linked_fields
        self.count = count
        self.token = settings.DADATA_API_SUGGESTION_TOKEN
        self.field_id = None

    @property
    def linked_fields(self):
        script = ''
        for field, path in self._linked_fields.items():
            script += f'$("#id_{field}").val(suggestion.{path});\n'
        return script

    def on_select_js_hook(self):
        return ''

    def create_script(self, field_id):
        return f'''
            <script type="text/javascript">
                $("#{field_id}").suggestions({{
                    token: "{self.token}",
                    type: "{self.type}",
                    count: "{self.count}",
                    onSelect: function(suggestion) {{
                        {self.linked_fields}
                        {self.on_select_js_hook()}
                    }}
                }});
            </script>'''

    def render(self, name, value, attrs=None, renderer=None):
        field_id = self.build_attrs(attrs)['id']
        result = super(DadataWidget, self).render(name, value, attrs, renderer)
        result += self.create_script(field_id)
        return mark_safe(result)

    class Media:
        js = [
            'https://cdnjs.cloudflare.com/ajax/libs/jquery/1.10.2/'
            'jquery.min.js',
            'https://cdn.jsdelivr.net/npm/suggestions-jquery@17.10.0/'
            'dist/js/jquery.suggestions.min.js'
        ]

        css = {
            'all': ['https://cdn.jsdelivr.net/npm/suggestions-jquery@18.11.1/'
                    'dist/css/suggestions.min.css']}
