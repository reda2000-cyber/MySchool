from odoo import models, fields

class complaints (models.Model):

    _name="complaints"
    _description = 'complaints'
   
    Idcomplaints = fields.Char("Complaints ID")
    idProfessor = fields.Many2one('professor', 'Professor', ondelete='cascade')
    idEleve = fields.Many2one('eleve', 'Eleve', ondelete='cascade')
    subject = fields.Char("Subject",size=255)
    body = fields.Text("Body")