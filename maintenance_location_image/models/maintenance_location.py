from odoo import models

class MaintenanceLocation(models.Model):
    _inherit = ["maintenance.location", "image.mixin"]
    _name = "maintenance.location"
