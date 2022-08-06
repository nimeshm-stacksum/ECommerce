from importlib.util import set_loader
from odoo import models, fields, api, _
from odoo.tools.misc import parse_date

class CreateOrder(models.TransientModel):
    _name = 'create.order.wizard'
    _description = 'Create Appoinment Wizard'

    client_id = fields.Many2one('ecommerce.client', string="Client")
    order_date = fields.Date(string="Order Date")

    def action_create_order(self):
        pass
        # vals = {
        #     'client_id' : self.client_id.id,
        #     'product_id' : 2,
        #     'order_date' :  self.order_date
        # }
        # order_rec= self.env['ecommerce.order'].create(vals)
        # return {
        #     'name' : _('Order'),
        #     'type' : 'ir.actions.act_window',
        #     'view_mode' : 'form',
        #     'res_model' : 'ecommerce.order',
        #     'res_id' : order_rec.id
        # }