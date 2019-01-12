=============================
django-dadata
=============================

Some django batteries for dadata.ru services


Quickstart
----------

Install django-dadata::

    pip install -e git+https://github.com/okfish/django-dadata.git#egg=django-dadata

Then use it in a project::

    # forms.py
    
    from dadata.widgets import DadataWidget
    from dadata import PARTY
    
    # form class definition
    name = CharField(widget=DadataWidget(
        {'suggestions_type': PARTY, 'linked-fields': {
            'inn' : 'data.inn', 'kpp' : 'data.kpp'}}))
                                                            
    # form.html
    
    # do not forget to add widget's media
    <head>
    	{{ form.media.js }}
    	{{ form.media.css }}
    </head>

Features
--------

 * Fields and validators (TODO)
 * Widgets
 	DadataOrgWidget uses dadata jquery suggestion plugin
 * REST API helpers (TODO)

Cookiecutter Tools Used in Making This Package
----------------------------------------------

*  cookiecutter
*  cookiecutter-djangopackage
