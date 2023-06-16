from rdflib import Graph
from pathlib import Path

# Create a Graph
g = Graph()

# Parse in an RDF file hosted on the Internet
g.parse(f'file://{Path(__file__).parent.resolve()}/linkedmdb-latest-dump/linkedmdb-latest-dump.nt')

# Loop through each triple in the graph (subj, pred, obj)
for subj, pred, obj in g:
    # Check if there is at least one triple in the Graph
    if (subj, pred, obj) not in g:
       raise Exception("It better be!")

# Print the number of "triples" in the Graph
print(f"Graph g has {len(g)} statements.")
# Prints: Graph g has 86 statements.

# Print out the entire Graph in the RDF Turtle format
# print(g.serialize(format="turtle"))
