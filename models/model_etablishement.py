from odoo import models, fields

class etablishement (models.Model):

    _name="etablishement"
    _description = 'etablishement'

    idEtablishement = fields. Integer("Etablishement ID",required=True,select=True)
    name = fields.Char("Label",size=255,required=True)
    maxStudentTotal = fields.Integer("Max Student Total",required=True)
    maxStudentPerClass = fields.Integer("Max Student per class" ,required=True)
    scholaryear_ids = fields.One2many('scholaryear', 'idEtablishement', string='Scholar Years')
    room_ids = fields.One2many('room', 'idEtablishement', string='Rooms')