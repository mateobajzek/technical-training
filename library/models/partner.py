from odoo import models,fields,api


class Partner(models.Model):
    _name = 'library.partner'
    _description = 'Partner'

    name = fields.Char()
    email = fields.Char()
    address = fields.Char()
    
    partner_type = fields.Selection ([('customer', 'Customer'), ('author', 'Author')]) 
    
    rental_ids = fields.One2many('library.rental', 'customer_id','Rentals')