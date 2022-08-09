from multiprocessing import context
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class ResPartners(models.Model):
    _inherit = 'res.partner'

    @api.model
    def create(self, vals_list):
        res = super(ResPartners, self).create(vals_list)
        return res

class SaleOrderInherit(models.Model):
    _inherit = 'sale.order'

    client_name = fields.Char(string='Client Name')

class Client(models.Model):
    _name = 'ecommerce.client'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = 'Client Record'
    _rec_name = 'client_name'

    @api.constrains('client_age')
    def check_age(self):
        for rec in self:
            if rec.client_age:
                if rec.client_age <= 5:
                    raise ValidationError(_('The Age must be Greater than 5'))

    def open_client_order(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Order',
            'res_model': 'ecommerce.order',
            'domain':[('client_id', '=', self.id)],
            'context': {'default_client_id':self.id},
            'view_mode': 'tree,form',
            'target':'current',            
        }

    # Send Mail using Mail Template
    def send_client_card(self):
        template_id = self.env.ref('E-Commerce.client_card_email_template').id
        template = self.env['mail.template'].browse(template_id)
        template.send_mail(self.id, force_send=True)

    def get_order_count(self):
        count = self.env['ecommerce.order'].search_count([('client_id', '=', self.id)])
        self.order_count = count

    name = fields.Char(string='Test Field')
    name_seq =  fields.Char(string='Client ID', required=True, copy=False, readonly=True, index=True, default=lambda self:_('New'))

    client_name = fields.Char(string='Name', track_visibility="always")
    client_age = fields.Integer(string='Age', track_visibility="always")
    client_phone = fields.Char(string='Phone No.', track_visibility="always")
    notes = fields.Text(string='Notes')
    image = fields.Char(string='Image')
    order_count = fields.Integer(string='Order', compute='get_order_count')
    active = fields.Boolean("Active", default=True)
    user_id = fields.Many2one('res.users', string="PRO")
    email = fields.Char(string="Email")
    # product_id = fields.Many2one('ecommerce.product', string='Product')

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq']= self.env['ir.sequence'].next_by_code('ecommerce.client.sequence') or _('New')
        result = super(Client, self).create(vals)
        return result

    def test_name(self):
        pass