from neo4j import GraphDatabase
from neomodel import  StructuredNode, StringProperty, FloatProperty, IntegerProperty


class DataBase:


    def __init__(self):
        URI = "bolt://localhost:7687"
        USERNAME = "neo4j"
        PASSWORD = "infestation"        
        self.driver = GraphDatabase.driver(URI,auth=(USERNAME,PASSWORD))


    
    def test_connection(self):
        with self.driver.session() as session:
            result = session.run("MATCH (n) RETURN n LIMIT 5")  # Fetch sample data
            for record in result:
                print(record)



    def get_all_node_properties(self):
        query = """
        CALL db.schema.nodeTypeProperties()
        YIELD propertyName
        RETURN DISTINCT propertyName
        """
        with self.driver.session() as session:
            result = session.run(query)
            properties = [record["propertyName"] for record in result]
            return properties
        

    def close_db_connection(self):
        self.driver.close()


if __name__ == "__main__":
    properties = DataBase().get_all_node_properties()
    print(f"Node Properties {properties}")
    

