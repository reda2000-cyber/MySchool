from odoo import models, fields

class course (models.Model):

    _name="course"
    _description = 'course'
   
    idModule = fields.Many2one('module','Module',ondelete='cascade',required=True)
    name = fields.Char('Title',required=True)
    videoLink = fields.Char('Video Link')
    content = fields.Text('Content',required=True)
    attachement = fields.Binary('Attachement')