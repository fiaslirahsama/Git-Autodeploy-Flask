from flask import redirect, render_template, url_for
from app.indexes import appindex
  
@appindex.route('/')
# @minify_decorators.minify(html=True, js=True, cssless=True)
def index():
  ohio= {
    'a' : 'Damkar',
    'b' : 'Selapat Pagi',
  }
  return render_template('ohio.html', ohio=ohio)

@appindex.route('/damen')
# @minify_decorators.minify(html=True, js=True, cssless=True)
def damen():
  ohio= {
    'a' : 'Damkar',
    'b' : 'Selapat Pagi',
  }
  return render_template('ohio.html', ohio=ohio)