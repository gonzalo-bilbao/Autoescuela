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

class Autoescuela(models.Model):
    _name = 'autoescuela.autoescuela'
    _description = 'Modelo para gestionar autoescuelas'

    nombre = fields.Char(string='Nombre de la Autoescuela', required=True)
    domicilio = fields.Char(string='Domicilio')
    localidad = fields.Char(string='Localidad')
    provincia = fields.Char(string='Provincia')
    contacto = fields.Char(string='Contacto')
    # examen_ids = fields.Many2many('autoescuela.examen', string='Exámenes')
    # profesor_ids = fields.One2many('autoescuela.profesor', string='Profesores')
    # alumno_ids = fields.One2many('autoescuela.alumno', string='Alumnos')

class Examen(models.Model):
    _name = 'autoescuela.examen'
    _description = 'Modelo para gestionar examenes'

    nombre = fields.Char(string='Nombre del Examen')
    fecha = fields.Date(string='Fecha del Examen')
    precio = fields.monetary(string='Precio del Examen')
    clases = fields.integer(string='Número de Clases')
    carnet = fields.char(string='Tipo de Carnet', required=True)
    aprobado = fields.boolean(string='Aprobado', default=False)

class Profesor(models.Model):
    _name = 'autoescuela.profesor'
    _description = 'Modelo para gestionar profesores'

    nombre = fields.Char(string='Nombre del Profesor', required=True)
    dni = fields.Char(string='DNI', required=True)
    coche = fields.Char(string='Coche Asignado')
    matricula = fields.Char(string='Matrícula del Coche')
    incorporacion = fields.Date(string='Fecha de Incorporación')
    antiguedad = fields.integer(string='Antigüedad (años)', compute='_compute_antiguedad')

class Alumno(models.Model):
    _name = 'autoescuela.alumno'
    _description = 'Modelo para gestionar alumnos'

    nombre = fields.Char(string='Nombre del Alumno', required=True)
    dni = fields.Char(string='DNI', required=True)
    domicilio = fields.Char(string='Domicilio')
    matricula = fields.Char(string='Matrícula del Coche')