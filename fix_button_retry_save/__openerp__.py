# -*- coding: utf-8 -*-
{
    'name': "Fix Button Retry Save",
    'summary': """Created to tackle form save issues reported here at: https://redmine.kjellberg-erp.de/issues/5348""",
    'description': """
The fix consist on clean dirty fields on form save to prevent that simultaneous save calls triggered by others actions
like buttons click for print get o2m record lines get duplicated on write
    """,
    'author': "Axel Mendoza",
    'email': 'aekroft@gmail.com',
    'license': "AGPL-3",
    'website': "https://www.aekroft.com",
    'category': 'web',
    'version': '8.0',
    'depends': ['base', 'web'],
    'data': [
        'views.xml'
    ],
}
