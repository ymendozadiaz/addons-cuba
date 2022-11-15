# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

{
    'name': 'Agenda 2022',
    'version': '1.0.0.0',
    'author': 'Yosbel Mendoza Díaz',
    'maintainer': 'Yosbel Mendoza Díaz',
    'category': 'Extra Tools',
    'summary': 'Short summary.',
    'depends': ['contacts'],
    'data': [
        'security/ir.model.access.csv',
        'views/open_academy_view.xml',
        'views/res_partner_view.xml',
    ],
    'images': ['static/description/codies.ico'],
    'application': True,
    'license': 'LGPL-3',
    'demo': [
        'demo/demo.xml'    
    ],
}
