from odoo import models, fields, api
from odoo.exceptions import ValidationError, UserError
from odoo.exceptions import Warning

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    is_booking_order = fields.Boolean(string='Is Booking Order', default=True)
    team = fields.Many2one('service.team', string='Team')
    team_leader = fields.Many2one('res.users', string='Team Leader')
    team_member = fields.Many2many('res.users', string='Team Members')
    book_start = fields.Datetime(string='Booking Start')
    book_end = fields.Datetime(string='Booking End')

    @api.onchange('team')
    def get_team(self):
        for rec in self:
            rec.team_leader = self.team.team_leader
            rec.team_member = self.team.team_member

    def cek_work_order(self):
        work = self.env['work.order'].search([
        '&', ('team_id', '=', self.team.id),
            ('team_member', 'in', self.team_member.ids),
            ('state', 'not in', 'cancel'),
            ('plan_start','=', self.book_start), 
            ('plan_end','=', self.book_end),
        ], limit=1)
        if work:
            raise ValidationError("Team already has work order during that period ")
        else:
            raise ValidationError("Team is available for booking.")
        
    