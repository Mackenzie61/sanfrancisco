# San Francisco.

Data Mining course project based on the data sets from https://data.sfgov.org/





San Francisco Crash Analysis using Clustering





Overview

This project analyzes traffic crash data in San Francisco to identify high risk locations and patterns in crash occurrences. Using clustering techniques, the project groups crash locations into geographic clusters, identifies the most dangerous areas based on crash density and plots the number of crashes for each hour of the day for the worst 5 clusters.



The goal is to assist new residents and tourists in understanding where and when to avoid driving a vehicle in San Francisco.



Aim

The aim of this project is to identify high-risk areas in San Francisco by analyzing traffic crash data and discovering patterns in both location and time.



This project answers:

\- Where do traffic crashes cluster geographically in San Francisco?

\- What are the top 5 most dangerous clusters to drive in?

\- When do crashes most frequently occur in high-risk areas?



This contributes to improving public safety awareness and can help guide safer navigation and planning decisions.





Data Source

Data was obtained from the San Francisco Open Data Portal:



Traffic Crashes Dataset:  

&#x20; https://data.sfgov.org/Public-Safety/Traffic-Crashes-Resulting-in-Injury/ubvf-ztfx





Methodology



1\. Data Preprocessing

\- Selected relevant columns: latitude, longitude, collision time

\- Removed missing values

\- Flipped one positive longitude to negative

\- Converted collision time into hour of the day



2\. Clustering (Data Mining Task)

\- Applied K-Means clustering to group crash locations

\- Used 30 clusters to identify detailed crash hotspots

\- Identified the top 5 clusters with the highest crash counts



3\. Analysis

\- Mapped cluster density to visualize high risk areas

\- Extracted hourly crash patterns for each high risk cluster

\- Generated visualizations for spatial and temporal analysis



\---



Tools \& Libraries

\- Python

\- pandas

\- matplotlib

\- scikit-learn



\---



How to Run



1\. Install dependencies



pip install pandas matplotlib scikit-learn

