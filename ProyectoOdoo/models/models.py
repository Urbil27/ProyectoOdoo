
from odoo import models, fields, api
from dataclasses import field


class equipo(models.Model):
    _name = 'equipo'
    _description = 'equipo'

    price = fields.Float()
    estado = my_selection_field = fields.Selection([('bueno', 'Bueno'), ('malo', 'Malo')], string='Estado del equipo')
    fechaCompra = fields.Datetime()

class aula(models.Model):
    _name = 'aula'
    codigo_aula = fields.Char()
    capacidad = fields.Integer()

class calificacion(models.Model):
    _name = 'calificacion'
    alumno_id = fields.Many2one('alumno','alumno_id')
    asignatura = fields.Many2one('asignatura','asignatura_id')
    calificacion = fields.Integer()

class asignatura(models.Model):
    _name = 'asignatura'
    profesor_id = fields.Many2one('profesor','profesor_id')
    nombre_asignatura= fields.Char()

class profesor(models.Model):
   _name = 'profesor'
   user_id = fields.Many2one('res.users', 'user_id')

class alumno(models.Model):
    _name = 'alumno'
    aula = fields.Many2one('aula', 'codigo_aula')
    user_id = fields.Many2one('res.users', 'user_id')

class asistencia(models.Model):
    _name= 'asistencia'
    alumno = fields.Many2one('alumno', 'user_id')
    asignatura = fields.Many2one('asignatura', 'asignatura_id')
    fechaAsistencia = fields.Datetime()
    falta = fields.Selection([('s', 'Si'), ('n', 'No'),])




   