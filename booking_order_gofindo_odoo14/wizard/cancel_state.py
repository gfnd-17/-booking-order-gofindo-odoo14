from odoo import fields, models, api, _
from odoo.exceptions import UserError

class CancelStateWizard(models.TransientModel):

    _name = 'cancel.state.wizard'

    reason = fields.Text(string='Reason for cancellation') 

    def process_wizard(self):
        ids_to_change = self._context.get('active_ids')
        active_model = self._context.get('active_model')
        doc_ids = self.env[active_model].browse(ids_to_change)
        # 1. Run another function
        # doc_ids.set_open()

        # 2. Modify selected Document
        doc_ids.write(
            {
                'state' : 'cancel',
                'notes' : self.reason
            }
        )