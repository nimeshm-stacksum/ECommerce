{
    'name': "Odoo Ecommerce",
    'version': '12.0.1.0.0',
    'category':'Extra Tools',
    'summary':'Module for E-Commerce',
    # 'sequence':'AGPL-3',
    'author':'Stack Summation',
    'maintainer':'Stack Summation',
    'website':'https://www.google.com/',
    'depends':['sale'],
    'demo':[],
    'data':[
        'views/client.xml',
        'views/buyer.xml',
        'security/ir.model.access.csv',
        'data/sequence.xml',
        'reports/reports.xml',
        'reports/client_card.xml'
    ],
    'installable':True,
    'application':True,
    'auto_install':False,
}
