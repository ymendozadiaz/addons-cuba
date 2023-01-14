# -*- coding: utf-8 -*-
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError



class AccountTicket(models.Model):
    _name = "account.ticket"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Account Ticket"
    
    code = fields.Char(string='code', required=True, copy= False, readonly=1, default=lambda self: _('New'))
    
    name_ticket_id = fields.Many2one('ticket.cuba', string="Name Ticket", required=True, tracking=True)
    
    price = fields.Integer(string="Order Price", required=True)

    date_account = fields.Date(string="Date Account", required=True,)

    date_pay = fields.Datetime(string="Date pay", required=True,)

    description = fields.Text(string='description')

    operations_line_ids = fields.One2many('account.operations.lines', 'accountticket_id',
                                            string="Operations Lines")

    state = fields.Selection([('draft', 'Draft'), ('validated', 'Validated'), ('finished', 'Finished')],
                                 default='draft', string="Status", tracking=True)


    def action_validated(self):
        self.state = 'validated'

    def action_finished(self):
        self.state = 'finished'
    
    def action_draft(self):
        self.state = 'draft'

    @api.model
    def create(self, vals):
        if vals.get('code', "New") == "New":
            vals['code'] = self.env['ir.sequence'].next_by_code(
                'ticket.cuba') or "New"
        accountticket = super(AccountTicket, self).create(vals)
        return accountticket


class OperationsLines(models.Model):
    _name = "account.operations.lines"
    _description = "Account ticket Operations Lines"

    accountticket_id = fields.Many2one('account.ticket', string="Ticket")
    name = fields.Char(string="Operations", required=True,)
    Topay = fields.Integer(string="To pay", required=True)

    
