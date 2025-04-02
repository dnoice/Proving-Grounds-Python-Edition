# 🏦 Pricing European Call Options Using the Black–Scholes Model

## 🔍 Overview
This challenge centers on the **Black–Scholes model**—a groundbreaking mathematical framework for **pricing European call options**. You’ll learn how to derive or implement the closed-form solution for option prices, understand the underlying assumptions, and explore key model inputs (volatility, risk-free rate, time to maturity). By mastering this foundational model, you’ll gain insights into more advanced option pricing methods and practical trading strategies.

## 🚀 Scenario
Imagine you are a **quantitative analyst** at an investment bank responsible for valuing call options on various stocks. Your firm needs a fast and reliable way to gauge fair prices for these derivatives. The **Black–Scholes formula** not only provides a theoretical pricing baseline but also helps you compute **Greeks** (sensitivities like \(\Delta, \Gamma, \Theta, \Vega\)) for risk management. Understanding how these prices shift with changing market conditions (e.g., volatility spikes) is crucial for hedging and trading decisions.

## 📝 Problem Tasks

### ⚙️ Task 1: Model Formulation and Inputs
- **Task Description:** Familiarize yourself with the **Black–Scholes** formula and the assumptions it relies on.
  - **Sub-tasks:**
    - 🏷️ Identify key inputs: current underlying price \(S_0\), strike price \(K\), risk-free rate \(r\), volatility \(\sigma\), and time to maturity \(T\).
    - 🔎 Review assumptions like lognormal price distribution, continuous compounding, no arbitrage, frictionless markets.
    - 🏗️ Write down the closed-form solution for a European call option, including the **cumulative normal** terms \(N(d_1)\) and \(N(d_2)\).

### 🔬 Task 2: Implementing the Black–Scholes Formula
- **Task Description:** Code the **Black–Scholes** formula for a European call option in Python.
  - **Sub-tasks:**
    - 💻 Use libraries (e.g., `math`, `scipy.stats` for the cumulative distribution function).
    - 🏷️ Validate your implementation against known test cases or examples from literature.
    - 🚀 Allow for vectorized inputs (multiple strike prices, maturities) if practical.

### 🏗️ Task 3: Sensitivity Analysis & The Greeks
- **Task Description:** Compute and interpret the **Greeks**—key derivatives of the option pricing function.
  - **Sub-tasks:**
    - 📐 Derive or implement the formulas for \(\Delta\) (price sensitivity w.r.t. underlying), \(\Gamma\) (second derivative), \(\Theta\) (time decay), \(\Vega\) (volatility sensitivity), and \(\Rho\) (interest rate sensitivity).
    - 💻 Perform small tests to confirm that directional changes in \(S_0, \sigma, r\) produce the expected Greek-induced price changes.
    - 🗒️ Provide explanations or real-world interpretations of each Greek (e.g., hedging applications).

### 🖼️ Task 4: Scenario Testing
- **Task Description:** Demonstrate how the option price evolves under different scenarios.
  - **Sub-tasks:**
    - 🔄 Vary \(\sigma\) (volatility) across a range and plot option prices and Greeks, showing how “expensive” the option becomes under high volatility.
    - 📆 Examine how the option’s value decays as time to maturity \(T\) decreases.
    - 💡 Optionally explore the effect of dividend yields (using the Black–Scholes–Merton extension).

## 📦 Deliverables
- **💻 Code Implementation:**
  A Python script or Jupyter Notebook where you:
  1. Implement the Black–Scholes formula for a European call.  
  2. Compute and interpret the main Greeks (\(\Delta, \Gamma, \Theta, \Vega, \Rho\)).  
  3. Test various inputs (e.g., \(\sigma\), \(T\)) and record changes in option prices.

- **📊 Analysis Report:**
  A concise explanation covering:
  1. Model assumptions and derivation highlights (or references).  
  2. Validation of your formula and any comparisons to known benchmarks.  
  3. Observations from sensitivity analysis—especially how volatility and time to maturity affect the option price.

- **🖼️ Visualizations:**
  - Plots illustrating how option prices and Greeks vary with the underlying price, volatility, or time to maturity.  
  - Potential 3D or heatmap plots for a broader “landscape” of prices vs. two changing parameters.

## 🎁 Bonus Section
1. **🕹️ Interactive Option Pricing App:**
   Build a dashboard (e.g., Streamlit or Dash) that lets users input \(\sigma\), \(r\), \(T\), and \(S_0\), and instantly see the resulting call option price and Greeks.

2. **🔎 Implied Volatility Computation:**
   Implement a routine to **invert** the Black–Scholes formula and find implied volatility given a market-observed option price.

3. **🚀 Monte Carlo Approach for Validation:**
   Use a **Monte Carlo simulation** of geometric Brownian motion to approximate the option’s fair value and compare it to the closed-form result.

4. **🌐 Black–Scholes–Merton for Dividend-Paying Assets:**
   Extend the model to handle continuous dividend yields or discrete dividends in your pricing calculations.

5. **🎥 Presentation Materials:**
   Create a short video or slide deck outlining the formula, showcasing your code, and demonstrating how the Greeks inform hedging decisions.

## 🏅 Bonus Section Deliverables
- **🕹️ Interactive Option Pricing App Deliverable:**
  A functional interface for user-defined parameters, instantly returning a call option price and relevant Greeks.

- **🔎 Implied Volatility Computation Deliverable:**
  A Python function or notebook that, given an option market price, solves for \(\sigma\) via root-finding (e.g., Newton-Raphson or bisection).

- **🚀 Monte Carlo Approach for Validation Deliverable:**
  A script simulating asset paths and computing the option’s payoff, then comparing the empirical mean to the Black–Scholes closed-form price.

- **🌐 Black–Scholes–Merton for Dividend-Paying Assets Deliverable:**
  Additional code/analysis reflecting how dividends alter the underlying’s drift or the present value of the strike.

- **🎥 Presentation Materials Deliverable:**
  A recorded explanation or slides detailing Black–Scholes assumptions, formula usage, and real-world practicality (including key limitations).

## 📚 Resources

- **🔗 [Black–Scholes Model (Wikipedia)](https://en.wikipedia.org/wiki/Black–Scholes_model)**

- **🔗 [Geometric Brownian Motion Basics](https://en.wikipedia.org/wiki/Geometric_Brownian_motion)**

- **🔗 [Monte Carlo Methods for Option Pricing](https://en.wikipedia.org/wiki/Monte_Carlo_methods_for_option_pricing)**

- **🔗 [Implied Volatility (Investopedia)](https://www.investopedia.com/terms/i/iv.asp)**

- **🔗 [Quantitative Finance & Python (PyQuant)](https://pypi.org/project/PyQuant/)**

---
