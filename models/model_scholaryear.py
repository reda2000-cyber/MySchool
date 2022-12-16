from odoo import models, fields
from datetime import datetime,timedelta


class scholaryear (models.Model):

    _name="scholaryear"
    _description = 'scholaryear'

    idScholarYear = fields.Char("Scholar Year",size=9,required=True,select=True)
    name = fields.Char("Label",required=True)
    startDate = fields.Date("Start Date",required=True)
    endDate = fields.Date("Ending Date",required=True)
    idEtablishement = fields.Many2one('etablishement','Etablishement',ondelete='cascade')
    class_ids = fields.One2many('class', 'idScholarYear', string='Classes')
    holiday_ids = fields.One2many('holiday', 'idScholarYear', string='Holidays')