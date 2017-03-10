# -*- encoding: utf-8 -*-
from openerp import models, fields, api, exceptions, _

class res_partner(models.Model):
    _name = "res.partner"
    _inherit = "res.partner"
    ico = fields.Char(string='IČ', size=8, help='Identifikační číslo organizace')
    _sql_constraints = [
       ('ico_uniq', 'unique (ico)', 'The IČ of the partner must be unique !')
    ]

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
