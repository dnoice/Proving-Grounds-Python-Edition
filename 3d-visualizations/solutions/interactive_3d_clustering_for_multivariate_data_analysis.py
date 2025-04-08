"""
Interactive 3D Clustering Tool with Advanced Mode

This script provides two modes for performing and visualizing clustering on the Wine dataset:
an interactive mode using a Dash web application and an advanced, command-line driven mode
that saves results to files.

Author: Dennis 'dendogg' Smaltz
Date: April 7, 2025
Version: 1.0 (Reference Only)
"""
import os
import sys
import time
import threading
import argparse
import numpy as np
import pandas as pd
from sklearn.datasets import load_wine
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
from sklearn.cluster import KMeans, DBSCAN, AgglomerativeClustering
from sklearn.metrics import silhouette_score, davies_bouldin_score
import plotly.graph_objs as go
import dash
from dash import dcc, html, Input, Output, State
import dash_bootstrap_components as dbc

# ==============================
# Create Solutions Folder
# ==============================
SOLUTIONS_FOLDER = "solutions"
if not os.path.exists(SOLUTIONS_FOLDER):
    os.makedirs(SOLUTIONS_FOLDER)

# ==============================
# Data Preparation and Preprocessing
# ==============================
def load_and_preprocess_data():
    """Loads the Wine dataset, preprocesses it by handling missing values and outliers,
    and scales the features.

    Returns:
        pd.DataFrame: A DataFrame containing the scaled features of the Wine dataset.
    """
    data = load_wine()
    df = pd.DataFrame(data.data, columns=data.feature_names)

    # Introduce 1% missing values at random for demonstration
    np.random.seed(42)
    mask = np.random.rand(*df.shape) < 0.01
    df[mask] = np.nan

    # Fill missing values with column mean
    df.fillna(df.mean(), inplace=True)

    # Remove outliers using the IQR method
    def remove_outliers(df, factor=1.5):
        """Removes outliers from each column of a DataFrame using the IQR method.

        Args:
            df (pd.DataFrame): The input DataFrame.
            factor (float, optional): The multiplier for the IQR to define the
                outlier boundaries. Defaults to 1.5.

        Returns:
            pd.DataFrame: A DataFrame with outliers removed from each column.
        """
        for col in df.columns:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            lower_bound = Q1 - factor * IQR
            upper_bound = Q3 + factor * IQR
            df = df[(df[col] >= lower_bound) & (df[col] <= upper_bound)]
        return df

    df = remove_outliers(df)

    # Normalize features using StandardScaler
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(df)
    df_scaled = pd.DataFrame(scaled_data, columns=df.columns)

    return df_scaled

# ==============================
# Dimensionality Reduction for Visualization
# ==============================
def reduce_dimensionality(df, n_components=3):
    """Applies Principal Component Analysis (PCA) to reduce the dimensionality
    of the input DataFrame for visualization purposes.

    Args:
        df (pd.DataFrame): The input DataFrame.
        n_components (int, optional): The number of principal components to
            keep. Defaults to 3.

    Returns:
        pd.DataFrame: A DataFrame containing the principal components.
    """
    pca = PCA(n_components=n_components)
    components = pca.fit_transform(df)
    comp_df = pd.DataFrame(components, columns=[f'PC{i+1}' for i in range(n_components)])
    return comp_df

# ==============================
# Clustering Functions
# ==============================
def run_kmeans(data, n_clusters=3):
    """Performs K-Means clustering on the input data.

    Args:
        data (np.ndarray): The input data array.
        n_clusters (int, optional): The number of clusters to form.
            Defaults to 3.

    Returns:
        tuple: A tuple containing:
            - np.ndarray: The cluster labels for each data point.
            - np.ndarray: The coordinates of the cluster centroids.
    """
    model = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
    labels = model.fit_predict(data)
    centroids = model.cluster_centers_
    return labels, centroids

def run_dbscan(data, eps=0.5, min_samples=5):
    """Performs DBSCAN clustering on the input data.

    Args:
        data (np.ndarray): The input data array.
        eps (float, optional): The maximum distance between two samples for one
            to be considered as in the neighborhood of the other. Defaults to 0.5.
        min_samples (int, optional): The number of samples (or total weight) in a
            neighborhood for a point to be considered as a core point.
            Defaults to 5.

    Returns:
        tuple: A tuple containing:
            - np.ndarray: The cluster labels for each data point (-1 indicates noise).
            - None: DBSCAN does not compute centroids.
    """
    model = DBSCAN(eps=eps, min_samples=min_samples)
    labels = model.fit_predict(data)
    centroids = None  # DBSCAN does not compute centroids
    return labels, centroids

def run_agglomerative(data, n_clusters=3):
    """Performs Agglomerative Hierarchical Clustering on the input data.

    Args:
        data (np.ndarray): The input data array.
        n_clusters (int, optional): The number of clusters to find.
            Defaults to 3.

    Returns:
        tuple: A tuple containing:
            - np.ndarray: The cluster labels for each data point.
            - None: Agglomerative clustering does not directly compute centroids.
    """
    model = AgglomerativeClustering(n_clusters=n_clusters)
    labels = model.fit_predict(data)
    centroids = None  # Compute centroids manually if needed
    return labels, centroids

# ==============================
# Compute Cluster Metrics
# ==============================
def compute_metrics(data, labels):
    """Computes the Silhouette Score and Davies-Bouldin Index for the clustering results.

    Args:
        data (np.ndarray): The input data array.
        labels (np.ndarray): The cluster labels assigned to each data point.

    Returns:
        tuple: A tuple containing:
            - float or None: The Silhouette Score, or None if it cannot be computed.
            - float or None: The Davies-Bouldin Index, or None if it cannot be computed.
    """
    valid_mask = labels != -1
    if np.sum(valid_mask) > 1 and len(np.unique(labels[valid_mask])) > 1:
        sil_score = silhouette_score(data[valid_mask], labels[valid_mask])
        db_score = davies_bouldin_score(data[valid_mask], labels[valid_mask])
    else:
        sil_score, db_score = None, None
    return sil_score, db_score

# ==============================
# Real-Time Data Streaming (Simulation)
# ==============================
streamed_data = None
def simulate_data_streaming(original_df):
    """Simulates real-time data streaming by incrementally adding rows from the
    original DataFrame to a global `streamed_data` DataFrame.

    Args:
        original_df (pd.DataFrame): The DataFrame to simulate streaming from.
    """
    global streamed_data
    streamed_data = original_df.copy().iloc[:50, :].reset_index(drop=True)
    def stream():
        global streamed_data
        for i in range(50, len(original_df)):
            time.sleep(0.2)  # simulate delay
            new_point = original_df.iloc[i, :].to_frame().T
            streamed_data = pd.concat([streamed_data, new_point], ignore_index=True)
    threading.Thread(target=stream, daemon=True).start()

# ==============================
# Static Advanced Mode: Run and Save Outputs
# ==============================
def run_advanced_mode(args):
    """Runs the clustering analysis in advanced mode based on command-line arguments.
    Loads data, performs dimensionality reduction, applies the selected clustering
    algorithm, computes metrics, and saves the results (metrics, clustered data,
    and visualization) to the 'solutions' folder.

    Args:
        args (argparse.Namespace): Parsed command-line arguments.
    """
    # Load and preprocess data
    df_scaled = load_and_preprocess_data()
    df_3d = reduce_dimensionality(df_scaled)
    data_combined = df_scaled.copy()
    data_combined[['PC1', 'PC2', 'PC3']] = df_3d

    # Use entire dataset for static analysis
    X_vis = data_combined[['PC1', 'PC2', 'PC3']].values

    # Run selected clustering algorithm
    if args.algorithm == "kmeans":
        labels, centroids = run_kmeans(X_vis, n_clusters=args.n_clusters)
    elif args.algorithm == "dbscan":
        labels, centroids = run_dbscan(X_vis, eps=args.dbscan_eps, min_samples=args.dbscan_min_samples)
    elif args.algorithm == "agglomerative":
        labels, centroids = run_agglomerative(X_vis, n_clusters=args.n_clusters)
    else:
        print("Invalid algorithm selected. Exiting.")
        sys.exit(1)

    # Compute metrics
    sil_score, db_score = compute_metrics(X_vis, labels)
    metrics_str = f"Silhouette Score: {sil_score:.3f}\nDavies-Bouldin Index: {db_score:.3f}" if sil_score is not None else "Cluster metrics could not be computed."
    print(metrics_str)

    # Save metrics to a file
    metrics_path = os.path.join(SOLUTIONS_FOLDER, "cluster_metrics.txt")
    with open(metrics_path, "w") as f:
        f.write(metrics_str)

    # Save clustered data points
    data_combined['Cluster'] = labels
    csv_path = os.path.join(SOLUTIONS_FOLDER, "clustered_data.csv")
    data_combined.to_csv(csv_path, index=False)

    # Create the 3D scatter plot
    fig = go.Figure()
    unique_labels = np.unique(labels)
    for label in unique_labels:
        mask = labels == label
        name = f"Cluster {label}" if label != -1 else "Noise"
        fig.add_trace(go.Scatter3d(
            x=X_vis[mask, 0],
            y=X_vis[mask, 1],
            z=X_vis[mask, 2],
            mode='markers',
            marker=dict(size=5),
            name=name
        ))
    if centroids is not None:
        fig.add_trace(go.Scatter3d(
            x=centroids[:, 0],
            y=centroids[:, 1],
            z=centroids[:, 2],
            mode='markers',
            marker=dict(size=10, symbol='diamond', color='black'),
            name="Centroids"
        ))
    fig.update_layout(
        scene=dict(
            xaxis_title='PC1',
            yaxis_title='PC2',
            zaxis_title='PC3'
        ),
        margin=dict(l=0, r=0, b=0, t=40),
        legend=dict(x=0, y=1)
    )

    # Save the visualization to an HTML file and as a static image (requires kaleido)
    html_path = os.path.join(SOLUTIONS_FOLDER, "cluster_visualization.html")
    fig.write_html(html_path)
    try:
        image_path = os.path.join(SOLUTIONS_FOLDER, "cluster_visualization.png")
        fig.write_image(image_path)
    except Exception as e:
        print("Static image export failed (kaleido not installed?):", e)

    print(f"All outputs saved to the '{SOLUTIONS_FOLDER}' folder.")

# ==============================
# Dash App for Interactive Mode
# ==============================
def run_interactive_mode():
    """Runs the interactive clustering tool using a Dash web application.
    Allows users to select a clustering algorithm and adjust its parameters
    to visualize the clustering results in 3D and view cluster metrics in real-time
    (simulated streaming).
    """
    # Load and preprocess data
    df_scaled = load_and_preprocess_data()
    df_3d = reduce_dimensionality(df_scaled)
    data_combined = df_scaled.copy()
    data_combined[['PC1', 'PC2', 'PC3']] = df_3d

    # Start simulated data streaming
    simulate_data_streaming(data_combined)

    app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
    app.title = "Interactive 3D Clustering Tool"

    app.layout = dbc.Container([
        dbc.Row([
            dbc.Col(html.H2("Interactive 3D Clustering Dashboard"), width=8),
        ], justify="center", className="my-3"),

        dbc.Row([
            dbc.Col([
                html.Label("Select Clustering Algorithm:"),
                dcc.Dropdown(
                    id="algorithm-dropdown",
                    options=[
                        {"label": "K-Means", "value": "kmeans"},
                        {"label": "DBSCAN", "value": "dbscan"},
                        {"label": "Agglomerative", "value": "agglomerative"}
                    ],
                    value="kmeans",
                    clearable=False
                ),
                html.Br(),
                html.Div(id="param-controls", children=[  # Initialize with potential controls
                    html.Div(id="n-clusters-container", style={'display': 'block'}, children=[
                        html.Label("Number of Clusters:"),
                        dcc.Slider(id="n-clusters", min=2, max=10, step=1, value=3,
                                     marks={i: str(i) for i in range(2, 11)})
                    ]),
                    html.Div(id="dbscan-params-container", style={'display': 'none'}, children=[
                        html.Label("DBSCAN eps:"),
                        dcc.Input(id="dbscan-eps", type="number", value=0.5, step=0.1),
                        html.Br(),
                        html.Label("DBSCAN min_samples:"),
                        dcc.Input(id="dbscan-min-samples", type="number", value=5, step=1)
                    ])
                ]),
                html.Br(),
                html.Button("Update Clusters", id="update-button", n_clicks=0),
                html.Br(), html.Br(),
                html.H5("Cluster Metrics:"),
                html.Div(id="cluster-metrics")
            ], width=3),
            dbc.Col([
                dcc.Graph(id="cluster-graph", style={"height": "80vh"})
            ], width=9)
        ])
    ], fluid=True)

    @app.callback(
        Output("n-clusters-container", "style"),
        Output("dbscan-params-container", "style"),
        Input("algorithm-dropdown", "value")
    )
    def update_param_visibility(algo):
        """Callback to show/hide algorithm-specific parameters based on the selected algorithm."""
        if algo in ["kmeans", "agglomerative"]:
            return {'display': 'block'}, {'display': 'none'}
        elif algo == "dbscan":
            return {'display': 'none'}, {'display': 'block'}
        return {'display': 'block'}, {'display': 'none'} # Default to KMeans style

    @app.callback(
        Output("cluster-graph", "figure"),
        Output("cluster-metrics", "children"),
        Input("update-button", "n_clicks"),
        State("algorithm-dropdown", "value"),
        State("n-clusters", "value"),
        State("dbscan-eps", "value"),
        State("dbscan-min-samples", "value")
    )
    def update_clusters(n_clicks, algorithm, n_clusters, dbscan_eps, dbscan_min_samples):
        """Callback to update the 3D scatter plot and cluster metrics based on
        the selected algorithm and its parameters.
        """
        global streamed_data
        current_data = streamed_data if streamed_data is not None else data_combined
        X_vis = current_data[['PC1', 'PC2', 'PC3']].values

        if algorithm == "kmeans":
            labels, centroids = run_kmeans(X_vis, n_clusters=n_clusters if n_clusters else 3)
        elif algorithm == "dbscan":
            labels, centroids = run_dbscan(X_vis, eps=dbscan_eps if dbscan_eps else 0.5,
            min_samples=dbscan_min_samples if dbscan_min_samples else 5)
        elif algorithm == "agglomerative":
            labels, centroids = run_agglomerative(X_vis, n_clusters=n_clusters if n_clusters else 3)
        else:
            labels, centroids = run_kmeans(X_vis, n_clusters=3)

        sil_score, db_score = compute_metrics(X_vis, labels)
        metric_info = [
            html.P(f"Silhouette Score: {sil_score:.3f}" if sil_score is not None else "Silhouette Score: N/A"),
            html.P(f"Davies-Bouldin Index: {db_score:.3f}" if db_score is not None else "Davies-Bouldin Index: N/A"),
            html.P(f"Number of Clusters: {len(np.unique(labels[labels != -1])) if algorithm=='dbscan' else (n_clusters if algorithm in ['kmeans', 'agglomerative'] else 'N/A')}")
        ]

        fig = go.Figure()
        unique_labels = np.unique(labels)
        for label in unique_labels:
            mask = labels == label
            name = f"Cluster {label}" if label != -1 else "Noise"
            fig.add_trace(go.Scatter3d(
                x=X_vis[mask, 0],
                y=X_vis[mask, 1],
                z=X_vis[mask, 2],
                mode='markers',
                marker=dict(size=5),
                name=name
            ))
        if centroids is not None:
            fig.add_trace(go.Scatter3d(
                x=centroids[:, 0],
                y=centroids[:, 1],
                z=centroids[:, 2],
                mode='markers',
                marker=dict(size=10, symbol='diamond', color='black'),
                name="Centroids"
            ))
        fig.update_layout(
            scene=dict(
                xaxis_title='PC1',
                yaxis_title='PC2',
                zaxis_title='PC3'
            ),
            margin=dict(l=0, r=0, b=0, t=40),
            legend=dict(x=0, y=1)
        )
        return fig, metric_info

    app.run(debug=True)

# ==============================
# Command Line Interface
# ==============================
def main():
    """Main function to parse command-line arguments and run either the
    advanced or interactive mode of the clustering tool.
    """
    parser = argparse.ArgumentParser(
        description="Interactive 3D Clustering Tool - Advanced and Interactive Modes",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("--mode", type=str, choices=["advanced", "interactive"], default="interactive",
                        help="Choose 'advanced' for command-line driven clustering or 'interactive' for guided Dash UI")
    parser.add_argument("--algorithm", type=str, choices=["kmeans", "dbscan", "agglomerative"], default="kmeans",
                        help="Clustering algorithm to use (advanced mode only)")
    parser.add_argument("--n_clusters", type=int, default=3,
                        help="Number of clusters for KMeans or Agglomerative (advanced mode only)")
    parser.add_argument("--dbscan_eps", type=float, default=0.5,
                        help="Epsilon parameter for DBSCAN (advanced mode only)")
    parser.add_argument("--dbscan_min_samples", type=int, default=5,
                        help="Min samples parameter for DBSCAN (advanced mode only)")
    args = parser.parse_args()

    if args.mode == "advanced":
        try:
            run_advanced_mode(args)
        except Exception as e:
            print("An error occurred in advanced mode:", e)
            sys.exit(1)
    else:
        # For interactive mode, print helpful messages and then run the interactive app.
        print("Launching Interactive Mode...")
        print("Use the dashboard controls to select clustering algorithm and adjust parameters.")
        run_interactive_mode()

if __name__ == '__main__':
    main()
