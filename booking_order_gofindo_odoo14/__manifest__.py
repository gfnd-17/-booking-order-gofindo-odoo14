{
    'name': "Booking Order",
    'author': "My Company",
    'website': "http://www.yourcompany.com",

    'category': 'Sales',
    'version': '0.1',
    'application': True,
    'installable': True,

    'depends': [
        'base', 
        'mail', 
        'sale', 
        'sales_team'
    ],

    'data': [
        'data/data.xml',
        'views/menu_item.xml',
        'views/sale_order.xml',
        'views/service_team.xml',
        'views/work_order.xml',
        'wizard/cancel_state.xml',
        'report/work_order_report.xml',
    ],

}
