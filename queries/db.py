from neo4j import GraphDatabase
from neomodel import config
from .models import Project, RegistrationToken
import os

class DataBase:


    def __init__(self):
        URI = "bolt://localhost:7687"
        USERNAME = "neo4j"
        PASSWORD = "infestation"        
        self.driver = GraphDatabase.driver(URI,auth=(USERNAME,PASSWORD))
        config.DATABASE_URL = URI.replace("bolt://", f"bolt://{USERNAME}:{PASSWORD}@")


    def get_all_projects(self) -> list:
        projects = Project.nodes.all()
        return projects
    

    def get_all_tokens(self) -> list:
        tokens = RegistrationToken.nodes.all()
        return tokens
    
    def get_all_files_in_project_one(self) -> list:
        project = Project.nodes.get(name="Project 1")
        files = project.has_files.all()
        return files

    def close_db_connection(self):
        self.driver.close()


    def get_images_by_google_id(self):
        query = """
        MATCH (u:User)-[:UPLOADED_BY]->(f:File)
        WHERE u.id_str = "102718630068735143796"  AND f.width = 200
        RETURN f.file_name, f.file_path_loc, f.created_at, f.size
        """
        with self.driver.session() as session:
            result = session.run(query)
            return [record.data() for record in result]
        return result

    
# if __name__ == "__main__":
#     db = DataBase()
#     files = db.get_all_files_in_project_one()
#     print(files)