# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class autoescuela(models.Model):
#     _name = 'autoescuela.autoescuela'
#     _description = 'autoescuela.autoescuela'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

from odoo import models, fields, api # type: ignore
from datetime import date
from dateutil.relativedelta import relativedelta

class Autoescuela(models.Model):
    _name = 'autoescuela.autoescuela'
    _description = 'Modelo para gestionar autoescuelas'

    name = fields.Char(string='Nombre', required=True)
    domicilio = fields.Char(string='Domicilio')
    localidad = fields.Char(string='Localidad')
    provincia = fields.Char(string='Provincia')
    contacto = fields.Char(string='Contacto')
    
    examen_ids = fields.Many2many('autoescuela.examen', string='Exámenes')
    profesor_ids = fields.One2many('autoescuela.profesor', 'autoescuela_id', string='Profesores')
    alumno_ids = fields.One2many('autoescuela.alumno', 'autoescuela_id', string='Alumnos')

class Examen(models.Model):
    _name = 'autoescuela.examen'
    _description = 'Modelo para gestionar examenes'

    name = fields.Char(string='Referencia', required=True, copy=False, readonly=True, default=lambda self: 'Nuevo')
    fecha = fields.Date(string='Fecha del Examen')
    moneda_id = fields.Many2one('res.currency', string='Moneda')
    precio = fields.Monetary(string='Precio del Examen', currency_field='moneda_id')
    clases = fields.Integer(string='Número de Clases')
    carnet = fields.Char(string='Tipo de Carnet', required=True, 
                         help="AM = Ciclomotores (hasta 50 cc)\n"
                              "A1 = Motocicletas (potencia máxima 11 kW)\n"
                              "A2 = Motocicletas (potencia máxima 35 kW)\n"
                              "A = Motocicletas y triciclos de motor\n"
                              "B = Automóviles (MMA hasta 3.500 kg)")
    aprobado = fields.Boolean(string='Aprobado', default=False)
    
    autoescuela_ids = fields.Many2many('autoescuela.autoescuela', string='Autoescuelas')
    alumno_id = fields.Many2one('autoescuela.alumno', string='Alumno', required=True)

    @api.model
    def create(self, vals):
        if vals.get('name', 'Nuevo') == 'Nuevo':
            vals['name'] = self.env['ir.sequence'].next_by_code('autoescuela.examen') or 'Nuevo'
        return super(Examen, self).create(vals)

class Profesor(models.Model):
    _name = 'autoescuela.profesor'
    _description = 'Modelo para gestionar profesores'

    name = fields.Char(string='Nombre del Profesor', required=True)
    dni = fields.Char(string='DNI', required=True)
    coche = fields.Char(string='Coche Asignado')
    matricula = fields.Char(string='Matrícula del Coche')
    incorporacion = fields.Date(string='Fecha de Incorporación')
    antiguedad = fields.Integer(string='Antigüedad (años)', compute='_compute_antiguedad')
    
    autoescuela_id = fields.Many2one('autoescuela.autoescuela', string='Autoescuela')
    alumno_ids = fields.One2many('autoescuela.alumno', 'profesor_id', string='Alumnos')

    @api.depends('incorporacion')
    def _compute_antiguedad(self):
        for record in self:
            if record.incorporacion:
                record.antiguedad = relativedelta(fields.Date.today(), record.incorporacion).years
            else:
                record.antiguedad = 0

class Alumno(models.Model):
    _name = 'autoescuela.alumno'
    _description = 'Modelo para gestionar alumnos'

    name = fields.Char(string='Nombre del Alumno', required=True)
    dni = fields.Char(string='DNI', required=True)
    domicilio = fields.Char(string='Domicilio')
    matricula = fields.Char(string='Matrícula')
    
    autoescuela_id = fields.Many2one('autoescuela.autoescuela', string='Autoescuela')
    profesor_id = fields.Many2one('autoescuela.profesor', string='Profesor')
    examen_ids = fields.One2many('autoescuela.examen', 'alumno_id', string='Exámenes')