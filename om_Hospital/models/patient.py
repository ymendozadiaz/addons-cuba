# -*- coding: utf-8 -*-
from odoo import api, fields, models



class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _description = "Hospital Patient"
    _order = "is_off_balance, code, company_id"
    _check_company_auto = True
