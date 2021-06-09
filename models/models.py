# -*- coding: utf-8 -*-
import time
from datetime import datetime
from odoo import models, fields, api, _
from odoo.exceptions import UserError


class ModuleName(models.Model):
    _inherit = 'washing.washing'


class ModuleName(models.Model):
    _inherit = 'res.partner'

    planes_lavaderia_ids = fields.One2many(comodel_name='method_laundry.cliente_plan', inverse_name='partner_id', string='Planes de Lavandería')    
    laundry_order_ids = fields.One2many(comodel_name='laundry.order', inverse_name='partner_id', string='Ordenes de Lavandería')    
    laundry_order_count = fields.Integer(compute='_compute_order_laundry_count', string='Nro. Ordenes Lavandería')
    
    @api.depends('laundry_order_ids')
    def _compute_order_laundry_count(self):
        i=0
        for orden in self.laundry_order_ids:
           i+=1
        self.laundry_order_count=i 
    



class ModuleName(models.Model):
    _inherit = 'laundry.order'

    fecha_retiro = fields.Date(string='Fecha Retiro', default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
    fecha_entrega = fields.Date(string='Fecha Entrega')
    tipo_pago = fields.Selection([('plan', 'Plan'),('boleta_ticket','Boleta/Tikect'),('app','Aplicación Mr. Jeff')], string='Tipo de Pago',required=True)
    pos_order_id = fields.Many2one(comodel_name='pos.order', string='Boleta/Ticket',
                                   domain="[('partner_id', '=', partner_id)]")
    nro_pedido = fields.Char(string='Nro. Pedido',related='pos_order_id.pos_reference')
    nro_mr_jeff = fields.Char(string='Nro. Mr Jeff')
    
    plan_id = fields.Many2one(comodel_name='method_laundry.cliente_plan', 
                              string='Planes de Lavandería',
                              domain="[('partner_id', '=', partner_id),('saldo_cupo_lavados','>',0)]")
    


class PedidosPOS(models.Model):
    _inherit = 'pos.order'
    _rec_name = 'pos_reference'


class PlanLavados(models.Model):
    _name = 'method_laundry.plan'
    _description = 'Planes de lavado'

    name = fields.Char(string='Nombre del Plan')    
    cupo_lavados = fields.Integer(string='Cupos de Lavado')
    descripcion = fields.Text(string='Descripción')
    
            


class ClientesPlan(models.Model):
    _name = 'method_laundry.cliente_plan'

    name = fields.Char(string='Nombre del Plan Cliente')    
    partner_id = fields.Many2one(comodel_name='res.partner', string='Cliente')
    plan_id = fields.Many2one(comodel_name='method_laundry.plan', string='Plan de Lavandería')
    fecha_inicio = fields.Date(string='Fecha Inicio')
    fecha_final = fields.Date(string='Fecha Final')
    cupo_lavados = fields.Integer(string='Cupo de Lavados',related='plan_id.cupo_lavados')
    cupo_lavados_usados = fields.Integer(compute='_compute_cupo_lavados_usados', string='Cupos Usados', store=True)
    saldo_cupo_lavados = fields.Integer(compute='_compute_saldo_cupo_lavados', string='Saldo Cupos Lavado', store=True)
    laundry_order_ids = fields.One2many(comodel_name='laundry.order', inverse_name='plan_id', string='Ordenes de Lavado')
    dia_retiro = fields.Selection([
        ('lunes', 'Lunes'),('martes', 'Martes'),('miercoles', 'Miercoles'),('jueves', 'Jueves'),('viernes', 'Viernes'),
        ('sabado', 'Sabado'),('domingo', 'Domingo')
    ], string='Día Retiro')
    dia_entrega = fields.Selection([
        ('lunes', 'Lunes'),('martes', 'Martes'),('miercoles', 'Miercoles'),('jueves', 'Jueves'),('viernes', 'Viernes'),
        ('sabado', 'Sabado'),('domingo', 'Domingo')
    ], string='Día Retiro')
    

    @api.depends('laundry_order_ids','cupo_lavados_usados')
    def _compute_saldo_cupo_lavados(self):
        for p in self:
            p.saldo_cupo_lavados=p.cupo_lavados-p.cupo_lavados_usados
    
    @api.multi
    @api.depends('laundry_order_ids')
    def _compute_cupo_lavados_usados(self):
        for p in self:
            i=0
            for order in p.laundry_order_ids:
                i+=1
            p.cupo_lavados_usados=i 
    
    
    
    

