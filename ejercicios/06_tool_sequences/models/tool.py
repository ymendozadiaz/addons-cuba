# -*- coding: utf-8 -*- 
# Part of Odoo. See LICENSE file for full copyright and licensing details. 
from odoo import api, fields, models, _
from datetime import datetime 

class Tools(models.Model): 
    _name = 'ej.tool' 
    _description = 'Tool'
    
    user = fields.Char(string='User', required=True) 

    code = fields.Char(string='code', default='New', readonly=1)
 
    exploitation_years = fields.Integer(string='exploitation_years', required=True) 
 
    size = fields.Char(string='size', required=True) 
 
    type = fields.Selection([('spanish', 'Spanish'),
                             ('english', 'English'),
                             ('cube', 'Cube'),
                             ('allien', 'Allien')], string='type', default="spanish", required=True)
    
    @api.model
    def create(self, vals):
        if vals.get('code', "New") == "New":
            vals['code'] = self.env['ir.sequence'].next_by_code(
                'ej.tool') or "New"
        tool = super(Tools, self).create(vals)
        return tool