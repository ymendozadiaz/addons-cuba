# -*- coding: utf-8 -*- 
# Part of Odoo. See LICENSE file for full copyright and licensing details. 
from odoo import api, fields, models, _
from datetime import datetime 

class HgmIgm(models.Model): 
    _name = 'hgm.igm'
    _inherit = ['mail.thread', 'mail.activity.mixin'] #chatter
    _description = 'HGM IGM'
    _rec_name = 'name'


    name = fields.Char(string='name', tracking=True, required=True) 
    age = fields.Integer(string='age', tracking=True, required=True) 
    address = fields.Char(string='address', tracking=True, required=True) 
    symptoms = fields.Char(string='symptoms', tracking=True) 
    fis = fields.Datetime(string='fis', tracking=True, required=True)  
    ftm = fields.Datetime(string='ftm', tracking=True, required=True)  
    fever = fields.Boolean(string='fever', tracking=True)  
    migraine = fields.Boolean(string='migraine', tracking=True)  
    rash = fields.Boolean(string='rash', tracking=True)  
    pain_retrocular = fields.Boolean(string='pain_retrocular', tracking=True)  
    uneasiness_gral = fields.Boolean(string='uneasiness_gral', tracking=True)  
    area_health = fields.Char(string='area_health', tracking=True, required=True) 
    analysis_count = fields.Integer(compute='_compute_analysis_count', string='analysis Count') #campo calculado
    statusBar = fields.Selection([
                            ('draft', 'Draft'), 
                            ('finished', 'finished')], default='draft', tracking=True)

    def button_draft(self):
        self.statusBar = 'draft'

    def button_finished(self):
        self.statusBar = 'finished' 
                   

# defiendo la función del campo computado 
    def _compute_analysis_count(self):     
        analysis_count = self.env['hgm.studies.analysis'].search_count([('name_id', '=', self.id)])
        self.analysis_count = analysis_count   

# defiendo la accion del smart button
    def action_open_studies_analysis(self):
        return {
            'type': 'ir.actions.act_window',
            'name': 'Studies Analysis',
            'res_model': 'hgm.studies.analysis',
            'domain': [('name_id', '=', self.id)],
            'view_mode': 'tree,form',
            'target': 'current',

        }