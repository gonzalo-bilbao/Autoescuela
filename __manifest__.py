# -*- coding: utf-8 -*-
{
    'name': "Autoescuela",

    'summary': "Trabajo gestionn empresas de autoescuelas",

    'description': """
Trabajo de gestion de empresas de autoescuelas en el cual
trabajamos con github para crear un modulo en odoo mediante visual studio code
    """,

    'author': "Alberto Luque, Vicente Mena, Gonzalo Bilbao",
    'website': "https://github.com/gonzalo-bilbao/Autoescuela",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    #inidcamos que es una aplicacion
    'application': True,
}

