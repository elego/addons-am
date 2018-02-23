# -*- coding: utf-8 -*-
{
    'name': "Fix One-to-Many Onchange",
    'summary': """Created to tackle onchange issues reported here at: https://redmine.kjellberg-erp.de/issues/5346""",
    'description': """
The fix consist on disconnect the code executed on the save event of o2m fields also triggered on the dataset write 
function duplicating the trigger of the o2m field onchange due to that the save event was used for create and write 
operations, write it's covered by the dataset, so the trigger for create was moved to the dataset and a new event 
bind is registered for the fields to match the new event, so now the save event doesn't trigger anything by itself, 
the dataset create and write functions are the responsible for trigger the o2m field onchange for the parent form""",
    'author': "Axel Mendoza",
    'email': 'aekroft@gmail.com',
    'license': "AGPL-3",
    'website': "https://www.aekroft.com",
    'category': 'web',
    'version': '8.0',
    'depends': ['base', 'web',],
    'data': [
        'views.xml'
    ],
}
