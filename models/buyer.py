from odoo import models, fields, api, _

class EcommerceBuyer(models.Model):
    _name = 'ecommerce.buyer'
    _description = 'Buyer'
    # _inherit = ['mail.thread', 'mail.activity.mixin']

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
            vals['name']= self.env['ir.sequence'].next_by_code('ecommerce.buyer') or _('New')
        result = super(EcommerceBuyer, self).create(vals)
        return result

    def _get_defalut_note(self):
        return "Hello, I am default note please you can edit me!"

    name = fields.Char(string="Buyer ID", required=True, copy=False, readonly=True, index=True, default=lambda self: _('New'))
    client_id = fields.Many2one('ecommerce.client', string='Client', required=True)
    client_age = fields.Integer('Age', related='client_id.client_age')
    notes = fields.Text(string='Registration Note', default=_get_defalut_note)
    product_detail = fields.Text(string='Note')
    pharmacy = fields.Text(string='Note')
    buyer_date = fields.Date(string='Date', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('pending', 'Pending'),
        ('done', 'Done'),
        ('cancel', 'Cancelled')
        ], string='Status', readonly=True, default='draft', tracking=True)

    def action_pending(self):
        self.state = 'pending'

    def action_done(self):
        self.state = 'done'

    def action_cancel(self):
        self.state = 'cancel'