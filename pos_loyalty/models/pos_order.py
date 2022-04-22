# Copyright 2004-2010 OpenERP SA
# Copyright 2017 RGB Consulting S.L. (https://www.rgbconsulting.com)
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import api, fields, models


class PosOrder(models.Model):
    _inherit = "pos.order"

    loyalty_points = fields.Float(
        #string="Loyalty Points",
        #help="The amount of Loyalty points awarded " "to the customer with this order",
        string="Puntos de lealtad",
        help="La cantidad de puntos de fidelidad otorgados al cliente con este pedido",
    )

    @api.model
    def _order_fields(self, ui_order):
        res = super(PosOrder, self)._order_fields(ui_order)
        res["loyalty_points"] = ui_order.get("loyalty_points", 0)
        return res

    @api.model
    def create_from_ui(self, orders, draft=False):
        res = super(PosOrder, self).create_from_ui(orders, draft)
        for order in orders:
            order_partner = order["data"]["partner_id"]
            order_points = order["data"].get("loyalty_points", 0)
            if order_points != 0 and order_partner:
                partner = self.env["res.partner"].browse(order_partner)
                partner.loyalty_points += order_points
        return res
