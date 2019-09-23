from odoo import models,fields,api


class Course(models.Model):
    _name ='openacademy.person'
    _description = 'This is a course of the Westeros Library.'

    name = fields.Char()

    is_teacher = fields.Boolean()

    sessions_ids = fields.Many2many('openacademy.session')

