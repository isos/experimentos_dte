# -*- coding: utf-8 -*-
"""
    dteweb
    ~~~~~~~
    A simple chilean invoice viewer in jinja2

    :copyright: (c) 2015 by Daniel Blanco.
"""
import os
import urlparse
import locale
locale.setlocale(locale.LC_ALL,'es_CL.utf-8')
from werkzeug.wrappers import Request, Response
from werkzeug.routing import Map, Rule
from werkzeug.exceptions import HTTPException, NotFound
from werkzeug.wsgi import SharedDataMiddleware
from werkzeug.utils import redirect

from jinja2 import Environment, FileSystemLoader
from parsedxml import head, partner, lines


def is_valid_url(url):
    parts = urlparse.urlparse(url)
    return parts.scheme in ('http', 'https')

def get_hostname(url):
    return urlparse.urlparse(url).netloc

#filtros definidos por mi
def format_currency(value):
    if isinstance(value, str):
        return ' '
    a = str(int(round(value,0)))
    result = ''
    i = -3
    porcion = a[i:]
    result = porcion
    while len(porcion) >= 3:
        j = i
        i -= 3
        porcion = a[i:j]
        if len(porcion) == 0:
            break
        result = porcion + '.' + result
    return result
    #locale.currency(value)

def righted(value,qty):
    return value.rjust(qty)

def format_vat(value):
    try:
        return locale.format('%d',int(float(value[2:10])),1)+'-' + value[10:]
    except:
        return "----"
    
def integ(value):
    return str(value)

def fixlen(value,qty):
    return value.ljust(qty)[:qty]

def comuna(value):
    value1 = value.split("/")
    return value1[2].strip()

def zeroempty(value):
    if isinstance(value, str) and value == '':
        return ''
    elif value == 0:
        return ''
    else:
        return value
    
class DTEWeb(object):

    def __init__(self, config):
        template_path = os.path.join(os.path.dirname(__file__), 'templates')
        self.jinja_env = Environment(loader=FileSystemLoader(template_path),autoescape=True)
        self.jinja_env = Environment(loader=FileSystemLoader(template_path),autoescape=True)        
        self.jinja_env.filters['hostname'] = get_hostname
        self.jinja_env.filters['fixlen'] = fixlen
        self.jinja_env.filters['format_vat'] = format_vat
        self.jinja_env.filters['comuna'] = comuna
        self.jinja_env.filters['righted'] = righted
        self.jinja_env.filters['format_currency'] = format_currency
        self.jinja_env.filters['integ'] = integ
        self.jinja_env.filters['zeroempty'] = zeroempty

        self.url_map = Map([
            Rule('/', endpoint='invoice'),
            #Rule('/<short_id>', endpoint='follow_short_link'),
            #Rule('/<short_id>+', endpoint='short_link_details')
        ])

    def on_invoice(self, request, *variables):
        error = None
        url = ''
        company_vat = '76201227-K'
        if request.method == 'POST':
            url = request.form['url']
            if not is_valid_url(url):
                error = 'Por favor, ingrese una url válida'
                #  Estas acciones no vienen al caso por ahora, ya que insert_url
                #  es una funcion que trabaja sobre el modelo de datos
                #  else:
                #  short_id = self.insert_url(url)
                #  return redirect('/%s+' % short_id)
        return self.render_template('invoice.html', error=error, url=url, company_vat=company_vat, head=head, partner=partner, lines=lines)


    """
    Estas funciones que están acá corresponden a shotly, no se usan por
    ahora, pero las dejo como ejemplo de controladores (eligió ponerle 
    el "on_" delante)
    
    def on_follow_short_link(self, request, short_id):
        link_target = self.redis.get('url-target:' + short_id)
        if link_target is None:
            raise NotFound()
        self.redis.incr('click-count:' + short_id)
        return redirect(link_target)

    def on_short_link_details(self, request, short_id):
        link_target = self.redis.get('url-target:' + short_id)
        if link_target is None:
            raise NotFound()
        click_count = int(self.redis.get('click-count:' + short_id) or 0)
        return self.render_template('short_link_details.html',
            link_target=link_target,
            short_id=short_id,
            click_count=click_count
        )
    """
    def error_404(self):
        response = self.render_template('404.html')
        response.status_code = 404
        return response

    def render_template(self, template_name, **context):
        t = self.jinja_env.get_template(template_name)
        return Response(t.render(context), mimetype='text/html')


    """ 
    estas funciones vendrian a ser referentes al modelo, que por ahora
    no tengo
        def insert_url(self, url):
            short_id = self.redis.get('reverse-url:' + url)
            if short_id is not None:
                return short_id
            url_num = self.redis.incr('last-url-id')
            short_id = base36_encode(url_num)
            self.redis.set('url-target:' + short_id, url)
            self.redis.set('reverse-url:' + url, short_id)
            return short_id
    """

    def dispatch_request(self, request):
        adapter = self.url_map.bind_to_environ(request.environ)
        try:
            endpoint, values = adapter.match()
            return getattr(self, 'on_' + endpoint)(request, **values)
        except NotFound, e:
            return self.error_404()
        except HTTPException, e:
            return e

    def wsgi_app(self, environ, start_response):
        request = Request(environ)
        response = self.dispatch_request(request)
        return response(environ, start_response)

    def __call__(self, environ, start_response):
        return self.wsgi_app(environ, start_response)

# estas funciones son de modelado en redis. no me sirven por ahora
# esta creando una "app" (tabla)
# notar que esta está fuera de la clase

def create_app(with_static=True):
    app = DTEWeb({'company_vat':'72201224-3'})
    if with_static:
        app.wsgi_app = SharedDataMiddleware(app.wsgi_app, {
            '/static':  os.path.join(os.path.dirname(__file__), 'static')
        })
    return app


if __name__ == '__main__':
    from werkzeug.serving import run_simple
    app = create_app()
    run_simple('127.0.0.1', 5000, app, use_debugger=True, use_reloader=True)
