# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (C) 2021 ERPGO LLC (<http://erpgo.az>).

{
    'name': 'Azerbaijan - Accounting',
    'version': '1.0',
    'category': 'Accounting/Localizations/Account Charts',
    'summary': """Azerbaijan accounting localization
    """,
    'description': """
This is the latest Accounting localisation aligned for Azerbaijani legislation
    """,
    'author': 'ERPGO LLC',
    'website': 'https://erpgo.az',
    'depends': [
        'account',
        'base_iban',
        'base_vat',
    ],
    'data': [
        'data/l10n_az_chart_data.xml',
        'data/account.account.template.csv',
        'data/account.chart.template.csv',
        'data/account.tax.group.csv',
        'data/account_tax_data.xml',
        'data/account_chart_template_data.xml',
    ],
    'images': ['static/description/icon.png'],
    'license': 'AGPL-3',
    'installable': True,
    'application': True,
    'auto-install': False,
}

