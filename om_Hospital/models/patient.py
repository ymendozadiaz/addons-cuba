# -*- coding: utf-8 -*-
from odoo import api, fields, models



class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Hospital Patient"

    name = fields.Char(string='Name', required=True)
    age = fields.Integer(string='Age')
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female'),
        ('male', 'Male'),
        ('other', 'Other'),
    ], required=True, default='Male')
    note = fields.Text(string='Description')