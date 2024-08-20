from odoo import models, fields, api, _
from odoo import models, api, exceptions


class saleorder(models.Model):
    _inherit = 'sale.order'

    # Added button in the sale order name the button as Auto Process.
    # By Clicking the Button The SAle Order Is Confirmed , Create Invoice ,Validate the Invoice , Validate Delivery order , Register Payment
    def auto_process(self):
        # sale order confirm
        for order in self:
            order.action_confirm()  # action_confirm() using this sale order is confirmed
        # validate Delivery order
        for picking in order.picking_ids:  # Picking_ids will get when the delivery button is clicked
            if picking.state not in ('done', 'cancel'):
                    picking.action_confirm()
                    picking.action_assign()  # action_assign is used for -->Check availability of picking moves.
                    picking.button_validate()  # button_validate is used to validate the delivery order

        # create invoice
        invoice = order._create_invoices()
        invoice.action_post()  # action_post() is used to validate the invoice
        payment_register = self.env['account.payment.register'].with_context(active_model='account.move',
                                                                             active_ids=invoice.ids).create({
            'payment_date': invoice.date,
        })
        payment_register.action_create_payments()
        return True
