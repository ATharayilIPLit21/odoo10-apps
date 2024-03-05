{
    'name': 'Drug Sale Report',
    'version': '10.0',
    'summary': 'Detailed report of drug sale',
    'description': "Detailed report of drug sale",
    'author': 'Akhil',
    'category': 'Hidden',
    'sequence' : 1,
    'depends': ['stock', 'bahmni_product','bahmni_sale'],
    'data': [
        
        'security/ir.model.access.csv',
        'report/drug_sale_view.xml',
        

    ],
    'demo': [],
    'images': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb':[],
}
