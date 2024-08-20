
# -*- coding: utf-8 -*-
{
    'name': "Auto Process",

    'summary': "Maded a auto process button to automated all the action of the sale.order module and same as in  purchase.order module ",

    'description': """
in odoo sale.order i have maded a button named auto process when its is 
clicked than the sale order is confirmed,validate delivery order, create invoice
,validate invoice, register payment this all will be done on the click of the auto process button.

As same is done on the purchase Module 

    """,

    'author': "My Company",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '17.0',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management', 'account', 'sale', 'purchase', 'stock', 'product'],

    # always loaded
    'data': [

        'views/purchase_order_views.xml',
        'views/sale_order_views.xml',


    ],
    'installable': True,
    'application': True,
}
