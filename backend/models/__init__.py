from extensions import db
from werkzeug.security import generate_password_hash, check_password_hash
import datetime
from flask import current_app

conversation_document = db.Table('conversation_document',
    db.Column('conversation_id', db.Integer, db.ForeignKey('conversation.id'), primary_key=True),
    db.Column('document_id', db.Integer, db.ForeignKey('document.id'), primary_key=True)
)

class Conversation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # Add other fields here
    messages = db.relationship('Message', backref='conversation')
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    last_updated_at = db.Column(db.DateTime, default=datetime.datetime.utcnow, onupdate=datetime.datetime.utcnow)

    documents = db.relationship('Document', secondary=conversation_document, lazy='subquery',
                                backref=db.backref('conversations', lazy=True))

    def serialize(self):
        # Convert the object's state to a serializable dictionary
        return {
            'conversation_id': self.id,
            'user_id': self.user_id,
            'created_at': self.created_at,
            'last_updated_at': self.last_updated_at,
            'messages': [message.serialize() for message in self.messages],
            'documents': [document.serialize() for document in self.documents]
        }

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    conversations = db.relationship('Conversation', backref='user')
    documents = db.relationship('Document', backref='user')
    # Add other fields here

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def serialize(self):
        # Convert the object's state to a serializable dictionary
        return {
            'id': self.id,
            'email': self.email,
            'created_at': self.created_at
        }

class Message(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(1280), nullable=False)
    role = db.Column(db.String(128), nullable=False)
    conversation_id = db.Column(db.Integer, db.ForeignKey('conversation.id'))
    # Add other fields here

    def serialize(self):
        # Convert the object's state to a serializable dictionary
        return {
            'id': self.id,
            'content': self.content,
            'role': self.role
        }

class Document(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    file_name = db.Column(db.String(255))
    content_type = db.Column(db.String(255))
    file_size = db.Column(db.Integer)
    s3_file_name = db.Column(db.String(255))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def get_s3_file_url(self):
        S3_BUCKET = current_app.config['S3_DOCUMENT_STORE']
        S3_REGION = current_app.config['S3_REGION']
        return f'https://{S3_BUCKET}.s3.{S3_REGION}.amazonaws.com/{self.s3_file_name}'

    def serialize(self):
        return {
            'id': self.id,
            'content_type': self.content_type,
            'file_name': self.file_name,
            'file_size': self.file_size,
            's3_file_name': self.s3_file_name,
            's3_file_url': self.get_s3_file_url()
        }