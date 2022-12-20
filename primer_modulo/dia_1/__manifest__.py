# -*- coding: utf-8 -*-


{
    'name': 'Curso de programación odoo 16',
    'sequence': -150,
    'sumary':"""
    Cursos de programción de odoo 16, funcionalidades
    """,
    'author': 'Yosbel Mendoza Díaz',
    'category': 'Extra Tools',
    'version': '1.0.0.0',
    'depends': [],
    'data': [
        'security/libreria_security.xml',
        'security/ir.model.access.csv',
        'views/menu_view.xml',
        'views/libros_view.xml'
        ],
    'installable': True,
    'application': True
}