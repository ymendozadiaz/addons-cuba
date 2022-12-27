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
    'name': 'ticket_c MFH',
    'sequence': -100,
    'version': '16.0.0.1.0',
    'author': "Marlon Falc�n Her�ndez",
    'maintainer': 'Marlon Falcon',
    'website': 'http://www.marlonfalcon.com',
    'license': 'AGPL-3',
    'category': 'account.payment',
    'summary': 'Ejemplo de un m�dulo by Marlon.',
    'depends': ['base','stock','mail'],
    'description': """
Modulo basado en Marlon
===================================================== 
�ste m�dulo permite selecionar 
""",
    'demo': [],
    'test': [],
    'data': [
        'data/data.xml',
        'views/ticket_c_view.xml', 
        'security/ir.model.access.csv'
    ],
    'installable': True,
    'auto_install': False,
}
