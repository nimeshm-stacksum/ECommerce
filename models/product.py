from odoo import models, fields, api, _

class EcommerceProduct(models.Model):
    _name = 'ecommerce.product'
    _description = 'Buyer'

    product_name = fields.Char(string="Buyer ID", required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))