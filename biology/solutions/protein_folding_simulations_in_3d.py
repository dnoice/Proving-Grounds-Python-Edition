#!/usr/bin/env python
"""
Robust Protein Folding Simulation Framework
---------------------------------------------
This script implements:
1. Protein sequence setup and validation.
2. Modeling simplified folding forces (hydrophobic, hydrogen bonding,
   van der Waals, and electrostatic interactions).
3. A Monte Carlo simulation for folding with energy minimization and free energy tracking.
4. 3D visualization of the final folded structure and energy landscape.
5. Exploratory functions for folding variability (misfolding simulation, real data integration, and ML prediction).

Run this script to simulate a folding process from a linear chain to a folded structure.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # needed for 3D plotting
import random
from sklearn.linear_model import LinearRegression

# ---------------------------
# Task 1: Setting Up Protein Sequence
# ---------------------------
VALID_AMINO_ACIDS = set("ACDEFGHIKLMNPQRSTVWY")  # 20 standard amino acids

def validate_sequence(seq):
    """Validate that the protein sequence only contains valid amino acid codes."""
    for aa in seq:
        if aa not in VALID_AMINO_ACIDS:
            raise ValueError(f"Invalid amino acid found: {aa}")
    return True

def create_protein_dataframe(seq):
    """
    Store the sequence in a pandas DataFrame for structured representation.
    Each residue is stored with its index and code.
    """
    data = {"Index": list(range(len(seq))), "Residue": list(seq)}
    df = pd.DataFrame(data)
    return df

# ---------------------------
# Task 2: Modeling the Folding Forces
# ---------------------------
# Simplified interaction coefficients for demonstration
HYDROPHOBICITY = {
    'A': 1.8, 'C': 2.5, 'D': -3.5, 'E': -3.5, 'F': 2.8, 
    'G': -0.4, 'H': -3.2, 'I': 4.5, 'K': -3.9, 'L': 3.8,
    'M': 1.9, 'N': -3.5, 'P': -1.6, 'Q': -3.5, 'R': -4.5,
    'S': -0.8, 'T': -0.7, 'V': 4.2, 'W': -0.9, 'Y': -1.3
}

def calculate_interaction_energy(seq, positions):
    """
    Calculate the total interaction energy for the current configuration.
    
    For simplicity:
    - Hydrophobic interactions: Favor clustering of nonpolar residues.
    - Hydrogen bonds: Reward if polar residues are at optimal distance.
    - van der Waals: Simulated using a simplified Lennard-Jones-like term.
    - Electrostatic: Simple Coulomb-like repulsion/attraction for charged residues.
    
    Note: This is a highly simplified model and uses arbitrary parameters.
    """
    energy = 0.0
    n = len(seq)
    # Constants (arbitrary units)
    hydro_coeff = -0.5
    hbond_coeff = -1.0
    vdw_coeff = 0.1
    electro_coeff = 0.2
    optimal_distance = 1.5
    
    # For simplicity, assume charges: D, E = -1; K, R = +1; others 0.
    charges = {aa: (1 if aa in "KR" else -1 if aa in "DE" else 0) for aa in VALID_AMINO_ACIDS}
    
    for i in range(n):
        for j in range(i+1, n):
            # Euclidean distance
            dist = np.linalg.norm(positions[i] - positions[j])
            if dist == 0:
                continue  # avoid division by zero
            
            # Hydrophobic term: if both residues are hydrophobic (hydrophobicity > 0), lower energy when close
            if HYDROPHOBICITY[seq[i]] > 0 and HYDROPHOBICITY[seq[j]] > 0:
                energy += hydro_coeff * (HYDROPHOBICITY[seq[i]] + HYDROPHOBICITY[seq[j]]) / dist
            
            # Hydrogen bonding: if residues are polar (hydrophobicity < 0) and near optimal distance
            if HYDROPHOBICITY[seq[i]] < 0 and HYDROPHOBICITY[seq[j]] < 0 and abs(dist - optimal_distance) < 0.5:
                energy += hbond_coeff
            
            # van der Waals: simplified Lennard-Jones potential style (repulsive if too close, attractive if near optimal)
            vdw_energy = vdw_coeff * ((optimal_distance / dist)**12 - 2 * (optimal_distance / dist)**6)
            energy += vdw_energy
            
            # Electrostatic: Coulomb-like interaction if either residue is charged
            energy += electro_coeff * charges[seq[i]] * charges[seq[j]] / dist

    return energy

# ---------------------------
# Task 3: Simulating the Folding Process
# ---------------------------
def initialize_positions(seq):
    """
    Initialize a linear chain of positions in 3D (e.g., along the x-axis)
    Each residue starts one unit apart.
    """
    n = len(seq)
    positions = np.array([[i, 0.0, 0.0] for i in range(n)])
    return positions

def monte_carlo_folding(seq, init_positions, steps=1000, temperature=1.0):
    """
    Perform a Monte Carlo simulation to explore folding configurations.
    - At each step, a random residue is moved a small random delta.
    - The new configuration is accepted if it lowers the energy, or probabilistically if not.
    - Track energy and intermediate states.
    
    Returns:
        best_positions: Configuration with the lowest energy encountered.
        energy_trajectory: List of energies over iterations.
        positions_history: List of positions for visualization.
    """
    current_positions = np.copy(init_positions)
    current_energy = calculate_interaction_energy(seq, current_positions)
    best_energy = current_energy
    best_positions = np.copy(current_positions)
    
    energy_trajectory = [current_energy]
    positions_history = [np.copy(current_positions)]
    
    for step in range(steps):
        # Select a random residue to move
        i = random.randint(0, len(seq)-1)
        new_positions = np.copy(current_positions)
        # Random displacement in each dimension (scale can be adjusted)
        delta = np.random.uniform(-0.5, 0.5, 3)
        new_positions[i] += delta
        
        new_energy = calculate_interaction_energy(seq, new_positions)
        delta_E = new_energy - current_energy
        
        # Metropolis criterion
        if delta_E < 0 or np.exp(-delta_E / temperature) > random.random():
            current_positions = new_positions
            current_energy = new_energy
            # Update best configuration if improved
            if current_energy < best_energy:
                best_energy = current_energy
                best_positions = np.copy(current_positions)
        
        energy_trajectory.append(current_energy)
        if step % 50 == 0:  # store intermediate state every 50 iterations
            positions_history.append(np.copy(current_positions))
    
    return best_positions, energy_trajectory, positions_history

# ---------------------------
# Task 4: Visualizing the Protein in 3D
# ---------------------------
def plot_protein_3d(positions, seq, title="Protein Structure"):
    """
    Visualize the protein structure in 3D.
    Color codes can be added based on properties (e.g., hydrophobicity).
    """
    fig = plt.figure(figsize=(16, 9))  # widescreen format
    ax = fig.add_subplot(111, projection='3d')
    
    # Map color based on hydrophobicity: hydrophobic (blue) vs polar (red)
    colors = ['blue' if HYDROPHOBICITY[aa] > 0 else 'red' for aa in seq]
    
    xs, ys, zs = positions[:,0], positions[:,1], positions[:,2]
    ax.scatter(xs, ys, zs, c=colors, s=100)
    ax.plot(xs, ys, zs, color='gray', linestyle='--')  # connect the dots
    
    ax.set_title(title)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    plt.show()

def plot_energy_trajectory(energy_trajectory):
    """Plot the energy trajectory over simulation steps."""
    plt.figure(figsize=(16, 9))
    plt.plot(energy_trajectory, lw=2)
    plt.xlabel("Simulation Step")
    plt.ylabel("Interaction Energy")
    plt.title("Energy Trajectory During Folding")
    plt.grid(True)
    plt.show()

# ---------------------------
# Task 5: Exploring Folding Variability
# ---------------------------
def simulate_misfolding(seq, mutation_index, new_residue):
    """
    Simulate misfolding by mutating one residue and re-running the folding simulation.
    """
    mutated_seq = list(seq)
    mutated_seq[mutation_index] = new_residue
    mutated_seq = "".join(mutated_seq)
    print(f"Simulating misfolding: Mutation at index {mutation_index} -> {new_residue}")
    init_positions = initialize_positions(mutated_seq)
    best_positions, energy_traj, pos_history = monte_carlo_folding(mutated_seq, init_positions, steps=800)
    return mutated_seq, best_positions, energy_traj, pos_history

def energy_landscape_exploration(seq, iterations=10):
    """
    Explore the energy landscape by running several simulations with random perturbations.
    Returns a list of best energies.
    """
    energies = []
    for _ in range(iterations):
        init_positions = initialize_positions(seq)
        best_positions, energy_traj, _ = monte_carlo_folding(seq, init_positions, steps=500)
        energies.append(calculate_interaction_energy(seq, best_positions))
    # Plotting the energy landscape
    plt.figure(figsize=(16, 9))
    plt.hist(energies, bins=10, edgecolor='black')
    plt.xlabel("Best Energy Found")
    plt.ylabel("Frequency")
    plt.title("Energy Landscape Exploration")
    plt.show()
    return energies

def integrate_real_protein_data(pdb_filename):
    """
    Stub for integrating real protein data from a PDB file.
    In practice, use Bio.PDB from Biopython to parse the PDB and extract atom coordinates.
    """
    print(f"Integrating real protein data from: {pdb_filename}")
    # Dummy return: in a real implementation, parse the PDB file.
    return None

def machine_learning_prediction(feature_matrix, target_vector):
    """
    Train a simple linear regression model to predict folding efficiency (or energy)
    based on sequence features.
    
    For demonstration, the features could be:
        - Sequence length
        - Average hydrophobicity
    """
    model = LinearRegression()
    model.fit(feature_matrix, target_vector)
    predictions = model.predict(feature_matrix)
    print("ML model trained. Sample predictions:")
    print(predictions[:5])
    return model, predictions

def extract_features(seq):
    """
    Extract simple features from the sequence:
    - Length of the sequence.
    - Average hydrophobicity.
    """
    length = len(seq)
    avg_hydro = np.mean([HYDROPHOBICITY[aa] for aa in seq])
    return np.array([length, avg_hydro])

def real_time_folding_simulation_interface():
    """
    Stub for a real-time interactive folding simulation.
    In practice, you might use ipywidgets or a GUI framework like PyQt to allow user interaction.
    """
    print("Launching interactive real-time folding simulation (stub).")
    # Placeholder for real-time simulation interface
    return

# ---------------------------
# Main Execution
# ---------------------------
def main():
    # Define a sample protein sequence
    protein_seq = "ACDEFGHIKLMNPQRSTVWY"  # 20-residue sequence
    try:
        validate_sequence(protein_seq)
    except ValueError as e:
        print(e)
        return
    
    # Store sequence in a DataFrame (Task 1)
    df_sequence = create_protein_dataframe(protein_seq)
    print("Protein sequence DataFrame:")
    print(df_sequence)
    
    # Initialize positions (linear chain)
    init_positions = initialize_positions(protein_seq)
    
    # Run Monte Carlo folding simulation (Task 3)
    best_positions, energy_traj, pos_history = monte_carlo_folding(protein_seq, init_positions, steps=1000)
    print(f"Final energy: {energy_traj[-1]:.2f}")
    
    # Visualize final protein structure (Task 4)
    plot_protein_3d(best_positions, protein_seq, title="Final Folded Protein Structure")
    
    # Plot energy trajectory
    plot_energy_trajectory(energy_traj)
    
    # Explore energy landscape (Task 5)
    energies = energy_landscape_exploration(protein_seq, iterations=15)
    
    # Simulate misfolding by mutating residue at index 5
    mutated_seq, mutated_positions, mutated_energy_traj, mutated_history = simulate_misfolding(protein_seq, mutation_index=5, new_residue='W')
    plot_protein_3d(mutated_positions, mutated_seq, title="Misfolded Protein Structure")
    plot_energy_trajectory(mutated_energy_traj)
    
    # Machine learning prediction demo using dummy data
    # For demonstration, create a dummy dataset with features from several random sequences.
    dummy_seqs = [protein_seq, mutated_seq, protein_seq[::-1]]
    feature_matrix = np.array([extract_features(seq) for seq in dummy_seqs])
    # Dummy target: using final energies from simulations
    target_vector = np.array([energy_traj[-1], mutated_energy_traj[-1], energy_traj[-1] + 5])
    model, predictions = machine_learning_prediction(feature_matrix, target_vector)
    
    # Stub for real-time simulation interface (Task 5)
    real_time_folding_simulation_interface()
    
if __name__ == "__main__":
    main()
  
