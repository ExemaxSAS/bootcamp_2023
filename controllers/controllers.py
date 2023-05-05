# -*- coding: utf-8 -*-
import odoo
from odoo import http
from odoo.http import request

class Bootcamp(http.Controller):

    @http.route('/bootcamp', auth='public', website=True)
    def bootcamp(self, **kw):

        products = request.env['product.product'].sudo().search([('id', '>', 1)])
        result = []

        for p in products:
            result.append({'name': p.name})

        return str('<b>' + result[0]['name'] + '</b>')

    @http.route(['/bootcamp_website'], auth="public", website=True)
    def bootcamp_website(self, **kw):
        return request.render('bootcamp.bootcamp_website', {})

