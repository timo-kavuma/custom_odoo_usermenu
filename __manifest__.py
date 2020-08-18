##########################Ability User Menu#####################################

{
    'name': "User Menu",
    'version': "1.0",
    'summary': """Odoo Backend Menu""",
    'description': """Custom Menu odoo13""",
    'author': "Timo Kavuma",
    'company': "Ability Software",
    'website': "https://abilitysoft.tech",
    'category': 'Tools',
    'data': [
        'views/menu_views.xml', 
    ],
    'qweb': ["static/src/xml/template.xml"],
    'images': ['static/description/banner.gif'],
    'license': "AGPL-3",
    'installable': True,
    'application': False
}
