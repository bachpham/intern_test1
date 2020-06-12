from odoo import fields, models, api
import re


class SaleOder(models.Model):
    _inherit = 'sale.order'
    _description = 'Sale Order Inherit'

    discount_estimated = fields.Monetary(string='Estimated Discount Total', readonly=True, store=True,
                                         compute='estimate_discount_total')
    customer_discount_code = fields.Text(string="Customer Discount Code", related='partner_id.customer_discount_code')

    @api.depends('amount_total', 'partner_id', 'customer_discount_code')
    def estimate_discount_total(self):
        for rec in self:
            if rec.valid_code:
                discount_code = self.customer_discount_code.split('_')
                discount_vals = int(discount_code[1])
                rec.discount_estimated = rec.amount_total * (100 - discount_vals) / 100
            else:
                rec.discount_estimated = rec.amount_total
                

class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'Res Partner Inherit'

    customer_discount_code = fields.Text(string="Customer Code")

