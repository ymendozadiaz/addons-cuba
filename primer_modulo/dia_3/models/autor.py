from odoo import models, fields


class Libros(models.Model):
    _name = 'autor'
    _Description = 'Autor'
    
    name = fields.Char(string="Nombre")
    last_name = fields.Char(string="Apellidos")