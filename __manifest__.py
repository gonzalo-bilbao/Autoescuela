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

    'category': 'Administration',
    'version': '1.0',

    'depends': ['base'],

    'data': [
        'security/autoescuela_security.xml',
        'security/ir.model.access.csv',

        'data/autoescuela_sequence.xml',
        
        'views/autoescuela_alumno_view.xml',
        'views/autoescuela_profesor_view.xml',
        'views/autoescuela_examen_view.xml', 
        'views/autoescuela_menus.xml', 

        'reports/autoescuela_alumno_report.xml',
        'reports/autoescuela_autoescuela_report.xml',
        'reports/autoescuela_examen_report.xml',
        'reports/autoescuela_profesor_report.xml',
    ],
    
    'demo': [
        'demo/demo.xml',
    ],
    'application': True,
    'installable': True,
}