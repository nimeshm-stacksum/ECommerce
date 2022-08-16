from attr import field
from odoo import models, fields, api, _

class EcommerceOrder(models.Model):
    _name = 'ecommerce.order'
    _description = 'Order'

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name']= self.env['ir.sequence'].next_by_code('ecommerce.order') or _('New')
        result = super(EcommerceOrder, self).create(vals)
        return result

    def _get_defalut_note(self):
        return "Hello, I am default note please you can edit me!"

    name = fields.Char(string="Order ID", required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
    client_id = fields.Many2one('ecommerce.client', string='Client Name', required=True)
    client_age = fields.Integer('Age', related='client_id.client_age')
    client_phone = fields.Char('Phone No.', related='client_id.client_phone')
    product_id = fields.Many2one('ecommerce.product', string='Product', required=True)
    notes = fields.Text(string='Registration Note', default=_get_defalut_note)
    order_lines = fields.One2many('ecommerce.order.lines', 'order_id', string="Order Lines")
    product_detail = fields.Text(string='Note')
    extra_service = fields.Text(string='Note')
    order_date = fields.Date(string='Date', required=True)
    state = fields.Selection([
        ('cart', 'Cart'),
        ('delivered', 'Delivered'),
        ('cancel', 'Cancelled')
        ], string='Status', readonly=True, default='cart', tracking=True)

    def action_Delivered(self):
        self.state = 'delivered'

    def action_cancel(self):
        self.state = 'cancel'

class EcommerceOrderLines(models.Model):
    _name = 'ecommerce.order.lines'
    _description = 'Order Lines'

    product_id = fields.Many2one('product.product', string="Product")
    product_qty = fields.Integer(string="Quantity")
    order_id = fields.Many2one('ecommerce.order', string="Order ID")