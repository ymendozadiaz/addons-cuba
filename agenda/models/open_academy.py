# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


from odoo import api, fields, models


class OpenAcademy(models.Model):
    _name = 'open.academy'

    name = fields.Char()