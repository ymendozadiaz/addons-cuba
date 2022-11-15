# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, fields


class OpenAcademy(models.Model):
    _name = 'open.academy'
    _decription = 'Open Academy'

    name = fields.Char(
        string='Name',
        required=True,
    )

    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Partner',
        help='This is de teacher'
    )

    partner_ids = fields.One2many(
        comodel_name='res.partner',
        inverse_name='academy_id',
        string='Partners',
        help='This are students'
    )

    partners_ids = fields.Many2many(
        comodel_name='res.partner',
        relation='academy_partner_rel',
        column1='academy_id',
        column2='partner_id',
        string='Many Partners',
    )