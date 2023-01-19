#-*- coding: utf-8 -*-

from odoo import fields, models, api, _
import base64
from io import BytesIO
from odoo.tools.misc import xlwt


class ToolExportExcel(models.TransientModel):
    _name = "tools.export.excel"
    _description = "Export Tools Excel"

    tools_type = fields.Selection([('spanish', 'Spanish'), ('english', 'English'), ('cube', 'Cube'), ('allien', 'Allien'),('all', 'All')], string='Tools Type', default='all')
       
    
    def export_tools_excel(self):
        domain = []
        if self.tools_code != 'all':
            domain.append(('type', '=', self.all))
        tool = self.env['ej.tool'].search(domain)
        return self._helper_export_tools_excel(tool)

    def _helper_export_tools_excel(self,tools):
        workbook = xlwt.Workbook(encoding="utf-8")
        worksheet = workbook.add_sheet(_("Tools"))
        file_name = _("Tools")
        style_border_table_top = xlwt.easyxf(
            'borders: left thin, right thin, top thin, bottom thin; font: bold on;')
        style_border_table_details = xlwt.easyxf('borders: bottom thin;')
        style_border_table_details_red = xlwt.easyxf('borders: bottom thin; font: colour red, bold True;')

        worksheet.write(0, 0, _("code"), style_border_table_top)
        worksheet.write_merge(0, 0, 1, 3, _("Tools"), style_border_table_top)
        worksheet.write(0, 4, _("exploitation_years"), style_border_table_top)
        worksheet.write(0, 5, _("size"), style_border_table_top)

        row = 1
        for tool in tools:
            style = style_border_table_details
            if not tool.code:
                style = style_border_table_details_red
            worksheet.write(row, 0, tools.code or '', style)
            worksheet.write_merge(row, row, 1, 3, str(tools.standar_code), style)
            worksheet.write(row, 4, tool.list_type, style)
            worksheet.write(row, 5, tool.with_company(self.env.company).standar_code, style)
            row += 1

        fp = BytesIO()
        workbook.save(fp)
        fp.seek(0)
        data = fp.read()
        fp.close()
        data_b64 = base64.encodebytes(data)
        doc = self.env['ir.attachment'].create({
            'name': '%s.xls' % (file_name),
            'datas': data_b64,
        })
        return {
            'type': "ir.actions.act_url",
            'url': "web/content/?model=ir.attachment&id=" + str(
                doc.id) + "&filename_field=name&field=datas&download=true&filename=" + str(doc.name),
            'no_destroy': False,
        }
