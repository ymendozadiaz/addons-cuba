
from odoo import models, fields


class OpenAcademy(models.Model):
    _name='open.academy'
    _description='Open Academy'

    name=fields.Char(
        string='name',
        required=True,
    )
