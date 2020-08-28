# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Learning(models.Model):
    _inherit = 'res.partner'

    eslam = fields.Char()

