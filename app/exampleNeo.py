from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
driver = GraphDatabase.driver(uri, auth=("neo4j", "tenaciousD"), encrypted=False)

def create_person(tx, name):
    tx.run("CREATE (a:Person {name: $name})", name=name)

def create_friend_of(tx, name, friend):
    tx.run("MATCH (a:Person) WHERE a.name = $name "
           "CREATE (a)-[:KNOWS]->(:Person {name: $friend})",
           name=name, friend=friend)

with driver.session() as session:
    session.write_transaction(create_person, "Alice")
    session.write_transaction(create_friend_of, "Alice", "Bob")
    session.write_transaction(create_friend_of, "Alice", "Carl")

driver.close()

print("Try running the following query:")
print("match (n)-[m]-(k) return n,m,k;")