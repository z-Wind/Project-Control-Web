'''
models.py
'''
import datetime
from flask_sqlalchemy import SQLAlchemy

from .main import db

productIDs_components = db.Table('productIDs_components', db.Model.metadata,
                                 db.Column('productIDs_id', db.Integer,
                                           db.ForeignKey('productIDs.id')),
                                 db.Column('components_id', db.Integer,
                                           db.ForeignKey('components.id')))

productIDs_documents = db.Table('productIDs_documents', db.Model.metadata,
                                db.Column('productIDs_id', db.Integer,
                                          db.ForeignKey('productIDs.id')),
                                db.Column('documents_id', db.Integer,
                                          db.ForeignKey('documents.id')))

productIDs_histories = db.Table('productIDs_histories', db.Model.metadata,
                                db.Column('productIDs_id', db.Integer,
                                          db.ForeignKey('productIDs.id')),
                                db.Column('histories_id', db.Integer,
                                          db.ForeignKey('histories.id')))

documents_histories = db.Table('documents_histories', db.Model.metadata,
                               db.Column('documents_id', db.Integer,
                                         db.ForeignKey('documents.id')),
                               db.Column('histories_id', db.Integer,
                                         db.ForeignKey('histories.id')))


class Models(db.Model):
    # 若不寫則看 class name
    __tablename__ = 'models'
    # 設定 primary_key
    id = db.Column(
        db.Integer, primary_key=True, autoincrement=True, nullable=False)
    JIRA = db.Column(db.String(20))
    name = db.Column(db.String(20), nullable=False)
    projectCode = db.Column(db.String(20))
    stage = db.Column(db.String(5), nullable=False)
    PM = db.Column(db.String(4), nullable=False)
    APM = db.Column(db.String(4), nullable=False)
    modelNameCode = db.Column(db.String(20))

    remark = db.Column(db.Text)

    owner_id = db.Column(
        db.Integer, db.ForeignKey('owners.id'), nullable=False)
    owner = db.relationship(
        "Owners", back_populates="models", foreign_keys=[owner_id])

    productIDs = db.relationship(
        "ProductIDs",
        back_populates="model",
        foreign_keys='ProductIDs.model_id')

    def __repr__(self):
        return '<Models {}>'.format(self.name)


class Owners(db.Model):
    # 若不寫則看 class name
    __tablename__ = 'owners'
    # 設定 primary_key
    id = db.Column(
        db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.String(10), nullable=False)

    models = db.relationship(
        "Models", back_populates="owner", foreign_keys='Models.owner_id')

    def __repr__(self):
        return '<Owners {}>'.format(self.name)


class ProductIDs(db.Model):
    # 若不寫則看 class name
    __tablename__ = 'productIDs'
    # 設定 primary_key
    id = db.Column(
        db.Integer, primary_key=True, autoincrement=True, nullable=False)
    name = db.Column(db.Text, nullable=False, unique=True)
    customer = db.Column(db.String(20), nullable=False)
    customerModelName = db.Column(db.String(20))

    model_id = db.Column(
        db.Integer, db.ForeignKey('models.id'), nullable=False)
    model = db.relationship(
        "Models", back_populates="productIDs", foreign_keys=[model_id])

    components = db.relationship(
        "Components",
        secondary=productIDs_components,
        back_populates="productIDs")
    documents = db.relationship(
        "Documents",
        secondary=productIDs_documents,
        back_populates="productIDs")
    histories = db.relationship(
        "Histories",
        secondary=productIDs_histories,
        back_populates="productIDs")

    def __repr__(self):
        return '<ProductIDs {}>'.format(self.name)


class Components(db.Model):
    # 若不寫則看 class name
    __tablename__ = 'components'
    # 設定 primary_key
    id = db.Column(
        db.Integer, primary_key=True, autoincrement=True, nullable=False)
    PN_number = db.Column(db.String(30), unique=True)
    name = db.Column(db.String(30), nullable=False)
    type = db.Column(db.String(30), nullable=False)
    vendor = db.Column(db.String(30))
    remark = db.Column(db.Text)

    productIDs = db.relationship(
        "ProductIDs",
        secondary=productIDs_components,
        back_populates="components")

    def __repr__(self):
        return '<Components {} {} {}>'.format(self.PN_number, self.name,
                                              self.vendor)


class Documents(db.Model):
    # 若不寫則看 class name
    __tablename__ = 'documents'
    # 設定 primary_key
    id = db.Column(
        db.Integer, primary_key=True, autoincrement=True, nullable=False)
    DN_number = db.Column(db.String(9), nullable=False, unique=True)
    type = db.Column(db.String(30), nullable=False)
    stage = db.Column(db.String(10))
    remark = db.Column(db.Text)

    productIDs = db.relationship(
        "ProductIDs",
        secondary=productIDs_documents,
        back_populates="documents")
    histories = db.relationship(
        "Histories", secondary=documents_histories, back_populates="documents")

    def __repr__(self):
        return '<Documents {} {} {}>'.format(self.DN_number, self.type,
                                             self.remark)


class Histories(db.Model):
    # 若不寫則看 class name
    __tablename__ = 'histories'
    # 設定 primary_key
    id = db.Column(
        db.Integer, primary_key=True, autoincrement=True, nullable=False)
    date = db.Column(db.Date, default=datetime.datetime.now(), nullable=False)
    type = db.Column(db.String(30), nullable=False)
    PCBAs = db.Column(db.Text, nullable=False)
    PCBA_version = db.Column(db.Integer, nullable=False)
    circuitVersion = db.Column(db.Integer, nullable=False)
    PCBs = db.Column(db.Text)
    PCB_version = db.Column(db.Integer)
    remark = db.Column(db.Text)

    productIDs = db.relationship(
        "ProductIDs",
        secondary=productIDs_histories,
        back_populates="histories")
    documents = db.relationship(
        "Documents", secondary=documents_histories, back_populates="histories")

    def __repr__(self):
        return '<Histories {} {} {}>'.format(self.date, self.PCBAs,
                                             self.remark)


# Create user model.
class Users(db.Model):
    # 若不寫則看 class name
    __tablename__ = 'users'
    # 設定 primary_key
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(10))
    userName = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120))
    password = db.Column(db.String(64))

    # Flask-Login integration
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.id

    def __repr__(self):
        return '<Users {} {}>'.format(self.name, self.userName)