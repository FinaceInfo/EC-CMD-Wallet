import os
import sys
from pathlib import Path
import recommonmark
from recommonmark.transform import AutoStructify
from recommonmark.parser import CommonMarkParser
p = Path(__file__).absolute()
sys.path.insert(0, str(p.parent.parent))

extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.todo',
              'sphinx.ext.viewcode',
              'sphinx.ext.napoleon',
              'sphinx.ext.mathjax']

templates_path = ['_templates']

source_parsers = {
    '.md': 'recommonmark.parser.CommonMarkParser',
}
source_suffix = ['.rst', '.md']

master_doc = 'index'

project = 'EC_CMD_Wallet'
copyright = '2017, huangsizhe'
author = 'huangsizhe'

version = '0.0.1'

release = ''

language = 'en'

exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

pygments_style = 'sphinx'

todo_include_todos = True

html_theme = 'alabaster'

html_static_path = ['_static']

htmlhelp_basename = 'EC_CMD_Wallet'

latex_elements = {

}

latex_documents = [
    (master_doc, 'EC_CMD_Wallet.tex', 'EC_CMD_Wallet Documentation',
     'Author', 'manual'),
]

man_pages = [
    (master_doc, 'EC_CMD_Wallet', 'EC_CMD_Wallet Documentation',
     [author], 1)
]

texinfo_documents = [
    (master_doc, 'EC_CMD_Wallet', 'EC_CMD_Wallet Documentation',
     author, 'EC_CMD_Wallet', 'One line description of project.',
     'Miscellaneous'),
]

epub_title = project
epub_author = author
epub_publisher = author
epub_copyright = copyright

epub_exclude_files = ['search.html']

todo_include_todos = True
url_doc_root = "xxxx"#
def setup(app):
    app.add_config_value('recommonmark_config', {
        'url_resolver': lambda url: url_doc_root + url,
        'auto_toc_tree_section':'Contents',
         'enable_math':True,
        'enable_inline_math':True
    }, True)
    app.add_transform(AutoStructify)