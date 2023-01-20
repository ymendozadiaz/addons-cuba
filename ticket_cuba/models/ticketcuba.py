# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError

class TicketCuba(models.Model):
    _name = "ticket.cuba"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Ticket order"

    code = fields.Char(string='code', required=True, copy= False, readonly=1, default=lambda self: _('New'))
    user_id = fields.Many2one('res.users', string='Creado', default=lambda self: self.env.user, tracking=True, readonly="False")
    name_ticket = fields.Char(string='Name', required=True, tracking=True)
    price = fields.Integer(string="Price", tracking=True)
    description = fields.Char(string='Description', tracking=True)
    state = fields.Selection([('new', 'New'), 
                               ('validated', 'Validated'),
                               ('finish', 'Finish')], default='new', tracking=True)


    def button_validated(self):
        self.state = 'validated'

    def button_new(self):
        self.state = 'new'

    def button_finish(self):
        self.state = 'finish'

    @api.model
    def create(self, vals):
        if vals.get('code', "New") == "New":
            vals['code'] = self.env['ir.sequence'].next_by_code(
                'ticket.cuba') or "New"
        ticket = super(TicketCuba, self).create(vals)
        return ticket

    @api.constrains('price')
    def check_price(self):
        for rec in self:
            if rec.price == 0:
                raise ValidationError(_("Price Cannot be Zero...!"))