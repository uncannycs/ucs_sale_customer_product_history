# -*- coding: utf-8 -*-
{
    'name': "Sales History Of Products",
    'version': '19.0.1.0.0',
    'summary': """User can view The Sales history of The 
    products from Sales Order Line""",
    'description': """Sales history of products from Sales Order Line""",
    'author': "Uncanny Consulting Services LLP",
    'company': "Uncanny Consulting Services LLP",
    'maintainer': 'Uncanny Consulting Services LLP',
    'website': "https://www.uncannycs.com",
    'category': 'Sales/Sales',
    'depends': ['sale_management'],
    'data': [
        'security/ir.model.access.csv',
        'wizard/product_sale_order_history_wizard_views.xml',
        'wizard/stock_picking_wizard.xml',
        'views/sale_order_views.xml',
    ],
    'license': 'AGPL-3',
    'images': ['static/description/banner.gif'],
    'installable': True,
    'auto_install': False,
    "price": 25,
    "currency": "USD"
}
