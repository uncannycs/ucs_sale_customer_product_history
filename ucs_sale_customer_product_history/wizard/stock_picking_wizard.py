# models/stock_picking_wizard.py
from odoo import models, fields, api

class StockPickingWizard(models.TransientModel):
    _name = 'stock.picking.wizard'
    _description = 'Picking Wizard'

    picking_id = fields.Many2one('stock.picking', string="Picking")
    product_id = fields.Many2one('product.product', string="Product")
    product_uom_qty = fields.Float("Demand Qty")
    quantity = fields.Float("Reserved Qty")
