# -*- coding: utf-8 -*-
{
    'name': "List Editable Enter - Add",
    'summary': """Created to tackle o2m enter add issues reported here at: https://redmine.kjellberg-erp.de/issues/5061""",
    'description': """
The fix consist on force Odoo o2m fields to add a new record line while editing when pressing enter and focus an 
specific field on the new record""",
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
