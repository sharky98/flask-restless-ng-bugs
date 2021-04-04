#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Own modules
from ..extensions import db


a_item_to_c_item = db.Table('a_item_to_c_item',
    db.Column('a_item_id', db.Integer, db.ForeignKey('a_item.id'), primary_key=True),
    db.Column('c_item_id', db.Integer, db.ForeignKey('c_item.id'), primary_key=True)
)


class AItem(db.Model):
    """Item A, which has none or one Item B; and many items C."""
    __tablename__ = 'a_item'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    b_item_id = db.Column(db.Integer, db.ForeignKey('b_item.id'), nullable=True)
    b_item = db.relationship('BItem', back_populates="a_items")
    c_items = db.relationship("CItem", secondary=a_item_to_c_item, back_populates="a_items")


class BItem(db.Model):
    """Item B, which belong to many item A."""
    __tablename__ = 'b_item'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    a_items = db.relationship("AItem", back_populates="b_item")


class CItem(db.Model):
    """Item C which has many items A."""
    __tablename__ = 'c_item'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    a_items = db.relationship("AItem", secondary=a_item_to_c_item, back_populates="c_items")