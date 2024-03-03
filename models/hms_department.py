from odoo import models, fields


class HmsDepartment(models.Model):
    _name = 'hms.department'
    _description = 'Hospital Department'

    name = fields.Char(required=True)
    capacity = fields.Integer()
    is_opened = fields.Boolean(string="Is Open", default=True)
    patient_ids = fields.One2many('hms.patient', 'department_id', string="Patients")
    doctor_ids = fields.Many2many('hms.doctor', string="Doctors")
