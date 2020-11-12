# -*- coding: utf-8 -*-
# from odoo import http


# class TechRh(http.Controller):
#     @http.route('/tech_rh/tech_rh/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/tech_rh/tech_rh/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('tech_rh.listing', {
#             'root': '/tech_rh/tech_rh',
#             'objects': http.request.env['tech_rh.tech_rh'].search([]),
#         })

#     @http.route('/tech_rh/tech_rh/objects/<model("tech_rh.tech_rh"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('tech_rh.object', {
#             'object': obj
#         })
