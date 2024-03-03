{
    'name': 'Hospital Management System',
    'version': '1.0',
    'category': 'Health',
    'summary': 'Manage hospital patient records',
    'author': 'Ramy Medhat',
    'website': '',
    'depends': ['base'],
    'data': [
        'views/hms_action_views.xml',
        'views/hms_menu_views.xml',
        'security/ir.model.access.csv',
        'views/hms_patient_views.xml',
        'views/hms_doctor_views.xml',
        'views/hms_department_views.xml',
    ],

    'application': True,
}
