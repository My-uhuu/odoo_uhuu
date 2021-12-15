# -*- coding: utf-8 -*-
from odoo import http
#import logging
#_logger = logging.getLogger(__name__)

class Myuhuu(http.Controller):
    @http.route('/myuhuu', auth='public')
    def index(self, **kw):
        return "Hello, world - Uhuu"
    
    @http.route('/myuhuu/searchContacts', auth='user', methods=['GET'], type='json')
    def getContacts(self, **kw):
        ## Validar con try/catch para evitar problemas, o gestionar las respuestas del api
        json_data = http.request.jsonrequest
        query = []
        if 'query' in json_data :
            query = json_data["query"]

        #_logger.info(query)
        contacts_db = http.request.env['res.partner'].search(query)
        contacts=[]

        for record in contacts_db :
            contact = {
                "id": record['id'],
                "name": record['name']
            }
            contacts.append(contact)
        
        data = {
            "status" : 200,
            "response": contacts,
            "message": "OK"
        }
        return data
    
    @http.route('/myuhuu/searchLeads', auth='user', methods=['GET'], type='json')
    def getContacts(self, **kw):
        ## Validar con try/catch para evitar problemas, o gestionar las respuestas del api
        json_data = http.request.jsonrequest
        query = []
        if 'query' in json_data :
            query = json_data["query"]

        #_logger.info(query)
        contacts_db = http.request.env['crm.lead'].search(query)
        contacts=[]

        for record in contacts_db :
            contact = {
                "id": record['id'],
                "name": record['name']
            }
            contacts.append(contact)
        
        data = {
            "status" : 200,
            "response": contacts,
            "message": "OK"
        }
        return data

#    @http.route('/myuhuu/myuhuu/objects', auth='public')
#    def list(self, **kw):
#        return http.request.render('myuhuu.listing', {
#            'root': '/myuhuu/myuhuu',
#            'objects': http.request.env['myuhuu.myuhuu'].search([]),
#        })

#    @http.route('/myuhuu/myuhuu/objects/<model("myuhuu.myuhuu"):obj>', auth='public')
#    def object(self, obj, **kw):
#        return http.request.render('myuhuu.object', {
#            'object': obj
#        })
