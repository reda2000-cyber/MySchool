from odoo import models, fields
from datetime import datetime,timedelta

class holiday (models.Model):

    _name="holiday"
    _description = 'holiday'

    fromm = fields.Date("From",required=True)
    to = fields.Date("To",required=True)
    name = fields.Char("Label",required=True)
    idScholarYear = fields.Many2one('scholaryear','Scholar Year',ondelete='cascade',required=True)