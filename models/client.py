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

    def open_client_buyer(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Buyer',
            'res_model': 'ecommerce.buyer',
            'domain':[('client_id', '=', self.id)],
            'context': {'default_client_id':self.id},
            'view_mode': 'tree,form',
            'target':'current',            
        }

    def get_buyer_count(self):
        count = self.env['ecommerce.buyer'].search_count([('client_id', '=', self.id)])
        self.buyer_count = count

    name = fields.Char(string='Test')
    name_seq =  fields.Char(string='Client ID', required=True, copy=False, readonly=True, index=True, default=lambda self:_('New'))

    client_name = fields.Char(string='Name', track_visibility="always")
    client_age = fields.Integer(string='Age', track_visibility="always")
    notes = fields.Text(string='Notes')
    image = fields.Char(string='Image')
    buyer_count = fields.Integer(string='Buyer', compute='get_buyer_count')
    active= fields.Boolean("Active", default=True)

    @api.model
    def create(self, vals):
        if vals.get('name_seq', _('New')) == _('New'):
            vals['name_seq']= self.env['ir.sequence'].next_by_code('ecommerce.client.sequence') or _('New')
        result = super(Client, self).create(vals)
        return result