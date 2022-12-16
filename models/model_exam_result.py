from odoo import models, fields


class exam_result (models.Model):

    _name="exam.result"
    _description = 'exam.result'

    idExam = fields.Many2one('exam','Exam',ondelete='cascade', required=True)
    idInscription = fields.Many2one('inscription','Inscription',ondelete='cascade',required=True)
    note = fields.Char("Note",size=255)
    report = fields.Text("Report")
    mark = fields.Float('Mark')
    originalMark = fields.Float('Original Mark',required=True)