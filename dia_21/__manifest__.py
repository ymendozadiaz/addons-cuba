# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Hospital Management',
    'version' : '16.0',
    'summary': 'Hospital Management Software',
    'sequence': -100,
    'description': """Hospital Management Software""",
    'category': 'Productivity',
    'website': '',
    'depends' : [
        'sale',
        'mail'],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/patient.xml',
        'views/doctor_view.xml',
        'wizard/create_appointment_view.xml',
        'wizard/search_appointment_view.xml',
        'views/kids_view.xml',
        'views/patient_gender_view.xml',
        'views/appointment_view.xml',
        'views/sale.xml',
        'report/patient_card.xml',
        'report/report.xml'
    ],
    'images': ['static/description/banner.png'],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'license': 'LGPL-3',
}