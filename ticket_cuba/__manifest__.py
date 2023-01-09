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
    'depends': ['mail','hr'],
    'data': [
        'security/ir.model.access.csv',
        'views/ticket_view.xml',
        'views/menu.xml'
        ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3'
}