import random
from sqlalchemy import create_engine, text
from urllib.parse import quote_plus
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from geopy.distance import geodesic
import numpy as np
from adjustText import adjust_text
import nutri as n

# Database configuration
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': quote_plus('Aditya@06'),  # URL encode the password
    'database': 'food'
}

# Create database connection string
db_url = f"mysql+pymysql://{db_config['user']}:{db_config['password']}@{db_config['host']}/{db_config['database']}"
engine = create_engine(db_url)

def calculate_distance(ngo_coords, donor_coords):
    """
    Calculate the geodesic distance between NGO and donor coordinates.
    If coordinates are identical or too close, set a default distance of 1 km.
    """
    if abs(ngo_coords[0] - donor_coords[0]) < 0.0001 and abs(ngo_coords[1] - donor_coords[1]) < 0.0001:
        print("Warning: NGO and donor have identical or very close coordinates. Setting distance to 1 km.")
        return 1.0

    distance = geodesic(ngo_coords, donor_coords).km
    print(f"Calculating distance between {ngo_coords} and {donor_coords}: {distance:.2f} km")
    return distance

def route_op():
    try:
        # Get NGO input
        ngo_name = input("Enter your NGO name: ")
        state = input("Enter your State: ").lower()

        # Query NGO data
        with engine.connect() as conn:
            ngo_query = text("SELECT latitude, longitude FROM ngos WHERE name = :name AND state = :state")
            ngo_result = conn.execute(ngo_query, {"name": ngo_name, "state": state}).fetchone()
            
            if not ngo_result:
                print(f"No NGO found with name {ngo_name} in {state}")
                return

            # Query donor data
            donor_query = text("SELECT name, latitude, longitude, quantity FROM donors WHERE state = :state")
            donors = pd.read_sql(donor_query, conn, params={"state": state})

            if donors.empty:
                print(f"No donors found in {state}")
                return

        # Create graph
        G = nx.Graph()
        ngo_coords = (float(ngo_result[0]), float(ngo_result[1]))
        
        # Add NGO node
        G.add_node('NGO', pos=ngo_coords)
        
        # Add donor nodes and calculate distances
        pos = {'NGO': ngo_coords}
        distances = {}
        
        for idx, donor in donors.iterrows():
            donor_coords = (float(donor['latitude']), float(donor['longitude']))
            donor_name = f"Donor{idx+1}"
            G.add_node(donor_name, pos=donor_coords)
            pos[donor_name] = donor_coords
            
            # Calculate distance
            distance = calculate_distance(ngo_coords, donor_coords)
            G.add_edge('NGO', donor_name, weight=distance)
            distances[donor_name] = distance

        # Find shortest paths
        shortest_paths = nx.single_source_shortest_path(G, 'NGO')
        
        # Plotting
        plt.figure(figsize=(12, 8))
        nx.draw(G, pos, with_labels=True, node_color='lightblue', 
                node_size=500, font_size=8, font_weight='bold')
        
        # Add edge labels
        edge_labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels)
        
        plt.title(f"Route Optimization for {ngo_name}")
        plt.axis('off')
        plt.show()

        # Print routes and distances
        print("\nOptimal Routes:")
        for node in G.nodes():
            if node != 'NGO':
                path = shortest_paths[node]
                distance = distances[node]
                print(f"NGO -> {node}: Distance = {distance:.2f} km")

    except Exception as e:
        print(f"Error: {str(e)}")
    finally:
        if 'conn' in locals():
            conn.close()

if __name__ == "__main__":
    route_op()