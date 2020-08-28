# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Learning(models.Model):
    _inherit = 'res.partner'

    eslam = fields.Char()

    @api.multi
    def test(self):
        print('ssssssssssssssss')

    @api.multi
    def test2(self):
        print('Eslaaaaaaaaaaaaam')