from odoo import models, fields

class eleve (models.Model):

    _name="eleve"
    _description = 'eleve'
    _inherit="person"
   
    idEleve = fields.Char("Eleve ID",required=True,select=True)
    cne = fields.Char("CNE",size=10,required=True,select=True)
    state = fields.Selection([
			('studying','Studying'),
			('studying_adjourned','Adjourned'),
            ('graduated', 'Graduated'),
            ('excluded','Excluded')
        ],'state',readonly=True)

    idParent = fields.Many2one('parent','Parent',ondelete='cascade',required=True)
    inscription_ids = fields.One2many('inscription', 'idEleve', string='Inscriptions')
    Idcomplaints = fields.One2many('complaints', 'idEleve', string='Compaints')