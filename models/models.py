from odoo import fields, models, api
import re


class SaleOder(models.Model):
    _inherit = 'sale.order'
    _description = 'Sale Order Inherit'

    customer_discount_code = fields.Text(string="Customer Discount Code", related='partner_id.customer_discount_code')


class ResPartner(models.Model):
    _inherit = 'res.partner'
    _description = 'Res Partner Inherit'

    customer_discount_code = fields.Text(string="Customer Code")

