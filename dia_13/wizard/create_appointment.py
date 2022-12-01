# -*- coding: utf-8 -*-
from odoo import api, fields, models, _



class CreateAppointmentWizard(models.TransientModel):
    _name = "create.appointment.wizard"
    _description = "Create Appointment Wizard"

    name = fields.Char(string='Name', required=True)
    