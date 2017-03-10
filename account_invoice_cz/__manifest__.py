# -*- coding: utf-8 -*-

{
    'name': 'Czech invoice',
    'version': '1.0',
    'category': 'Czech accounting',
    'summary': 'Account invoice',
    'description': """
Czech invoice
""",
    'website': 'https://www.odoo.com/',
    'depends': ['sale','account','base_vat'],
    'data': [
#        'security/ir.model.access.csv',
        'views/account_invoice_cz.xml',
    ],
    'demo': [],
}
