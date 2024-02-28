from odoo import models, fields

class uhuu_res_partner_fields(models.Model):
    _description = 'Campos adicionales para uhuuchat'
    _inherit = 'res.partner'

    x_facebookId = fields.Text(string='Facebook ID (Uhuu!)', default=False)
    x_telegramId= fields.Text(string='Telegram ID (Uhuu!)', default=False)
    x_twitterId = fields.Text(string='Twitter ID (Uhuu!)', default=False)