# -*- coding: utf-8 -*-
# from odoo import http


# class Myuhuu(http.Controller):
#     @http.route('/myuhuu/myuhuu', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/myuhuu/myuhuu/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('myuhuu.listing', {
#             'root': '/myuhuu/myuhuu',
#             'objects': http.request.env['myuhuu.myuhuu'].search([]),
#         })

#     @http.route('/myuhuu/myuhuu/objects/<model("myuhuu.myuhuu"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('myuhuu.object', {
#             'object': obj
#         })
