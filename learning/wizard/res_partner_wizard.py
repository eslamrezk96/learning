from odoo import api, fields, models


class CreateAppointment(models.TransientModel):
    _name = 'hr.res.partner'

    hr_id = fields.Many2one(comodel_name="res.partner", string="HR")

    def hr_test(self):
        print('bakaaaar')
