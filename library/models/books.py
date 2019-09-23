from odoo import models,fields,api

class Books(models.Model):
    _name = 'library.book'
    _description = 'Book'

    name = fields.Char('Title')

    author_ids = fields.Many2many("library.partner", "Authors")
   
    year_of_edition = fields.Date()
   
    isbn = fields.Char('ISBN')
   
    publisher_id = fields.Many2one('library.partner','Publisher')

    rental_ids = fields.One2many('library.rental', 'book_id','Rentals')