#-*- coding: utf-8 -*-

from odoo import fields, models, api, _
import base64
from io import BytesIO
from odoo.tools.misc import xlwt


class AnalysisExportExcel(models.TransientModel):
    _name = "analysis.export.excel"
    _description = "Export Analysis Excel"

    analysis_type = fields.Selection([('name', 'Name'), ('age', 'Age'), ('area_health', 'Area_health'),('all','All')], string='Analysis Type', default='all')

    def export_analysis_excel(self):
        domain = []
        if self.analysis_type != 'all':
            domain.append(('name', '=', self.analysis_type))
        Analysisand = self.env['hgm.igm'].search(domain)
        return self._helper_export_analysis_excel(Analysisand)

    def _helper_export_analysis_excel(self,analysisand):
        workbook = xlwt.Workbook(encoding="utf-8")
        worksheet = workbook.add_sheet(_("Analysis"))
        file_name = _("Analysis")
        style_border_table_top = xlwt.easyxf(
            'borders: left thin, right thin, top thin, bottom thin; font: bold on;')
        style_border_table_details = xlwt.easyxf('borders: bottom thin;')
        style_border_table_details_red = xlwt.easyxf('borders: bottom thin; font: colour red, bold True;')

        worksheet.write(0, 0, _("Code"), style_border_table_top)
        worksheet.write_merge(0, 0, 1, 1, _("Analysis"), style_border_table_top)
        worksheet.write(0, 2, _("Name"), style_border_table_top)
        worksheet.write(0, 3, _("Address"), style_border_table_top)

        # row = 1
        # for analysis in analysisand:
        #     style = style_border_table_details
        #     if not name.default_code:
        #         style = style_border_table_details_red
        #     worksheet.write(row, 0, name.default_code or '', style)
        #     worksheet.write_merge(row, row, 1, 3, str(analysis.name), style)
        #     worksheet.write(row, 2, analysis.list_name, style)
        #     worksheet.write(row, 3, analysis.with_company(self.env.company).standard_name, style)
        #     row += 1

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
