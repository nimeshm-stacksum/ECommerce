from odoo import models, fields, api, _

class CreateOrder(models.TransientModel):
    _name = 'create.order'
    _description = 'Create Appoinment Wizard'

    client_id = fields.Many2one('ecommerce.client', string="Client")
    order_date = fields.Date(string="Order Date")
    product_id = fields.Many2one('ecommerce.product', string='Product')

    def action_create_order(self):
        val = {
            'client_id': self.client_id.id,
            'order_date':  self.order_date,
            'product_id': self.product_id
        }
        self.env['ecommerce.order'].create(val)