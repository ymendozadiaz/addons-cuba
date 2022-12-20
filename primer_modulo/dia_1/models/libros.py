from odoo import models, fields


class Libros(models.Model):
    _name = 'libros'
    _Description = 'Libros'
    
    name = fields.Char(string="Nombre del libro")
    editorial = fields.Char(string="Editorial")