# -*- coding: utf-8 -*-
'''
Created on 17 paź 2014

@author: mbereda
'''

from openerp.osv import fields, osv
from openerp.addons.mail.mail_message import decode
import datetime

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO
    
import csv
import pdb
import base64

class import_new_model(osv.osv_memory):
    _name = 'import.new.model'
    _description = 'Import new model'

    _columns = {
        'import_file' : fields.binary('File to import', required=True),
        'filename' : fields.char('File name', size=255),
        }
    
    def import_new_model(self, cr, uid, ids, context=None):
        new_model_obj = self.pool.get('new.model')
        partner_obj = self.pool.get('res.partner')
        w = self.browse(cr, uid, ids)[0]
        
        csvfile = StringIO(base64.b64decode(w.import_file))
        
        while 1:
            row = csvfile.readline()
            row = row.replace('\r\n', '')
            row_tab = row.split(";") 
            if not row:
                break
            
            num_value = float(row_tab[0]) if row_tab[0] != '' else 0.0
            partner_id = partner_obj.search(cr, uid, [('name','=',row_tab[1])])
            if not partner_id :
                return True
            date = datetime.datetime.strptime(row_tab[2], '%Y.%m.%d').date() if row_tab != '' else False
            model_ids = new_model_obj.search(cr, uid, [('partner_id','=',partner_id[0]),('date','=',date)])
            
            if not model_ids:
                vals = {}
                vals = {
                        'partner_id': partner_id[0],
                        'numeric_value': num_value,
                        'date': date or False,
                        }
                new_model_obj.create(cr, uid, vals)
            else:
                new_model_obj.write(cr, uid, model_ids, {'numeric_value': num_value})
        
        return True