from odoo import api, fields, models, _ 
from odoo.exceptions import ValidationError



class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = 'mail.thread'
    _description = "Patient Records"

    name = fields.Char(string='Name', required=True, tracking=True)
    age = fields.Integer(string='age', tracking=True)
    is_child = fields.Boolean(string='Is Child', tracking=True)
    note = fields.Text(string='Note', tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female'), ('others', 'Others')], string='Gender', required=True, tracking=True)
    capitalized_name = fields.Char(string='capitalized_name', compute='compute_capitalized_name', store=True)
    
    @api.constrains('is_child', 'age')
    def check_child_age(self):
        for rec in self:
            if rec.is_child and rec.age == 0:
                raise ValidationError(_("Age has to be recorded !"))

    @api.depends('name')
    def compute_capitalized_name(self):
        for rec in self:
            if rec.name:
                rec.capitalized_name = rec.name.upper()
            else:
                rec.capitalized_name = ''
    
    @api.onchange('age')
    def _onchange_age(self):
        if self.age <= 18:
            self.is_child = True
        else:
            self.is_child = False