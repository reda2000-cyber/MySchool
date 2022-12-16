from odoo import models, fields
from datetime import datetime,timedelta


class person (models.Model):

    _name="person"
    _description = 'person'

    GENDER_TYPE_SELECTION = [
        ('male', 'Male'),
        ('female', 'Female')
    ]

    firstname = fields.Char("First Name",size=255,required=True)
    lastname = fields.Char("Last Name",size=255,required=True)
    dateofbirth = fields.Date("Date of Birth",required=True)
    cityofbirth = fields.Char("City of Birth",required=True)
    email = fields.Char("Email",size=1024,required=True)
    photo = fields.Binary('Picture',filters='*.png,*.jpeg,*.jpg',attachment=True)
    gender = fields.Selection(GENDER_TYPE_SELECTION, 'Gender',required=True)
    