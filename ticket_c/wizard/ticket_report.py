# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class TicketReportWizard(models.TransientModel):
    _name = "ticket.report.wizard"
    _description = "Print Ticket Wizard"
    
    ticket_c_id = fields.Many2one('ticket_c', string="Ticket")
    date_from = fields.Date(string="Date From")
    date_to = fields.Date(string="Date To")
        
    def action_print_report(self):
        domain = []
        ticket_c_id = self.ticket_c_id
        if ticket_c_id:
            domain += [('ticket_c_id', '=', ticket_c_id.id)]
        date_from = self.date_from
        if date_from:
            domain += [('date_ticket_c', '>=', date_from)]
        date_to = self.date_to
        if date_to:
            domain += [('date_ticket_c', '<=', date_to)]
            
        ticket_cs = self.env['ticket_c'].search(domain)
        ticket_c_list = []
        for ticket_c in ticket_cs:
            vals = {
                'name': ticket_c.name,
                'precio': ticket_c.precio,
                'nota': ticket_c.nota,
            }
            ticket_c_list.append(vals)
        data = {
            'form_data': self.read()[0],
            'ticket_cs': ticket_cs
        }
        return self.env.ref('action_report_ticket_c').report_action(self, data=data)