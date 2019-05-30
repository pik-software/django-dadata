from django_dadata.widgets import DadataWidget
from django_dadata import ORGANIZATION
from unittest import mock
from django.test.html import parse_html


class TestDadataWidget:
    @mock.patch('django_dadata.widgets.settings')
    def test_create_script(self, mocked_settings):
        mocked_settings.DADATA_API_SUGGESTION_TOKEN = 'asfhwqn12310adas123'
        widget = DadataWidget('PARTY', {'inn': 'data.inn'})
        script = widget.create_script('id_name')
        assert parse_html(script) == parse_html(
            '''
            <script type="text/javascript">
                        $("#id_name").suggestions({
                            token: "asfhwqn12310adas123",
                            type: "PARTY",
                            count: "5",
                            onSelect: function(suggestion) {
                                $("#id_inn").val(suggestion.data.inn);
                            }
                        });
            </script>''')
