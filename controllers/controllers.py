# -*- coding: utf-8 -*-
from odoo import http

# class MethodLaundry(http.Controller):
#     @http.route('/method_laundry/method_laundry/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/method_laundry/method_laundry/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('method_laundry.listing', {
#             'root': '/method_laundry/method_laundry',
#             'objects': http.request.env['method_laundry.method_laundry'].search([]),
#         })

#     @http.route('/method_laundry/method_laundry/objects/<model("method_laundry.method_laundry"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('method_laundry.object', {
#             'object': obj
#         })