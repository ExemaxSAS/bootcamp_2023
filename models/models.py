# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class BootcampBootcamp(models.Model):
    _name = 'bootcamp.bootcamp'

    def test_bootcamp(self):
        raise ValidationError('Test Bootcamp')

    def update_sale_order_note(self):
        if self.sale_order:
            self.sale_order.note = self.note
        else:
            raise ValidationError('No hay Presupuesto asociado')

    name = fields.Char('Nombre')
    sale_order = fields.Many2one('sale.order', 'Presupuesto')
    note = fields.Text('Nota')
    user_id = fields.Many2one('res.users', 'Usuario')

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    @api.constrains('campo_text')
    def _constrains_text(self):
        if self.campo_text != 'Hola Mundo':
            raise ValidationError('No se puede guardar así')

    @api.depends('campo_integer')
    def _compute_float(self):
        for rec in self:
            rec.campo_float = rec.campo_integer * 10

    campo_boolean = fields.Boolean(string='Campo Boolean')
    campo_integer = fields.Integer(string='Campo Integer', default=50)
    campo_float = fields.Float(string='Campo Float')
    campo_monetary = fields.Monetary(string='Campo Monetary')
    campo_char = fields.Char(string='Campo Char', related='partner_id.name')
    campo_text = fields.Text(string='Campo Texto')
    campo_selection = fields.Selection([('uno', 'Uno'), ('dos', 'Dos')], string='Campo Selection', default='dos')
    campo_html = fields.Html(string='Campo HTML')
    campo_binary = fields.Binary(string='Campo Binary')
    campo_date = fields.Date(string='Campo Date') #2023-03-16
    campo_datetime = fields.Datetime(string='Campo Datetime') #2023-03-16 00:00:00

    campo_many2one = fields.Many2one('res.partner', string='Campo Many2one') # 2
    campo_one2many = fields.One2many('res.partner', 'sale_id', string='Campo One2many') # [2, 3, 4, 5]
    campo_many2many = fields.Many2many('product.template', 'sale_id', string='Campo Many2many')

class ResPartner(models.Model):
    _inherit = 'res.partner'

    sale_id = fields.Many2one('sale.order', string='Sale ID')

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    sale_id = fields.Many2one('sale.order', string='Sale ID')


class PartnerXlsx(models.AbstractModel):
    _name = 'report.bootcamp.reporte_excel'
    _inherit = 'report.report_xlsx.abstract'

    def generate_xlsx_report(self, workbook, data, partners):
        report_name = 'Bootcamp XLSX'
        sheet = workbook.add_worksheet(report_name)

        for i, obj in enumerate(partners):
            sheet.write(i, 0, obj.name)
            sheet.write(i, 1, obj.property_product_pricelist.currency_id.name)
            if obj.property_product_pricelist.currency_id.name == 'EUR':
               sheet.write(i, 2, obj.property_product_pricelist.currency_id.l10n_ar_afip_code)
