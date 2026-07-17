from odoo import fields, models


class ProductSaleOrderHistory(models.TransientModel):
    _name = 'product.sale.order.history'
    _description = 'Product Sale Order History'
    _rec_name = 'product_id'

    product_sale_history_ids = fields.One2many('product.sale.history.line',
                                           'order_line_id',
                                           string='Product Sale Price History',
                                           help="shows the product sale "
                                                "history of the customer")
    product_id = fields.Many2one('product.product',
                                 string="Product",
                                 help="Choose a Product")
    product_sale_ohistory_ids = fields.One2many('product.sale.history.oline',
                                           'order_line_id',
                                           string='Product Sale Price History generic',
                                           help="shows the product sale "
                                                "history of the other customer")
