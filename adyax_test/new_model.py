# -*- coding: utf-8 -*-
'''
Created on 17 paź 2014

@author: sony
'''
from openerp.osv import fields,osv
import pdb

#point 1.
class new_model(osv.Model):
    _description = "New model"
    _name = "new.model"
    
    #point 1.3
    def _get_sum_value(self, cr, uid, ids, name, arg, context = None):
        vals = {}
        
        for obj in self.browse(cr, uid, ids):
            sum_value = 0.0
            related_model_ids = self.search(cr, uid, [('partner_id','=', obj.partner_id.id)])
            for related_model in self.browse(cr, uid, related_model_ids):
                sum_value += related_model.numeric_value
                
            vals[obj.id] = sum_value
        return vals
     
     
    _columns = {
        'numeric_value': fields.float('Numeric value', ), #point 1.1
        'partner_id': fields.many2one('res.partner', 'Partner', required=True), #point 1.2
        'sum_value': fields.function(_get_sum_value, type="float", string="Sum value"), #point 1.3
        'date':  fields.date('Date', required=True) #point 1.4
         }
    
    #point 2
    _sql_constraints = [('model_unique','unique(partner_id,date)','This model already exists.')]
    
    def name_get(self, cr, uid, ids, context=None):
        """Overrides orm name_get method"""
        if not isinstance(ids, list) :
            ids = [ids]
        res = []
        if not ids:
            return res
        
        reads = self.read(cr, uid, ids, ['partner_id', 'date'], context)
        for record in reads:
            partner = record['partner_id'][1]
            date = record['date']
            res.append((record['id'], partner + ' - ' + date))
        return res