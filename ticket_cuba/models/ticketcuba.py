# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class TicketCuba(models.Model):
    _name = "ticket.cuba"
    _description = "Ticket order description"
    _inherit = ['mail.activity.mixin', 'mail.thread']
    
    
    user_id = fields.Many2one('res.users', string='Creado',
                              default=lambda self: self.env.user)
    name_ticket = fields.Char(string='name', required=True, tracking=True)
    price = fields.Float(string="Price", tracking=True)
    note = fields.Text( string="Note", tracking=True)