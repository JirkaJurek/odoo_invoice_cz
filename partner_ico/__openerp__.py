# -*- coding: utf-8 -*-
{   'name': 'Czech - ICO',
    'version': '0.4',
    'category': 'Localization',
    'description': """
This is the module to manage the "IČO" and "datum zdanitelného plňění" for Czech in OpenERP.
    """,
    'author': 'Jirka Jurek',
    'depends': [
        'account',
        'base_vat',
    ],
    'init_xml': [],
    'update_xml': [
        'account_invoice_view.xml',
        'partner_view.xml',
    ],
    'demo_xml': [],
    'installable': True,
    'certificate': '',
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
