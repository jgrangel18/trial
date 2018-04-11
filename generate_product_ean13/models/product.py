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

from odoo import models, api, _
from datetime import datetime


class product_template(models.Model):
    _inherit = "product.template"

    @api.model
    def create(self, vals):
        res = super(product_template, self).create(vals)
        if res:
            if not vals.get('barcode') and self.env['ir.config_parameter'].sudo().get_param('gen_ean13'):
                barcode_str = self.env['barcode.nomenclature'].sanitize_ean("%s%s" % (res.id, datetime.now().strftime("%d%m%y%H%M")))
                res.write({'barcode': barcode_str})
        return res


class product_product(models.Model):
    _inherit = "product.product"

    @api.model
    def create(self, vals):
        res = super(product_product, self).create(vals)
        if res:
            if not vals.get('barcode') and self.env['ir.config_parameter'].sudo().get_param('gen_ean13'):
                barcode_str = self.env['barcode.nomenclature'].sanitize_ean("%s%s" % (res.id, datetime.now().strftime("%d%m%y%H%M")))
                res.write({'barcode': barcode_str})
        return res

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
