# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    type = fields.Selection(selection_add=[
        ('test', 'Test'),
        ], tracking=True, ondelete={'test': 'cascade', 'test2': 'set null'})