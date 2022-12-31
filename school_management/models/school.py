from odoo import models, fields


class School(models.Model):
    _name = 'school.student'

    name = fields.Many2one('res.partnet', string='Student')
    class_id = fields.Interger(string='Class')
    division = fields.Char(string='Division')
