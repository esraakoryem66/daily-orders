from odoo import fields,models,api, _

class TodayOrders(models.Model):
    _name='today.orders'
    _inherit=['mail.thread']
    _description = 'it displays daily orders and its number'

    # transaction_ids = fields.Many2many('sale.order', 'today_orders_transaction_rel', 'order_id', 'related_order_id', string='Transactions')
    order_date = fields.Date(string='Order Date')
    today_orders = fields.Integer(string='Number of Orders', compute='_compute_today_orders')
    ref=fields.Char(string="reference", default=lambda self: _('New'))

    @api.depends('order_date')
    def _compute_today_orders(self):
            for record in self:
                # Your logic to count daily orders based on order date
                orders = self.env['sale.order'].search_count([('date_order', '=', record.order_date)])
                record.today_orders = orders


    @api.model_create_multi
    def create(self, vals_list):
     for vals in vals_list:
            vals['ref']=self.env['ir.sequence'].next_by_code('today.orders')
     return super(TodayOrders,self).create(vals_list)

    # @api.onchange('order_date')
    # def _onchange_order_date(self):
    #    if self.order_date=='date_order':
    #         for record in self:
    #             # Your logic to count daily orders based on order date
    #             orders = self.env['sale.order'].search_count([('date_order', '=', record.order_date)])
    #             record.today_orders = orders
        