# -*- coding: utf-8 -*- 
# Part of Odoo. See LICENSE file for full copyright and licensing details. 
from odoo import api, fields, models 
from datetime import datetime 

class tool(models.Model):
    _inherit = 'ej.tool' 

    good_conditions = fields.Boolean(string='Good conditions')
    use_time = fields.Integer(string='Use_time')
   
 
