from odoo import fields, models


class Rentals(models.Model):
    _name = 'library.rental'
    _description = 'Book rental'

    customer_id = fields.Many2one('library.partner', 'Customer')
    book_id = fields.Many2one('library.book', 'Book')

    rental_date = fields.Date()
    return_date = fields.Date()
    
