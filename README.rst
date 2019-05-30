=============================
django-dadata
=============================

Some django batteries for dadata.ru services


Quickstart
----------

Install django-dadata::

    pip install -e git+https://github.com/pik-software/django-dadata.git#egg=django-dadata

Then use it in a project::

    # forms.py

    import django_dadata.widgets import DadataOrgWidget
    ...

    # form class definition
    name = CharField(widget=DadataOrgWidget(
        attrs={'data-linked-fields': {'inn' : '#id_vatin','kpp' : '#id_reason_code'}}))

    # form.html
    # do not forget to add widget's media
    <head>
    	{{ form.media.js }}
    	{{ form.media.css }}
    </head>
