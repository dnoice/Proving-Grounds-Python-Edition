# Simulating RSA Encryption and Decryption

This exploration dives into one of the cornerstones of modern cryptography—RSA encryption and decryption. Let’s break it down: You’ll implement the RSA algorithm from key generation to the encryption and decryption processes in Python, gaining hands-on experience with modular exponentiation, prime number generation, and Euler's totient function.

---

## 📝 Problem Title

**Simulating RSA Encryption and Decryption: A Cryptography Challenge**

*Here's the lowdown:*
Develop a Python-based simulation that demonstrates the full RSA process. You’ll generate RSA keys from scratch, encrypt messages, and then decrypt them while verifying the correctness of your implementation. The aim is to understand the mathematical principles behind public-key cryptography and appreciate the security provided by the RSA algorithm.

---

## 🌍 Scenario

Imagine you’re the lead cryptographic engineer at a financial institution where data security is paramount. Recently, a breach in an external system has convinced your management that stronger encryption methods are needed. Your mission is to develop and test an RSA encryption system to secure sensitive transactions and communications. You must generate keys using large primes, construct the public and private exponents, and ensure that messages encrypted with your public key can only be decrypted with your private key. Your work will illustrate the power and reliability of RSA in protecting critical data.

---

## 🔧 Problem Tasks

1. **Implement RSA Key Generation**
   - **Task 1-a:** Write Python functions to generate two large prime numbers (or use provided primes for demonstration).  
   - **Task 1-b:** Compute the modulus \( n = p \times q \) and Euler's totient function \( \phi(n) = (p-1)(q-1) \).  
   - **Task 1-c:** Choose a public exponent \( e \) that is coprime with \( \phi(n) \) and compute the private exponent \( d \) such that \( e \times d \equiv 1 \mod \phi(n) \).

2. **Implement RSA Encryption**
   - **Task 2-a:** Develop a function that converts a plaintext message into an integer (using an appropriate encoding scheme).  
   - **Task 2-b:** Implement the encryption algorithm using the public key \( (e, n) \):  
     \[
     c = m^e \mod n
     \]
   - **Task 2-c:** Validate your encryption function with sample messages.

3. **Implement RSA Decryption**
   - **Task 3-a:** Write a Python function for decryption using the private exponent \( d \) and modulus \( n \):
     \[
     m = c^d \mod n
     \]
   - **Task 3-b:** Convert the resulting integer back to the original plaintext message.
   - **Task 3-c:** Ensure that decryption reliably recovers the original message from ciphertext.

4. **Validation and Testing**
   - **Task 4-a:** Perform end-to-end testing by encrypting a message and then decrypting it to confirm accuracy.  
   - **Task 4-b:** Analyze the performance and limitations when using smaller primes for demonstration versus realistic large primes.

5. **Documentation and Reporting**
   - **Task 5-a:** Document your code with detailed inline comments explaining key mathematical concepts and algorithm steps.  
   - **Task 5-b:** Prepare a report summarizing the RSA process, including key generation, encryption, decryption, and analysis of security implications.

---

## 📦 Deliverables

- **💻 Code Implementation:**
  - A Python script or Jupyter Notebook containing the complete RSA simulation—from key generation to encryption and decryption—with extensive documentation.

- **📊 Analysis Report:**
  - A report detailing your methodology, test results, and an analysis of the RSA algorithm's strengths and potential vulnerabilities.

- **🖼️ Visualizations:**
  - *(Optional)* Flow diagrams of the RSA process, and plots showing the relationship between key sizes and computational performance.

---

## 🎁 Bonus Section (Advanced Challenge)

1. **Optimized Key Generation using the CRT:**
   - Implement Chinese Remainder Theorem (CRT) optimizations for faster decryption and compare performance improvements.

2. **Interactive RSA Demo:**
   - Develop an interactive web application using Streamlit or Plotly Dash that allows users to generate RSA keys, encrypt messages, and view step-by-step decryption processes in real time.

3. **Hybrid Cryptosystem Integration:**
   - Explore combining RSA with a symmetric encryption algorithm (such as AES) to create a hybrid system, then analyze the security benefits and performance trade-offs.

4. **Visual and Statistical Analysis:**
   - Create visualizations (e.g., histograms or scatter plots) demonstrating how changes in prime number sizes affect key strength and computational time.

---

## 📚 Resources

1. **[RSA Cryptosystem – Wikipedia](https://en.wikipedia.org/wiki/RSA_(cryptosystem))**

2. **[Introduction to Public-Key Cryptography – NIST](https://www.nist.gov/publications)**

3. **[Python Cryptography Libraries](https://cryptography.io/)**

4. **[Matplotlib for Data Visualization](https://matplotlib.org/)**

5. **[Streamlit for Interactive Web Apps](https://streamlit.io/)**

---
