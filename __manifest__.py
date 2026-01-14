# -*- coding: utf-8 -*-
{
    'name': "Autoescuela",

    'summary': "Trabajo gestion empresas de autoescuelas",

    'description': """
Trabajo de gestion de empresas de autoescuelas en el cual
trabajamos con github para crear un modulo en odoo mediante visual studio code
    """,

    'author': "Alberto Luque, Vicente Mena, Gonzalo Bilbao",
    'website': "https://github.com/gonzalo-bilbao/Autoescuela",

    # Categories can be used to filter modules in modules listing
    'category': 'Administration', # He cambiado Uncategorized por algo más estándar
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/autoescuela_security.xml',
        'security/ir.model.access.csv',
        # 'data/sequence_data.xml',        
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    # indicamos que es una aplicacion para que salga en el menú principal
    'application': True,
    'installable': True,
}