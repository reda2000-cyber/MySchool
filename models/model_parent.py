from odoo import models, fields

class parent (models.Model):

    _name="parent"
    _description = 'parent'
    _inherit="person"

    idParent = fields.Char("Parent ID",required=True,select=True)
    address = fields.Text("Address",size=1024,required=True)
    job = fields.Char("Job",required=True)
    phone = fields.Char("Phone Number",required=True)
    eleve_ids = fields.One2many('eleve', 'idParent', string='Children')
    
    