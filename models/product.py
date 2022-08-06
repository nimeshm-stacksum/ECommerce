from odoo import models, fields, api, _

class EcommerceProduct(models.Model):
    _name = 'ecommerce.product'
    _description = 'Product'
    _rec_name = 'product_name'

    product_name = fields.Char(string='Product Name')
    product_company = fields.Char(string='Company Name')
    product_price = fields.Integer(string='Price')