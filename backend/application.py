from flask import Flask
from config import Config
from extensions import db
from routes import main
from routes.api import api
from routes.ai import ai
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from models import Conversation, User, Document, Message
import os
from pinecone import Pinecone, ServerlessSpec
from llama_index.vector_stores import PineconeVectorStore

def create_app(config_class=Config):
    application = Flask(__name__)
    application.config.from_object(config_class)

    CORS(application)
    db.init_app(application)

    application.register_blueprint(main)
    application.register_blueprint(api, url_prefix='/api')
    application.register_blueprint(ai, url_prefix='/ai')

    jwt = JWTManager(application)

    pinecone_api_key = application.config['PINECONE_API_KEY']

    pc = Pinecone(api_key=pinecone_api_key)
    index_name = application.config['PINECONE_INDEX_NAME']
    index = pc.Index(index_name)

    #pc_reader = PineconeReader(api_key=pinecone_api_key)

    application.index = index
    #application.pc_reader = pc_reader

    return application

application = create_app()

if __name__ == '__main__':
    application.run(debug=True)