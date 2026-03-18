import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


# Load data and clean
data = pd.read_csv("data/traffic_crashes.csv")

# Select Longitude and Latitude columns 
data = data[['tb_latitude','tb_longitude','collision_time']]

# Remove rows missing Latitude or Longitude
data = data.dropna()

# Initilize data variable X
X = data[['tb_latitude','tb_longitude']]

# Initialize KMeans algorithm with 20 clusters to see hot spots
kmeans20 = KMeans(n_clusters=30, random_state=61)

# Run clustering
data['cluster20'] = kmeans20.fit_predict(X)

# Count crashes per cluster
cluster20_counts = data['cluster20'].value_counts()

# Identify 5 worst clusters
worst_clusters = cluster20_counts.head(5).index
print("Top 5 high risk clusters:", worst_clusters)

# Map cluster size to each point
data['cluster20_size'] = data['cluster20'].map(cluster20_counts)

plt.figure()

# Create scatter plot colored by crash density
plt.scatter(data['tb_longitude'], data['tb_latitude'], c=data['cluster20_size'], cmap='RdYlBu_r', s=10)

# Create a hot and cold colorbar
plt.colorbar(label="Number of Crashes in Cluster")

# Add centroids for numbering each cluster
plt.scatter(kmeans20.cluster_centers_[:,1], kmeans20.cluster_centers_[:,0], color='black', marker='X', s=100, label='Centroids')

# Add rank numbers to clusters
for i, (lat, lon) in enumerate(kmeans20.cluster_centers_):
    if i in worst_clusters:
        plt.text(lon, lat, str(i), fontsize=12, color='red', weight='bold')

# Configure plot
plt.title("Vehicle Crash Clusters in San Francisco")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.xlim(-122.52, -122.35)
plt.ylim(37.70, 37.84)

# Save plot
plt.savefig("results/crash_clusters20.png")

# Extract the hour from the time to evaluate most dangerous times of day
data['hour'] = pd.to_datetime(data['collision_time'], format='%H:%M:%S').dt.hour

# Filter for worst clusters
high_risk_data = data[data['cluster20'].isin(worst_clusters)]

# Plot accidents by hour
for cluster_id in worst_clusters:
    
    # Filter data for this specific cluster
    cluster_data = data[data['cluster20'] == cluster_id]
    
    # Group by hour
    hourly_counts = cluster_data.groupby('hour').size()
    hourly_counts = hourly_counts.sort_index()
    
    # Create plot
    plt.figure()
    hourly_counts.plot(kind='bar', colormap='coolwarm')
    
    plt.xlabel('Hour of Day')
    plt.ylabel('Number of Crashes')
    plt.title(f'Accidents by Hour (Cluster {cluster_id})')
	
    # Save each hourly bar chart
    plt.savefig(f"results/hourly_cluster_{cluster_id}.png")
	


# Show plot
plt.show()