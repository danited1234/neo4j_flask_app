from flask import Blueprint,jsonify
from .db import DataBase

db = DataBase()
queries = Blueprint("queries",__name__)


@queries.route("/get_all_projects",methods=["GET"])
def get_all_projects():
    try:
        projects = db.get_all_projects()
        projects_dict = [project.__properties__  for project in projects]
        
        return jsonify (projects_dict), 200
    except Exception as e:
        return jsonify ({"error":f"{e}"}), 500


@queries.route("/get_all_tokens",methods=["GET"])
def get_all_tokens():
    try:
        tokens = db.get_all_tokens()
        if tokens:
            tokens_dict = [token.__dict__ for token in tokens]
            return jsonify (tokens_dict), 200
        
        return jsonify ({"message":"No Data Found"})
    except Exception as e:
        return jsonify ({"error":f"{e}"}), 500
    

@queries.route("/get_all_files_in_project_one",methods=["GET"])
def get_all_files_in_project_one():
    try:
        files = db.get_all_files_in_project_one()
        if files:
            files_dict = [file.__dict__ for file in files]
            return jsonify (files_dict), 200

        return jsonify ({"message":"No Data Found"})
    except Exception as e:
        return jsonify ({"error":f"{e}"}), 500
    

