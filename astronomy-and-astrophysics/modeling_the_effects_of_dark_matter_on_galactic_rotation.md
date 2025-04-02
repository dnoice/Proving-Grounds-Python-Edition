# Modeling the Effects of Dark Matter on Galactic Rotation

This exploration takes you on a journey deep into the cosmic puzzle of dark matter. By merging gravitational physics with observational insights, you'll model how dark matter tweaks the rotation curves of spiral galaxies. Let's break it down: You’ll calculate the expected rotation speeds from visible matter alone, then add in a dark matter halo to see how it flattens those curves, matching what astronomers observe.

---

## 📝 Problem Title

**Modeling the Effects of Dark Matter on Galactic Rotation: A Cosmic Dynamics Challenge**

*Here's the lowdown:*  
Develop a Python-based simulation that blends the contributions of luminous and dark matter to generate galactic rotation curves. You'll explore how the gravitational pull of dark matter influences the speed at which stars orbit their galaxy and validate your model against real-world observations.

---

## 🌍 Scenario

Astronomers have long noticed that the speeds at which stars orbit far from the centers of galaxies don’t drop off as expected based solely on the visible matter. This discrepancy led to the dark matter hypothesis—a mysterious component that exerts gravitational pull without emitting light. In this challenge, you'll model a spiral galaxy by:
- Representing its visible matter using an exponential disk model.
- Adding a dark matter halo (e.g., using the Navarro-Frenk-White (NFW) profile).

By combining these, you'll compute the overall mass distribution and derive the rotation curve. This curve is key to understanding why stars in the outer regions keep moving faster than predicted by luminous matter alone.

---

## 🔧 Problem Tasks

1. **Set Up the Galactic Model and Input Parameters**  
   - **Task 1-a:** Define the luminous mass distribution of the galaxy using an exponential disk model. Choose parameters like disk mass and scale length.
   - **Task 1-b:** Select a model for the dark matter halo (e.g., NFW profile) and specify its characteristic parameters such as scale radius and density.
   - **Task 1-c:** Set the gravitational constant \( G \) and ensure all units are consistent.

2. **Develop the Mathematical Framework**  
   - **Task 2-a:** Write down the equation for the rotational velocity:
     \[
     v(r) = \sqrt{\frac{G \, M_{\text{total}}(r)}{r}},
     \]
     where \( M_{\text{total}}(r) \) is the mass enclosed within a radius \( r \) which includes both luminous and dark matter.
   - **Task 2-b:** Derive expressions for \( M_{\text{luminous}}(r) \) (from the exponential disk) and \( M_{\text{dark}}(r) \) (from the dark matter halo model).
   - **Task 2-c:** Compare your theoretical predictions with the characteristic “flat” rotation curves observed in spiral galaxies.

3. **Implement the Numerical Simulation**  
   - **Task 3-a:** Create a Python script or Jupyter Notebook that computes the rotation curve over a range of radii.
   - **Task 3-b:** Modularize your code by writing separate functions for the luminous and dark matter contributions.
   - **Task 3-c:** Allow for interactive adjustments (via input parameters or sliders) to observe how changes in dark matter properties affect the rotation curve.

4. **Visualization and Data Analysis**  
   - **Task 4-a:** Use visualization libraries like Matplotlib or Plotly to plot the rotation curves. Display separate curves for the luminous component and the combined effect.
   - **Task 4-b:** Annotate your plots with key features, such as the radius where the curve flattens and comparisons with typical observational data.
   - **Task 4-c:** Discuss the sensitivity of the rotation curve to variations in dark matter parameters and what that tells us about galaxy dynamics.

5. **Documentation and Reporting**  
   - **Task 5-a:** Document your methodology, including derivations, assumptions, and computational details with clear inline comments.
   - **Task 5-b:** Summarize your findings in a report, comparing your computed curves with known data, and suggest possible extensions (such as incorporating alternative dark matter profiles or perturbations).

---

## 📦 Deliverables

- **💻 Code Implementation:**  
  - A Python script or Jupyter Notebook with the full simulation code, complete with inline documentation and explanatory comments.

- **📊 Analysis Report:**  
  - A report that outlines your methods, shows the computed rotation curves, compares them with observed data, and highlights how dark matter shapes galactic dynamics.

- **🖼️ Visualizations:**  
  - Plots of the rotation curves (both for luminous matter alone and with dark matter added), along with clear annotations.
  - *(Optional)* An interactive dashboard enabling real-time adjustments of galaxy parameters.

---

## 🎁 Bonus Section (Advanced Challenge)

1. **Alternative Dark Matter Models:**  
   - Implement additional halo models (e.g., isothermal sphere or Burkert profile) and analyze their impact on the rotation curve.

2. **Data-Driven Calibration:**  
   - Integrate real observational data from a well-studied galaxy to fine-tune your model and validate your simulation.

3. **Time Evolution of Galactic Dynamics:**  
   - Extend the simulation to explore how a galaxy's rotation curve might evolve over cosmic timescales under the influence of dark matter.

*Bonus Deliverables:*  
- A comparative analysis between different dark matter models.
- An interactive tool for exploring how changing parameters affects the rotation curve in real time.

---

## 📚 Resources

1. **[Dark Matter – Wikipedia](https://en.wikipedia.org/wiki/Dark_matter)**

2. **[Navarro-Frenk-White (NFW) Profile – Wikipedia](https://en.wikipedia.org/wiki/Navarro%E2%80%93Frenk%E2%80%93White_profile)**

3. **[Exponential Disk Model in Galaxies](https://ned.ipac.caltech.edu/level5/March01/vanDerKruit/van_der_Kruit.html)**

4. **[Matplotlib for Python Visualization](https://matplotlib.org/)**

5. **[Plotly for Python Interactive Plots](https://plotly.com/python/)**

---
