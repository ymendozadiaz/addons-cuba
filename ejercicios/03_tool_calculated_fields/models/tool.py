# -*- coding: utf-8 -*-
from odoo import api, fields, models

class tool(models.Model):
    _inherit = 'ej.tool'
    
    is_good_conditions = fields.Boolean(string='Goods conditions' ,
                                    compute='_compute_good_conditions')

    is_not_good_conditions = fields.Boolean(string='Not good conditions',
                                    compute='_compute_not_good_conditions',
                                    store=True)

    mydb = fields.Char(default=lambda self: self.env.cr.dbname, string='db')

    @api.depends('good_conditions')
    def _compute_good_conditions(self):
        for record in self:
            record.is_good_conditions = record.good_conditions

    @api.depends('good_conditions')
    def _compute_not_good_conditions(self):
        for record in self:
            record.is_not_good_conditions = not record.good_conditions