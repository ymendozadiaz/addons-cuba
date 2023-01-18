# -*- coding: utf-8 -*- 
# Part of Odoo. See LICENSE file for full copyright and licensing details. 
from odoo import api, fields, models, _
from datetime import datetime 

class Tools(models.Model): 
    _name = 'ej.tool' 
    _description = 'Tool'
    
    user = fields.Char(string='User', required=True) 

    code = fields.Char(string='code', default='New', readonly=1)
 
    exploitation_years = fields.Integer(string='exploitation_years', required=True) 
 
    size = fields.Char(string='size', required=True) 
 
    type = fields.Selection([('spanish', 'Spanish'),
                             ('english', 'English'),
                             ('cube', 'Cube'),
                             ('allien', 'Allien')], string='type', default="spanish", required=True)

    format = fields.Selection([('csv', 'Csv'), ('xls', 'Excel')], string='Type', required=True)
    tool_count = fields.Integer(string='Tools Count', compute='_compute_tool_count')

    
    @api.model
    def create(self, vals):
        if vals.get('code', "New") == "New":
            vals['code'] = self.env['ir.sequence'].next_by_code(
                'ej.tool') or "New"
        tool = super(Tools, self).create(vals)
        return tool

    def _compute_tool_count(self):
        for rec in self:
            print("rec.......", rec)
            tool_count = self.env['ej.tool'].search_count([('code', '=', rec.code)])
            print("t--------", rec.code)
            rec.tool_count = tool_count
            print("w--------", rec.tool_count)

    def action_import(self):
        if self.type == 'csv':
            self.import_csv()
        else:
            self.import_xls()
        self.imported = True
        return True

    @api.model
    def validate_extesion_file(self, filename):
        name = os.path.splitext(filename)[1]
        return (True, name) if name in ['.csv'] else False

    @api.model
    def validate_extesion_file_excel(self, filename):
        name = os.path.splitext(filename)[1]
        return (True, name) if name in ['.xls','.xlsx'] else False

    def import_csv(self):
        if not self.validate_extesion_file(self.file_name):
            raise UserError(_("File should be CSV extension"))
        file_path = tempfile.gettempdir() + '/file.csv'
        data = self.file
        f = open(file_path, 'wb')
        f.write(base64.b64decode(data))
        f.close()
        archive = csv.DictReader(open(file_path))
        toolObj = self.env['tool.template']

        for line in archive:
            tool_name = line.get('tool')
            tool_code = line.get('Code')
            tool_type = line.get('type')
            cost = line.get('Cost')
            toolObj.create({
                'name': tool_name,
                'default_code': tool_code,
                'list_type': tool_type,
                'type': 'tool',
            })

    def import_xls(self):
        if not self.validate_extesion_file_excel(self.file_name):
            raise UserError(_("File should be Excel extension"))

        toolObj = self.env['tool.template']
        data = base64.b64decode(self.file)
        work_book = xlrd.open_workbook(file_contents=data)
        sheet = work_book.sheet_by_index(0)
        first_row = []

        for col in range(sheet.ncols):
            first_row.append(sheet.cell_value(0, col))

        cont = 0
        for count, row in enumerate(range(1, sheet.nrows), 2):
            try:
                val = {}
                cont += 1
                for col in range(sheet.ncols):
                    val[first_row[col]] = sheet.cell_value(row, col)
                code = str(val.get('Code').strip())
                type = float(val.get('type', 0))
                cost = float(val.get('Cost', 0))
                tool_name = val.get('tool', '')
                toolObj.create({
                    'name': tool_name,
                    'default_code': code,
                    'list_type': type,
                    'type': 'tool',
                })
            except:
                raise UserError(_("There is an error in line" % (cont + 1)))