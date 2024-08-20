from odoo import models, fields, api, _
from odoo import models, api, exceptions


class saleorder(models.Model):
    _inherit = 'purchase.order'

    def action_auto_process(self):
        for order in self:
            order.button_confirm()
            for picking in order.picking_ids:
                if picking.state not in ('done', 'cancel'):
                    picking.action_confirm()
                    picking.action_assign()
                    picking.button_validate()

            invoices = order.action_create_invoice()
            account_move_obj = self.env['account.move'].browse(invoices['res_id'])
            account_move_obj.invoice_date = order.date_order
            account_move_obj.action_post()
            payment_register = self.env['account.payment.register'].with_context(active_model='account.move',
                                                                                 active_ids=account_move_obj.ids).create(
                {
                    'payment_date': account_move_obj.invoice_date,
                })
            payment_register.action_create_payments()
