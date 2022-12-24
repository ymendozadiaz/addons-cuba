from odoo import models, fields


class HrEmployee(models.Model):
    _inherit = "hr.employee"
    
    is_supervisor = fields.Boolean(string="Es supervisor")
 