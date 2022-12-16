from odoo import models, fields
from datetime import datetime,timedelta


class room (models.Model):

    _name="room"
    _description = 'room'

    idRoom = fields.Char("ID Room")
    room = fields.Integer("Room Number",required=True,select=True)
    name = fields.Char("Label",size=255)
    timetable_ids = fields.One2many('timetable', 'idRoom', string='Timetables')
    exam_ids = fields.One2many('exam', 'idRoom', string='Timetables')
    idEtablishement = fields.Many2one('etablishement','Etablishement',ondelete='cascade',required=True)