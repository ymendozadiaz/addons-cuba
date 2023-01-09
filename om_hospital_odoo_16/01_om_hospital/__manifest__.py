# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Hospital Management System',
    'author': 'Yosbel Mendoza Díaz',
    'sumary': 'Odoo 16 development',
    'version': '1.0.0.0',
    'category': 'Extra Tools',
    'depends': ['mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient.xml'
    ],
    'installable': True,
    'application': True,
    'sequence': -150,
    'license': 'LGPL-3'
}