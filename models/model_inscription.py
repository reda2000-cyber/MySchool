from odoo import models, fields
from datetime import datetime,timedelta

class inscription (models.Model):

    _name="inscription"
    _description = 'inscription'

    idInscription = fields.Char("Inscription ID",select=True)
    idClass = fields.Many2one('class','Class',ondelete='cascade',required=True)
    idEleve = fields.Many2one('eleve','Student',ondelete='cascade',required=True)
    created_at = fields.Datetime("Created time",required=True)
    exam_result_ids = fields.One2many('exam.result', 'idInscription', string='Exam\'s Results')