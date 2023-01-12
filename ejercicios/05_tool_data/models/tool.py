# -*- coding: utf-8 -*- 
# Part of Odoo. See LICENSE file for full copyright and licensing details. 
from odoo import api, fields, models 
from datetime import datetime 

class tool(models.Model): 
    _name = 'ej.tool' 
    
    user = fields.Char(string='User', required=True) 
 
    exploitation_years = fields.Integer(string='exploitation_years', required=True) 
 
    size = fields.Char(string='size', required=True) 
 
    type = fields.Selection([('spanish', 'Spanish'),
                             ('english', 'English'),
                             ('cube', 'Cube'),
                             ('allien', 'Allien')], string='type', default="spanish", required=True)
 
