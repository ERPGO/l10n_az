# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# Copyright (C) 2021 ERPGO LLC (<http://erpgo.az>).
from odoo import api, SUPERUSER_ID

def post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    
    # Update default journal to use local chart of account as default account id
    bank_journal = env['account.journal'].search([('name','=','Bank')])
    bank_journal['default_account_id'] = env.ref('l10n_az.1_az223')
    
    cash_journal = env['account.journal'].search([('name','=','Cash')])
    cash_journal['default_account_id'] = env.ref('l10n_az.1_az221')
    
    # Delete confusing bank and cash chart of accounts
    accounts = env['account.account'].search(['|',('code','=','2234'),('code','=','2211')])
    accounts.unlink()