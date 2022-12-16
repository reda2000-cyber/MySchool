from odoo import models, fields
from datetime import datetime,timedelta


class speciality (models.Model):

    _name="speciality"
    _description = 'speciality'

    idSpeciality = fields.Char("Speciality ID",required=True,select=True)
    name = fields.Char("Label",size=255,required=True)
    professor_ids = fields.One2many('professor', 'speciality', string='Professors')