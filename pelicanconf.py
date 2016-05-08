#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Comozilla Lab'
SITENAME = 'Comozilla Lab'
SITETITLE = 'コモジラ研究所'
SITESUBTITLE = ""
SITEURL = 'http://localhost:8000'
RELATIVE_URLS = True

THEME = './themes/comozilla-theme'
THEME_STATIC_DIR = 'theme'
PATH = 'content'
STATIC_PATHS = ['extra/CNAME']
EXTRA_PATH_METADATA = {
    'extra/CNAME': {'path': 'CNAME'},
}

PLUGIN_PATHS = ['plugins']
PLUGINS = ['assets']

TIMEZONE = 'Asia/Tokyo'
DEFAULT_LANG = 'ja'
BOOTSTRAP_FILE = 'bootstrap.min.css'
CSS_FILE = 'freeagent.css'
FONTS = 'fonts'

SCRIPTS = [
	'jquery-1.11.0.js',
	'bootstrap.min.js',
	'http://cdnjs.cloudflare.com/ajax/libs/jquery-easing/1.3/jquery.easing.min.js',
	'classie.js',
	'cbpAnimatedHeader.js',
	'jqBootstrapValidation.js',
	'freeagent.js'
]

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DIRECT_TEMPLATES = ['index']
DELETE_OUTPUT_DIRECTORY = True
# Top Menu Links
NAVLINKS = (
	('#about', 'About'),
	('#services','Services'),
	('#portfolio', 'Portfolio'),
	('#contact', 'Contact')
)

# Portfolio Name
PORTFOLIO = 'Portfolio'

#Contact form fields sorted by: label, input_type, id, required_validation_,msg
CONTACT_FIELDS = (
	['Name', 'text', 'name', 'Please enter your name.'],
	['Email Address', 'email', 'email','Please enter your email address.' ],

	['Message', 'textarea', 'message', 'Please enter a message.']
)
