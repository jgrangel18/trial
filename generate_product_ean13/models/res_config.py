# -*- coding: utf-8 -*-
#################################################################################
# Author      : Acespritech Solutions Pvt. Ltd. (<www.acespritech.com>)
# Copyright(c): 2012-Present Acespritech Solutions Pvt. Ltd.
# All Rights Reserved.
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#################################################################################

from odoo import fields, models, api, _


class res_config_settings(models.TransientModel):
    _inherit = "res.config.settings"

    def get_values(self):
        res = super(res_config_settings, self).get_values()
        res.update(
            gen_ean13=self.env['ir.config_parameter'].sudo().get_param('gen_ean13')
        )
        return res

    def set_values(self):
        super(res_config_settings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('gen_ean13', self.gen_ean13)

    gen_ean13 = fields.Boolean("On Product create generate EAN13")

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: