# -*- coding: utf-8 -*-
from odoo import api, fields, models, _


class AppointmentReportWizard(models.TransientModel):
    _name = "appointment.report.wizard"
    _description = "Print Appointment Wizard"
    
    patient_id = fields.Many2one('hospital.patient', string="Patient")
    date_from = fields.Date(string="Date From")
    date_to = fields.Date(string="Date To")
        
    def action_print_report(self):
        domain = []
        patient_id = self.patient_id
        if patient_id:
            domain += [('patient_id', '=', patient_id.id)]
        date_from = self.date_from
        if date_from:
            domain += [('date_appointment', '>=', date_from)]
        date_to = self.date_to
        if date_to:
            domain += [('date_appointment', '<=', date_to)]
            
        appointments = self.env['hospital.appointment'].search(domain)
        appointment_list = []
        for appointment in appointments:
            vals = {
                'name': appointment.name,
                'note': appointment.note,
                'age': appointment.age,
            }
            appointment_list.append(vals)
        data = {
            'form_data': self.read()[0],
            'appointments': appointments
        }
        return self.env.ref('action_report_appointment').report_action(self, data=data)