# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class TicketCuba(models.Model):
    _name = "ticket.cuba"
    _inherit = "mail.thread"
    _description = "Ticket order description"

    user_id = fields.Many2one('res.users', string='Creado', default=lambda self: self.env.user, tracking=True, readonly="False")
    name_ticket = fields.Char(string='Name', required=True, tracking=True)
    price = fields.Integer(string="Price", tracking=True, default="100")
    note = fields.Text(string="note", tracking=True)
