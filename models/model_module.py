from odoo import models, fields

class module (models.Model):

    _name="module"
    _description = 'module'

    idModule = fields.Char("Module ID",required=True,select=True)
    name = fields.Char("Label",size=255,required=True)
    idClass = fields.Many2one('class','Class',ondelete='cascade',required=True)
    timetable_ids = fields.One2many('timetable', 'idModule', string='Timetables')
    exam_ids = fields.One2many('exam', 'idModule', string='Exams')
    course_ids = fields.One2many('course', 'idModule', string='Courses')
    