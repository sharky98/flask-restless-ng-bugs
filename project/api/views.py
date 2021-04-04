#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Own modules
from ..extensions import manager
from ..frontend.models import AItem, BItem, CItem


def initialize_api(app):
    with app.app_context():
        # List all Flask-Restless APIs here
        # Frontend
        a_item_api = manager.create_api(AItem, methods=['GET','POST','PATCH'])
        b_item_api = manager.create_api(BItem, methods=['GET','POST','PATCH'])
        c_item_api = manager.create_api(CItem, methods=['GET','POST','PATCH'])
