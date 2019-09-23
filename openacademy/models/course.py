from odoo import models,fields,api


class Course(models.Model):
    _name ='openacademy.course'
    _description = 'This is a course of the Westeros Library.'

    name = fields.Char()

    description= fields.Text()

    level = fields.Selection([('1','First Grade'), ('2', 'Second Grade'),('3','Third Grade')])

    responsible_id = fields.Many2one('openacademy.person')

    sessions_ids = fields.One2many('openacademy.session', 'course_id')



