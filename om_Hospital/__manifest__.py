# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Hospital Management',
    'version' : '16.0',
    'summary': 'Hospital Management Software',
    'sequence': -100,
    'description': """Hospital Management Software""",
    'category': 'Productivity',
    'website': 'https://www.odoomates.tech',
    'depends' : ['sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/patient.xml',
        'views/sale.xml'
    ],
    'images': ['.static/description/mycomputer.ico'],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}