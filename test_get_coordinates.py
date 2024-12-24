import random
from sqlalchemy import create_engine
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from geopy.distance import geodesic
import numpy as np
from adjustText import adjust_text
from urllib.parse import quote_plus  


db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Aditya@06',
    'database': 'food',
}


password = quote_plus(db_config['password'])
engine = create_engine(f"mysql+pymysql://{db_config['user']}:{password}@{db_config['host']}/{db_config['database']}")

def calculate_distance(ngo_coords, donor_coords):
    """
    Calculate the geodesic distance between NGO and donor coordinates.
    """
    if ngo_coords == donor_coords:  
        return 0
    distance = geodesic(ngo_coords, donor_coords).km
    print(f"Calculating distance between {ngo_coords} and {donor_coords}: {distance:.2f} km")
    return distance

def route_op():
    """
    Main function to calculate and display optimized routes for an NGO.
    """
    ngo_name = input("Enter your NGO name: ")
    ngo_state = input("Enter your State: ")

    
    try:
        ngo_data = pd.read_sql(
            "SELECT NGO_name, Latitude, Longitude FROM Recipient WHERE LOWER(NGO_name) = %s AND LOWER(State) = %s",
            con=engine,
            params=(ngo_name.lower(), ngo_state.lower())
        )
        if ngo_data.empty:
            print("No NGO found with the provided details.")
            return
        ngo_coords = (ngo_data['Latitude'].iloc[0], ngo_data['Longitude'].iloc[0])
        print(f"NGO Coordinates: {ngo_coords}")
    except Exception as e:
        print(f"Error fetching NGO data: {e}")
        return

    
    try:
        donor_data = pd.read_sql(
            "SELECT NameOfRestaurant, Latitude, Longitude, State FROM Donor WHERE LOWER(State) = %s",
            con=engine,
            params=(ngo_state.lower(),)
        )

        if donor_data.empty:
            print("No donors found in the specified state.")
            return
    except Exception as e:
        print(f"Error fetching donor data: {e}")
        return

    
    donor_data = donor_data.drop_duplicates(subset=['Latitude', 'Longitude'])

    
    distances = []
    for _, donor_row in donor_data.iterrows():
        donor_coords = (donor_row['Latitude'], donor_row['Longitude'])
        distance = calculate_distance(ngo_coords, donor_coords)
        if distance > 0:  
            distances.append((donor_row['NameOfRestaurant'], distance))

    if not distances:
        print("No valid donors within a reasonable distance.")
        return

    
    distances.sort(key=lambda x: x[1])
    closest_donor = distances[0]
    print(f"The nearest restaurant to {ngo_name} ({ngo_state}) is: {closest_donor[0]} at a distance of {closest_donor[1]:.2f} km.")

    
    G = nx.Graph()
    for donor_name, distance in distances:
        G.add_edge(ngo_name, donor_name, weight=round(distance, 2))

    
    min_distance = min([d[1] for d in distances])
    max_distance = max([d[1] for d in distances])

    if min_distance == max_distance:
        print("All donors are at the same distance from the NGO. Skipping normalization.")
        normalized_distances = [1] * len(distances)  
    else:
        normalized_distances = [0.5 + (d[1] - min_distance) / (max_distance - min_distance) * 1.5 for d in distances]

    
    pos = {ngo_name: (0, 0)}  
    num_donors = len(donor_data)
    angle_step = 2 * np.pi / num_donors

    for i, (donor_name, _) in enumerate(distances):
        distance_scaled = normalized_distances[i]
        angle = i * angle_step + random.uniform(-0.1, 0.1)  
        x = distance_scaled * np.cos(angle) + random.uniform(-0.1, 0.1)  
        y = distance_scaled * np.sin(angle) + random.uniform(-0.1, 0.1)
        pos[donor_name] = (x, y)

    
    plt.figure(figsize=(12, 8))
    nx.draw(G, pos, with_labels=False, node_size=1000, node_color='skyblue')
    labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels, font_size=8)

    
    texts = [plt.text(x, y, s, fontsize=10, weight='bold') for s, (x, y) in pos.items()]
    adjust_text(texts, arrowprops=dict(arrowstyle='->', color='red'))

    
    nx.draw_networkx_labels(G, {ngo_name: pos[ngo_name]}, labels={ngo_name: ngo_name}, font_size=14, font_color='red', font_weight='bold')

    plt.title("Routes Graph with Adjusted Nodes and Labels")
    plt.show()

    
    mst = nx.minimum_spanning_tree(G)
    plt.figure(figsize=(12, 8))
    nx.draw(mst, pos, with_labels=False, node_size=1000, node_color='lightgreen')
    nx.draw_networkx_edge_labels(mst, pos, edge_labels=nx.get_edge_attributes(mst, 'weight'), font_size=8)

    
    texts_mst = [plt.text(x, y, s, fontsize=10, weight='bold') for s, (x, y) in pos.items()]
    adjust_text(texts_mst, arrowprops=dict(arrowstyle='->', color='blue'))

    nx.draw_networkx_labels(mst, {ngo_name: pos[ngo_name]}, labels={ngo_name: ngo_name}, font_size=14, font_color='red', font_weight='bold')

    plt.title("Optimized MST Graph with Adjusted Nodes and Labels")
    plt.show()

if __name__ == "__main__":
    route_op()
