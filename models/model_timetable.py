from odoo import models, fields
from datetime import datetime,timedelta


class timetable (models.Model) :

    _name="timetable"
    _description = 'timetable'

    idTimetable = fields.Char("ID Timetable",required=True,select=True)
    fromm = fields.Datetime("From",required=True)
    to = fields.Datetime("To",required=True)
    name = fields.Char("Label",required=True)
    exceptional = fields.Boolean("Exeptional ?")
    idModule = fields.Many2one('module','Module',ondelete='cascade',required=True)
    idProfessor = fields.Many2one('professor','Professor',ondelete='cascade',required=True)
    idRoom = fields.Many2one('room','Room',ondelete='cascade',required=True)