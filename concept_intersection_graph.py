from pyvis.network import Network
import networkx as nx
import matplotlib.pyplot as plt
import json

# Load entities and ideas from JSON files
with open('entities.json', 'r') as f:
    entities = json.load(f)['entities']

with open('idea_definitions.json', 'r') as f:
    idea_definitions = json.load(f)['idea_definitions']


# Create a NetworkX graph
G = nx.Graph()
# Add common idea nodes (in grey) with tooltips
common_ideas = set()
for entity, ideas in entities.items():
    common_ideas.update(ideas["common"])
for idea in common_ideas:
    definition = idea_definitions.get(idea, {}).get("definition", "No definition available")
    G.add_node(idea, color='grey', title=definition)

# Add unique idea nodes (with unique colors) with tooltips
unique_colors = plt.get_cmap('tab20', len(entities))  # Correct way to generate a colormap with enough unique colors
unique_idea_nodes = {}
for idx, (entity, ideas) in enumerate(entities.items()):
    color = unique_colors(idx)
    for unique_idea in ideas["unique"]:
        definition = idea_definitions.get(unique_idea, {}).get("definition", "No definition available")
        G.add_node(unique_idea, color=color, title=definition)
        unique_idea_nodes[unique_idea] = color

# Add entity nodes and edges to common and unique ideas
for entity, ideas in entities.items():
    G.add_node(entity, color='yellow', title=f"Entity: {entity}")
    for idea in ideas["common"]:
        G.add_edge(entity, idea)
    for unique_idea in ideas["unique"]:
        G.add_edge(entity, unique_idea)

# Initialize pyvis network
net = Network(height='2000px', width='100%', bgcolor='#222222', font_color='white')

# Load NetworkX graph into pyvis network
net.from_nx(G)

# Set physics options
net.show_buttons(filter_=['physics'])

# Generate and save the network graph in HTML
output_file = 'channeled_entities_network.html'
net.save_graph(output_file)

# Create the HTML table of ideas
table_html = """
<h2>List of Unique and Common Ideas</h2>
<table border="1" cellpadding="10" cellspacing="0" style="width: 100%; margin-top: 50px;">
    <tr>
        <th style="background-color: #f2f2f2;">Idea</th>
        <th style="background-color: #f2f2f2;">Type</th>
        <th style="background-color: #f2f2f2;">Definition</th>
        <th style="background-color: #f2f2f2;">Source</th>
    </tr>
"""

# Add common ideas to the table
for idea in common_ideas:
    definition = idea_definitions.get(idea, {}).get("definition", "No definition available")
    source = idea_definitions.get(idea, {}).get("source", "Source not available")
    table_html += f"""
    <tr>
        <td>{idea}</td>
        <td>Common</td>
        <td>{definition}</td>
        <td>{source}</td>
    </tr>
    """

# Add unique ideas to the table
for idea in unique_idea_nodes:
    definition = idea_definitions.get(idea, {}).get("definition", "No definition available")
    source = idea_definitions.get(idea, {}).get("source", "Source not available")
    table_html += f"""
    <tr>
        <td>{idea}</td>
        <td>Unique</td>
        <td>{definition}</td>
        <td>{source}</td>
    </tr>
    """

table_html += "</table>"

# Create the full HTML content with CSS for separation
full_html = f"""
<html>
<head>
    <style>
        body {{
            font-family: Arial, sans-serif;
        }}
        #network {{
            margin-bottom: 50px;
        }}
    </style>
</head>
<body>
    <div id="network">
        {net.html}
    </div>
    {table_html}
</body>
</html>
"""

# Write the full HTML content to the file
with open(output_file, "w") as f:
    f.write(full_html)

print(f"Interactive graph and table saved as {output_file}. You can open it in your web browser.")