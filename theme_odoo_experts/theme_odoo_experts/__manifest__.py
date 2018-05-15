{
    'name': 'Lannex Experts Odoo Theme',
    'description': 'A new look and feel for Lannex It solutions Theme',
    'category': 'Theme/Corporate',
    'sequence': 210,
    'version': '1.0',
    'author': 'Odoo SA',
    'depends': ['theme_loftspace', 'website_animate', 'snippet_google_map'],
    'data': [
        'views/assets.xml',
        'views/images.xml',
        'views/preset.xml',
        'views/layout.xml',
        'views/snippets.xml',
    ],
    'demo': [
        'demo/demo.xml',
        'demo/blocks.xml',
    ],
    'images': [
        'static/description/odoo_experts_description.png',
        'static/description/odoo_experts_screenshot.jpeg',
    ],
    'price': 4,
    'currency': 'EUR',
    'live_test_url': 'https://theme-odoo-experts.odoo.com',
}