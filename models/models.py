# -*- coding: utf-8 -*-

from odoo import models, fields, api


class tech_rh(models.Model):
    _name = 'tech.rh'

    matricule = fields.Char('Matricule')
    matricule_interne = fields.Char('Matricule (Interne)')
    n_rcar = fields.Char('N° RCAR')
    n_cmr = fields.Char('N° CMR')
    indice = fields.Char('Indice')
    date_grade = fields.Date("Date du grade")
    date_echelon = fields.Date("Date d'effet echelon")
    date_ambauche = fields.Date("Date d'ambauche")
    situation = fields.Char("Situation")
    grade_id = fields.Many2one('grade.rh', string="Grade")
    corps_id = fields.Many2one('corps.rh', string="Corps")
    echelle_id = fields.Many2one('echelle.rh', string="Echelle")
    echelon_id = fields.Many2one('echelon.rh', string="Echelon")

class grade(models.Model):
    _name = 'grade.rh'

    name = fields.Many2one('hr.employee', string="nom", required=True)

class corps(models.Model):
    _name = 'corps.rh'

    name = fields.Many2one('hr.employee', string="nom", required=True)

class echelle(models.Model):
    _name = 'echelle.rh'

    name = fields.Many2one('hr.employee', string="nom", required=True)

class echelon(models.Model):
    _name = 'echelon.rh'

    name = fields.Many2one('hr.employee', string="nom", required=True)