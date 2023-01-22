# -*- coding: utf-8 -*-


{
    'name': 'ticket_cuba',
    'sequence': -150,
    'sumary': """
    ticket_cuba
    """,
    'author': 'Yosbel Mendoza Díaz',
    'category': 'Extra Tools',
    'version': '1.0.0.0',
    'depends': ['base','mail','hr', 'sale','account'],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence.xml',
        'wizard/create_invoice_wzd.xml',
        'views/ticket_view.xml'
        ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3'
}