##############################################################################
{
    'name': 'igm MFH',
    'version': '16.0.0.1.0',
    'author': "Yosbel Mendoza Díaz",
    'maintainer': "Yosbel Mendoza Díaz",
    'license': 'AGPL-3',
    'category': 'account.payment',
    'summary': 'Ejemplo de un módulo by Yosbel.',
    'depends': ['base','stock', 'mail'],
    'description': """
Módulo basado en la versión 16 de odoo
===================================================== 
como ejemplo  
""",
    'demo': [],
    'test': [],
    'data': [
    'security/ir.model.access.csv',
    'wizard/analysis_export_excel_wzd.xml',
    'views/igm_view.xml',
    'views/igm_studies_view.xml'    
    ],
    'installable': True,
    'application': True,
    'auto_install': False,
    'sequence': -150
}
