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
    'depends': ['base','mail','hr', 'sale'],
    'data': [
        'security/ir.model.access.csv',
        'data/ir_sequence.xml',
        'views/ticket_view.xml',
        'views/create_invoice_view.xml',
        'views/account_ticket_view.xml',
        'report/account_ticket_details.xml',
        'report/reports.xml'
        ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3'
}