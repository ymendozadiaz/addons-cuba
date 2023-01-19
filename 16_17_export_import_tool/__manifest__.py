# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2017 Marlon Falc�n Hernandez
#    (<http://www.marlonfalcon.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': ' Tool',
    'version': '16.0.0.1.0',
    'author': "Marlon Falc�n Her�ndez",
    'maintainer': 'Marlon Falcon',
    'website': 'http://www.marlonfalcon.com',
    'license': 'AGPL-3',
    'category': 'account.payment',
    'summary': 'Ejemplo de un m�dulo by Marlon.',
    'depends': ['base','stock'],
    'description': """
Control of tools in workshops   
Modulo basado en Marlon
===================================================== 
�ste m�dulo permite selecionar 
""",
    'demo': [],
    'test': [],
    'images': ['static/description/banner.jpg'],
    'data': [
    'views/tool_view.xml',
    'views/import_tools.xml', 
    'wizard/tool_export_excel_wzd.xml',
#    'data/tool_data.xml',
    'data/ir_sequence.xml',
    'security/ir.model.access.csv'
    ],
    'installable': True,
    'application': True,
    'sequence': -150,
    'license': 'LGPL-3',
    'auto_install': False
}
