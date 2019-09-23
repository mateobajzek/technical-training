# -*- coding: utf-8 -*-
from odoo import fields, models,api
from odoo.exceptions import ValidationError, Warning


class Course(models.Model):
    _name = 'openacademy.course'
    _description = 'Course'

    name = fields.Char(string='Title', required=True)
    description = fields.Text()

    responsible_id = fields.Many2one('openacademy.partner', string="Responsible")
    session_ids = fields.One2many('openacademy.session', 'course_id', string="Sessions")

    level = fields.Selection([(1, 'Easy'), (2, 'Medium'), (3, 'Hard')], string="Difficulty Level")


class Session(models.Model):
    _name = 'openacademy.session'
    _description = 'Session'

    name = fields.Char(required=True)
    active = fields.Boolean(default=True)
    state = fields.Selection([('draft', "Draft"), ('confirmed', "Confirmed"), ('done', "Done")], default='draft')

    start_date = fields.Date(default=fields.Date.context_today)
    duration = fields.Float(digits=(6, 2), help="Duration in days", default=1)

    instructor_id = fields.Many2one('openacademy.partner', string="Instructor")
    course_id = fields.Many2one('openacademy.course', ondelete='cascade', string="Course", required=True)
    attendee_ids = fields.Many2many('openacademy.partner', string="Attendees")


    capacity = fields.Integer()
    number_attandees = fields.Integer(compute="get_number_attendees", store=True)

    _sql_constraints =[
        ('check_num_capacity','CHECK(capacity>= number_attendees)','Too much ateeendes for room capacity! SQL')
    ]

    @api.constrains('attendee_ids','capacity')
    def check_num_capacity(self):
        for rec in self:
            if rec.capacity < rec.number_attendees:
                raise Warning('Too much attendees for room capacity!')

    @api.depends('attendee_ids')
    def get_number_attendees(self):
        for rec in self:
            rec.number_attendees = len(rec.attendee_ids)


    # @api.onchange('attende_ids','capacity')
    # def ohchange_check_num_capacity(self):
    #    if self.capacity <number_attendees:
    #       self.attende_ids = self.attende_ids[:self.capacity]
    #       raise Warning('Too much atendees for room capacity!')

    
 
      