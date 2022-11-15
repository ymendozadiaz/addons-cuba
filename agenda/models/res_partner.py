# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, fields


class ResPartner(models.Model):
    _inherit = 'res.partner'
    
    academy_id = fields.Many2one(
        comodel_name='open.academy',
        string='Academy',
    )

    partners_ids = fields.Many2many(
        comodel_name='open.academy',
        relation='academy_partner_rel',
        column1='partner_id',
        column2='academy_id',
        string='Academies',
    )