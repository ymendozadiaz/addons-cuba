# -*- coding: utf-8 -*- 
# Part of Odoo. See LICENSE file for full copyright and licensing details. 
from odoo import api, fields, models 
from datetime import datetime 

class HgmStudiesAnalysis(models.Model): 
    _name = 'hgm.studies.analysis' 
    _inherit = ['mail.thread', 'mail.activity.mixin'] #chatter
    _description = 'HGM Studies analysis'
    _rec_name = 'name_id'


    name_id = fields.Many2one('hgm.igm', string='Patient', required=True, tracking=True) 
    age = fields.Integer(related='name_id.age') 
    area_health = fields.Char(related='name_id.area_health') 
    ftm = fields.Datetime(related='name_id.ftm')
    fsr = fields.Datetime(string='fsr', required=True, tracking=True)
    result = fields.Integer(string='Result', required=True, tracking=True) 
    resultState = fields.Selection([('positive', 'Positive'), 
                             ('negative', 'Negative')], default='negative', tracking=True)
    
    statusBar = fields.Selection([
                            ('new', 'New'),
                            ('draft', 'Draft'), 
                            ('finished', 'finished')], tracking=True)


    def button_draft(self):
        self.statusBar = 'draft'

    def button_finished(self):
        self.statusBar = 'finished'
    
    def button_new(self):
        self.statusBar = 'new' 
    
     
    @api.onchange('result')
    def _onchange_result(self): 
        if self.result != 0:
           self.resultState = 'positive'
        else:
            self.resultState = 'negative'

    



