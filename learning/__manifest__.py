# -*- coding: utf-8 -*-
{
    'name': "learning",
    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'wizard/res_partner_wizard.xml',
        'views/views.xml',
        'report/report_templates.xml',
        'report/report.xml',

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
