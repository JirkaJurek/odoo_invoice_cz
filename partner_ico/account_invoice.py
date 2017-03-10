
# -*- encoding: utf-8 -*-

from openerp import models, fields, api, exceptions, _
import time


class account_invoice(models.Model):
    _name = "account.invoice"
    _inherit = "account.invoice"
    def _default_date_zdpl(self):
        return time.strftime('%Y-%m-%d')
    date_zdpl = fields.Date(string='Datum ZDPL', readonly=True, states={'draft':[('readonly',False)]}, select=True, help="Datum uskutečnění zdanitelného plnění", default=_default_date_zdpl)

