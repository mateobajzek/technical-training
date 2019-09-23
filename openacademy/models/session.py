from odoo import models,fields,api


class Course(models.Model):
    _name ='openacademy.session'
    _description = 'This is a course of the Westeros Library.'

    name = fields.Char()

    start_date = fields.Datetime()

    end_date = fields. Datetime()

    course_id = fields.Many2one ('openacademy.course')

    teacher_id = fields.Many2one('openacademy.person')

    atandee_ids = fields.Many2many('openacademy.person')

    room_capacity = fields.Integer()