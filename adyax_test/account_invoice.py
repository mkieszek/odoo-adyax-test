# -*- coding: utf-8 -*-
'''
Created on 17 paź 2014

@author: mbereda
'''
from openerp.osv import fields,osv
import pdb

#point 6.2
class account_invoice(osv.osv):
    _inherit = "account.invoice"
    
    _columns = {
        'new_model_id': fields.many2one('new.model', 'New model', domain="[('partner_id','=',partner_id)]"),
        }
    