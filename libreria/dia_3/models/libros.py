from odoo import models, fields, api


class Libros(models.Model):
    _name = 'libros'
    _inherit = ['mail.thread','mail.activity.mixin']
    
    
    supervisor_id = fields.Many2one(comodel_name='hr.employee', string="Supervisor")
    name = fields.Char(string="Nombre del libro", required=True, tracking=True)
    editorial = fields.Char(string="Editorial", required=True)
    isbn = fields.Char(string="ISBN", required=True)
    autor_id = fields.Many2one(comodel_name="autor", string="Autor", required=True)
    lastname_autor = fields.Char(related="autor_id.last_name", string="Apellido del autor")
    image = fields.Binary(string="Image")
    categoria_id = fields.Many2one(comodel_name="categoria.libro")
    state = fields.Selection([('draft','Borrador'),('published','Publicado')], default='draft')
    description = fields.Char(string="Descripcion", compute="_compute_description")
    
    @api.depends('name','isbn')
    def _compute_description(self):
        self.description = self.name + ' | ' + self.isbn + ' | ' + self.autor_id.name + ' | ' + self.categoria_id.name
    
    def boton_publicar(self):
        self.state = 'published'
    
    def boton_borrador(self):
        self.state = 'draft'
        
    _sql_contraints = [("name_uniq","unique (name)", "El nombre del libro ya existe!!")]
    
class CategoriaLibro(models.Model):
    _name = 'categoria.libro'
    
    name = fields.Char(string="Nombre de la categoria")