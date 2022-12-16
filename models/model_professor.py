from odoo import models, fields
from datetime import datetime,timedelta


class professor (models.Model):

    _name="professor"
    _description = 'professor'
    _inherit="person"

    idProfessor = fields.Char("Professor ID",required=True,select=True)
    speciality = fields.Many2one('speciality','Speciality',ondelete='cascade')
    inService = fields.Boolean("Still in service")
    class_ids = fields.One2many('class', 'mainProfessor', string='Classes')
    timetable_ids = fields.One2many('timetable', 'idProfessor', string='Timetables')
    