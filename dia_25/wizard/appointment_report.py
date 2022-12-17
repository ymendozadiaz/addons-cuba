# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class AppointmentReportWizard(models.TransientModel):
    _name = "appointment.report.wizard"
    _description = "Print Appointment Wizard"
    
    patient_id = fields.Many2one('hospital.patient', string="Patient")
    date_from = fields.Date(string="Date From")
    date_to = fields.Date(string="Date To")
        
    def action_print_report(self):
        appointments = self.env['hospital.appointment'].search_read([])
        data = {
            'form': self.read()[0],
            'appointments': appointments
        }
        return self.env.ref('om_Hospital.action_report_appointment').report_action(self, data=data)