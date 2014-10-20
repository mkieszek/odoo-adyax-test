{
    "name" : "Test module for Adyax",
    "version" : "0.1 ",
    "author" : "Via IT Solutions",
    "website" : "http://www.viait.pl/",
    "category" : "",
    "depends" : ['base','account'],

    "description": """
                     This is a test module for Adyax.
                    """,
    "init_xml": [],
    "update_xml": [
                   'view/new_model_view.xml',
                   'view/account_invoice_view.xml',
                   'wizard/import_new_model_view.xml'
                   ],
    "installable": True,
    "active": False,
}