# -*- coding: utf-8 -*-
from odoo.exceptions import Warning
from odoo import fields, models , _ ,tools
from odoo.tools import drop_view_if_exists


class drugsalereport(models.Model):
    _name = 'drug.sale'
    _description = "Drug Sale Report"
    _auto = False
   
    so_name = fields.Char( string="Bill No")
    rp_name = fields.Char( string="Doctor Name")
    rp1_name = fields.Char(string="Patinet Name")
    rp1_ref = fields.Char(string="Patient Identifier")
    pt_name = fields.Char( string='Product Name')
    qty = fields.Float(string="Quantity")
    spl_name = fields.Char(string="Batch")
    spl_life_date= fields.Char(string="Expiry")
    so_date = fields.Datetime(string="Bill Date")
    
    
    def init(self):
        tools.drop_view_if_exists(self._cr,  'drug_sale')
        self._cr.execute("""   CREATE OR REPLACE VIEW drug_sale AS (
        SELECT ROW_NUMBER() OVER (ORDER BY so.name ) as id,so.name as so_name,so.confirmation_date  as so_date ,COALESCE (NULLIF(rp.name,'')) as rp_name ,rp1.name as rp1_name ,rp1.ref as rp1_ref ,pt.name as  pt_name,
        cast(sum(sol.product_uom_qty) as DECIMAL(10,2)) AS qty ,spl.name as spl_name ,CAST(spl.life_date AS DATE) as spl_life_date
        FROM sale_order_line sol
        INNER JOIN sale_order so ON sol.order_id=so.id AND 
           (so.state!='cancel' AND so.state!='draft')
        LEFT JOIN product_product pp ON pp.id = sol.product_id
        INNER JOIN product_template pt ON pt.id = pp.product_tmpl_id 
        LEFT JOIN stock_production_lot spl ON spl.id = sol.lot_id
        LEFT OUTER JOIN res_partner rp ON rp.id = so.doctor_name AND rp.is_doctor='t'
        JOIN res_partner rp1 ON rp1.id = so.partner_id
        WHERE pt.type='product' AND pt.active='t' 
        GROUP BY sol.product_id,pt.name ,rp1.name,rp1.ref,so.name,spl.name,rp.name,spl.life_date,sol.product_uom_qty,so.confirmation_date
        )""")

   
    def unlink(self):
        raise Warning('You cannot delete any record!')



