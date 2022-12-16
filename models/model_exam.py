from odoo import models, fields
from datetime import datetime,timedelta


class exam (models.Model):

    _name="exam"
    _description ='exam'

    idExam = fields.Char("Exam ID",select=True)
    name = fields.Char("Label",size=255,required=True)
    fromm = fields.Datetime("From")
    to = fields.Datetime("To")
    idModule = fields.Many2one('module','Module',ondelete='cascade',required=True)
    maxMark = fields.Integer('Max Marks',required=True)
    exam_result_ids = fields.One2many('exam.result', 'idExam', string='Exam\'s Results')
    idRoom = fields.Many2one('room','Room',ondelete='cascade')