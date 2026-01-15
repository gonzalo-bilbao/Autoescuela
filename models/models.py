# -*- coding: utf-8 -*-

from odoo import models, fields, api
from dateutil.relativedelta import relativedelta

# CLASE AUTOESCUELA
class Autoescuela(models.Model):
    _name = 'autoescuela.autoescuela'
    _description = 'Modelo para gestionar autoescuelas'

    name = fields.Char(string='Nombre', required=True)
    domicilio = fields.Char(string='Domicilio')
    localidad = fields.Char(string='Localidad')
    provincia = fields.Char(string='Provincia')
    contacto = fields.Char(string='Contacto')
    
    # Relaciones
    examen_ids = fields.Many2many('autoescuela.examen', string='Exámenes')
    profesor_ids = fields.One2many('autoescuela.profesor', 'autoescuela_id', string='Profesores')
    alumno_ids = fields.One2many('autoescuela.alumno', 'autoescuela_id', string='Alumnos')

# CLASE PROFESOR
class Profesor(models.Model):
    _name = 'autoescuela.profesor'
    _description = 'Modelo para gestionar profesores'

    name = fields.Char(string='Nombre del Profesor', required=True)
    dni = fields.Char(string='DNI', required=True)
    coche = fields.Char(string='Coche Asignado')
    matricula = fields.Char(string='Matrícula del Coche')
    incorporacion = fields.Date(string='Fecha de Incorporación')
    
    # Campo computado
    antiguedad = fields.Integer(string='Antigüedad (años)', compute='_compute_antiguedad')
    
    # Relaciones
    autoescuela_id = fields.Many2one('autoescuela.autoescuela', string='Autoescuela')
    alumno_ids = fields.One2many('autoescuela.alumno', 'profesor_id', string='Alumnos')

    @api.depends('incorporacion')
    def _compute_antiguedad(self):
        for record in self:
            if record.incorporacion:
                record.antiguedad = relativedelta(fields.Date.today(), record.incorporacion).years
            else:
                record.antiguedad = 0

# CLASE ALUMNO
class Alumno(models.Model):
    _name = 'autoescuela.alumno'
    _description = 'Permite definir las características de un alumno'

    name = fields.Char(string="Nombre y Apellidos", required=True)
    dni = fields.Char(string="DNI", required=True)
    matricula = fields.Char(string="Número de matrícula")
    domicilio = fields.Char(string="Domicilio")
    
    # Relaciones
    autoescuela_id = fields.Many2one('autoescuela.autoescuela', string="Autoescuela")
    profesor_id = fields.Many2one('autoescuela.profesor', string="Profesor habitual")
    examen_ids = fields.One2many('autoescuela.examen', 'alumno_id', string="Exámenes")

# CLASE EXAMEN
class Examen(models.Model):
    _name = 'autoescuela.examen'
    _description = 'Modelo para gestionar examenes'

    # Secuencia para el nombre
    name = fields.Char(string='Referencia', required=True, copy=False, readonly=True, default=lambda self: 'Autogenerado')
    
    fecha = fields.Date(string='Fecha del Examen')
    clases = fields.Integer(string='Número de Clases')
    
    # Moneda y Precio
    moneda_id = fields.Many2one('res.currency', string='Moneda')
    precio = fields.Monetary(string='Precio del Examen', currency_field='moneda_id')
    
    carnet = fields.Char(string='Tipo de Carnet', required=True, 
                         help="AM = Ciclomotores (hasta 50 cc)\n"
                              "A1 = Motocicletas (potencia máxima 11 kW)\n"
                              "A2 = Motocicletas (potencia máxima 35 kW)\n"
                              "A = Motocicletas y triciclos de motor\n"
                              "B = Automóviles (MMA hasta 3.500 kg)")
    
    aprobado = fields.Boolean(string='Aprobado', default=False)
    
    # Relaciones
    autoescuela_ids = fields.Many2many('autoescuela.autoescuela', string='Autoescuelas')
    alumno_id = fields.Many2one('autoescuela.alumno', string='Alumno', required=True)

    # Lógica para autogenerar la secuencia
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'Autogenerado') == 'Autogenerado':
                vals['name'] = self.env['ir.sequence'].next_by_code('autoescuela.examen') or 'Autogenerado'
        return super(Examen, self).create(vals_list)

    # --- ESTA ES LA FUNCIÓN QUE PIDE EL PDF PARA EL TEXTO DEL CALENDARIO ---
    def _compute_display_name(self):
        for record in self:
            # Crea el texto: 'Código Examen: SGE001 - Carnet: B'
            if record.name and record.carnet:
                record.display_name = f'Código Examen: {record.name} - Carnet: {record.carnet}'
            else:
                record.display_name = record.name or ""