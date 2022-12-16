from odoo import models, fields

class level (models.Model):

    _name="level"
    _description = 'level'

    idLevel = fields.Char("Level ID",required=True,select=True)
    name = fields.Char("Label",size=255,required=True),
    class_ids = fields.One2many('class', 'idLevel', string='Classes')
    