# Calculating Orbital Parameters for Celestial Bodies

This challenge involves applying principles of celestial mechanics to compute key orbital parameters of celestial bodies. Participants will derive values such as the semi-major axis, eccentricity, orbital period, and other dynamical properties using Kepler's laws and Newtonian gravitation.

---

## 📝 Problem Title

**Calculating Orbital Parameters for Celestial Bodies: A Celestial Mechanics Challenge**

*Instructions:*  
Develop a Python-based simulation and analysis that calculates the orbital parameters of a celestial object given input data such as its position and velocity vectors, or information about its orbit. Use analytical methods based on Kepler’s laws and Newtonian gravity to derive parameters like semi-major axis, eccentricity, orbital period, periapsis, and apoapsis. Document your methodology and compare the computed results with expected theoretical values (or known data for real celestial bodies).

---

## 🌍 Scenario

Celestial mechanics is fundamental to understanding the motion of bodies in space—from satellites orbiting the Earth to planets revolving around the Sun. In this challenge, you are tasked with computing orbital parameters given specific orbital data. For instance, using the vis-viva equation and conservation of angular momentum, you will determine the characteristics of an elliptical orbit. This problem bridges theoretical physics and practical computation, offering insights into orbital dynamics and system modeling.

---

## 🔧 Problem Tasks

1. **Defining the System and Input Parameters**  
   - **Task 1-a:** Choose a celestial object or satellite and define the input parameters (e.g., initial position vector, velocity vector, or known orbital points such as periapsis and apoapsis).  
   - **Task 1-b:** Specify the physical constants required, including the gravitational parameter \( \mu = GM \) (for example, for Earth, \( \mu \approx 3.986 \times 10^{14} \, \text{m}^3/\text{s}^2 \)).

2. **Deriving the Orbital Parameters**  
   - **Task 2-a:** Implement the vis-viva equation:  
     \[
     v^2 = \mu \left(\frac{2}{r} - \frac{1}{a}\right)
     \]
     to solve for the semi-major axis \( a \).  
   - **Task 2-b:** Calculate the orbit eccentricity \( e \) using the relationship between the specific angular momentum, energy, and orbital parameters.  
   - **Task 2-c:** Compute the orbital period \( T \) using Kepler's third law:  
     \[
     T = 2\pi\sqrt{\frac{a^3}{\mu}}
     \]
   - **Task 2-d:** Determine the distances at periapsis and apoapsis:  
     \[
     r_{\text{per}} = a(1 - e) \quad \text{and} \quad r_{\text{apo}} = a(1 + e)
     \]

3. **Numerical Implementation and Validation**  
   - **Task 3-a:** Develop a Python script or Jupyter Notebook that performs the calculations for one or more scenarios.  
   - **Task 3-b:** Validate your model by comparing the computed parameters with known values for a specific celestial body or satellite.  
   - **Task 3-c:** Include plots or tables that summarize how variations in the input parameters (e.g., different initial velocities) affect the orbital characteristics.

4. **Visualization and Analysis**  
   - **Task 4-a:** Visualize the computed elliptical orbit in 2D or 3D space. Libraries such as Matplotlib or Plotly can be used to plot the orbit along with marked positions for periapsis and apoapsis.  
   - **Task 4-b:** Analyze the sensitivity of the orbital parameters with respect to changes in the input parameters. Provide commentary or a short discussion on the stability and behavior of orbits under small perturbations.

5. **Documentation and Reporting**  
   - **Task 5-a:** Document your methodology thoroughly with inline comments and a detailed explanation of the equations used.  
   - **Task 5-b:** Prepare a report summarizing the simulation results, theoretical background, and any discrepancies between computed and expected values.  
   - **Task 5-c:** Discuss potential extensions (e.g., incorporating non-Keplerian effects such as atmospheric drag or third-body perturbations).

---

## 📦 Deliverables

- **💻 Code Implementation:**  
  - A Python script or Jupyter Notebook containing the complete code for calculating orbital parameters with clear inline documentation.
  
- **📊 Analysis Report:**  
  - A detailed report summarizing the methodology, computed orbital parameters, validation against known data, and sensitivity analysis.
  
- **🖼️ Visualizations:**  
  - Plots illustrating the computed orbit(s) in 2D or 3D, with annotations for key parameters such as periapsis and apoapsis.
  - Graphs or tables showing the influence of input parameter variations on the orbital elements.

---

## 🎁 Bonus Section (Advanced Challenge)

1. **Perturbation Analysis:**  
   - Extend the simulation to include perturbative forces (e.g., J2 perturbation, atmospheric drag) and analyze their impact on orbital evolution over time.
   
2. **Multi-Body Simulations:**  
   - Expand the model to handle multi-body interactions, calculating orbital parameters in more complex gravitational scenarios (e.g., Earth-Moon system dynamics).
   
3. **Interactive Exploration:**  
   - Develop an interactive dashboard using tools like Streamlit or Plotly Dash that allows users to adjust the input parameters in real time and sees the effect on orbital parameters and trajectories.

*Bonus Deliverables:*  
- A comparative study discussing the differences between the simple two-body model and the extended models including perturbations.
- An interactive tool for real-time exploration of orbital mechanics parameters.

---

## 📚 Resources

1. **[Orbital Mechanics – Wikipedia](https://en.wikipedia.org/wiki/Orbital_mechanics)**

2. **[Vis-Viva Equation – Wikipedia](https://en.wikipedia.org/wiki/Vis-viva_equation)**

3. **[Kepler's Laws – NASA](https://solarsystem.nasa.gov/resources/243/keplers-laws/)**

4. **[Celestial Mechanics and Dynamical Astronomy](https://www.springer.com/journal/10569)**

5. **[Matplotlib for Python](https://matplotlib.org/)**

6. **[Plotly for Python](https://plotly.com/python/)**

---
