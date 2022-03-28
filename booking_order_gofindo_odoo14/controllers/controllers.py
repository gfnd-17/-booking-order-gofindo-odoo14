# -*- coding: utf-8 -*-
# from odoo import http


# class BookingOrderGofindoOdoo14(http.Controller):
#     @http.route('/booking-order-gofindo-odoo14/booking-order-gofindo-odoo14/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/booking-order-gofindo-odoo14/booking-order-gofindo-odoo14/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('booking-order-gofindo-odoo14.listing', {
#             'root': '/booking-order-gofindo-odoo14/booking-order-gofindo-odoo14',
#             'objects': http.request.env['booking-order-gofindo-odoo14.booking-order-gofindo-odoo14'].search([]),
#         })

#     @http.route('/booking-order-gofindo-odoo14/booking-order-gofindo-odoo14/objects/<model("booking-order-gofindo-odoo14.booking-order-gofindo-odoo14"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('booking-order-gofindo-odoo14.object', {
#             'object': obj
#         })
