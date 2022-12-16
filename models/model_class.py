from odoo import models, fields

class classs (models.Model):

     _name='class'
     _description = 'class'
   
     idClass = fields.Char("class ID", required=True, select=True)
     name = fields.Char("Label",size=255, required=True)
     idLevel = fields.Many2one('level','Level',ondelete='cascade', required=True)
     idScholarYear = fields.Many2one('scholaryear','Scholar Year', ondelete='cascade', required=True)
     mainProfessor = fields.Many2one('professor','Main Professor', ondelete='cascade')
     inscription_ids = fields.One2many('inscription', 'idClass', string='Inscriptions')
     module_ids = fields.One2many('module', 'idClass', string='Modules')