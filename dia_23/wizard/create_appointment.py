# -*- coding: utf-8 -*-
from odoo import api, fields, models, _



class CreateAppointmentWizard(models.TransientModel):
    _name = "create.appointment.wizard"
    _description = "Create Appointment Wizard"

    date_appointment = fields.Date(string='Date', required=False)
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    
    def action_create_appointment(self):
        vals = {
            'patient_id': self.patient_id.id,
            'doctor_id': 1,
            'date_appointment': self.date_appointment
        }
        appointment_rec = self.env['hospital.appointment'].create(vals)
        print("appointment", appointment_rec.id)
        return {
            'name': _('Appointment'),
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'hospital.appointment',
            'res_id': appointment_rec.id,
            'target': 'new',                             # quitando esta línea te en la misma ventana
        }
        
    def action_view_appointment(self):
        # método 1 
        #action = self.env.ref('om_Hospital.action_hospital_appointment').read()[0]
        #action['domain'] = [('patient_id', '=', self.patient_id.id)]
        #return action
    
        # método 2
        #action = self.env['ir.actions.actions']._for_xml_id("om_Hospital.action_hospital_appointment")
        #action['domain'] = [('patient_id', '=', self.patient_id.id)]
        #return action
    
        # método 3
        action = self.env.ref('om_Hospital.action_hospital_appointment').read()[0]
        action['domain'] = [('patient_id', '=', self.patient_id.id)]
        return {
            'type': 'ir.actions.act_window',
            'name': 'Appointments',
            'res_model': 'hospital.appointment',
            'view_type': 'form',
            'domain': [('patient_id', '=', self.patient_id.id)],
            'view_mode': 'tree,form',
            'target': 'current',
        }
        