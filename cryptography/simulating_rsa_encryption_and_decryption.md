# **CryptoQuest: RSA Encryption Odyssey – Simulating RSA Encryption and Decryption in Python**

---

## Overview

RSA is one of the cornerstones of modern cryptography. Its asymmetric nature—using a pair of mathematically linked keys, one public and one private—offers both encryption and digital signature capabilities that underpin secure communications worldwide. In this challenge, you’ll simulate the entire RSA process: from generating prime numbers and computing keys to encrypting and decrypting messages. Along the way, you’ll gain hands-on experience with modular arithmetic, Euler’s totient function, and the extended Euclidean algorithm for computing modular inverses.  

*Objective:*  
- Understand RSA’s key generation process and the importance of prime selection.  
- Implement encryption and decryption routines that simulate real-world usage.  
- Explore the challenges of converting text into numeric representations and back.  
- Appreciate both the theoretical underpinnings and practical limitations of RSA in modern applications.

---

## Task 1: Generating RSA Keys

### Step-by-Step Breakdown

1. **Understanding Key Generation:**  
   - **Concept:** RSA key generation requires two large prime numbers. The modulus \( n \) is created by multiplying these primes, and the totient \( \phi(n) \) is computed as \( (p-1) \times (q-1) \).  
   - **Importance:** Choosing large primes is crucial because the security of RSA depends on the difficulty of factoring \( n \).

2. **Selecting Prime Numbers:**  
   - **Steps:**  
     - Decide on two primes \( p \) and \( q \). For initial testing, you may choose small primes, but note these are not secure.
     - Compute \( n = p \times q \) and \( \phi(n) = (p-1) \times (q-1) \).  
   - **Tip:** Use built-in or custom functions to verify prime status; consider starting with known small primes (such as 61 and 53) before scaling up.

3. **Choosing the Public Exponent \( e \):**  
   - **Task:**  
     - Select an integer \( e \) such that \( 1 < e < \phi(n) \) and \( \gcd(e, \phi(n)) = 1 \). This means \( e \) and \( \phi(n) \) must be co-prime.
   - **Hint:** A common choice for \( e \) is 65537, but for teaching purposes, you might select a smaller value.

4. **Computing the Private Exponent \( d \):**  
   - **Process:**  
     - Use the extended Euclidean algorithm to compute \( d \), the modular multiplicative inverse of \( e \) modulo \( \phi(n) \). Ensure that \( d \times e \equiv 1 \) (mod \( \phi(n) \)).
   - **Potential Pitfall:** Ensuring that the algorithm handles edge cases when \( e \) and \( \phi(n) \) are not properly co-prime.

### Expected Outcome

- A Python function or module that:
  - Accepts or generates two primes \( p \) and \( q \).  
  - Computes \( n \) and \( \phi(n) \).  
  - Chooses a valid \( e \) and calculates \( d \).  
- Inline comments that explain each calculation and decision point.

### Practical Hints

- Use Python’s `math.gcd()` to verify co-primeness.  
- Implement a helper function (e.g., `mod_inverse(e, phi)`) using the extended Euclidean algorithm.  
- Validate your key pair by checking that \( (e \times d) \mod \phi(n) = 1 \).

---

## Task 2: Implementing RSA Encryption

### Step-by-Step Breakdown

1. **Preparing the Plaintext:**  
   - **Concept:** RSA works on numeric data. You must convert your plaintext message into a numeric format.
   - **Approach:**  
     - Convert each character of the string to its corresponding ASCII value or use another scheme to form a large integer.
   - **Challenge:** Manage the conversion so that the resulting number is less than \( n \) and reversible during decryption.

2. **Encryption Routine:**  
   - **Process:**  
     - The RSA encryption formula is:  
       \[
       c = m^e \mod n
       \]
       where \( m \) is the message in its numeric form and \( c \) is the ciphertext.
   - **Tip:** Leverage Python’s built-in `pow(m, e, n)` for efficient modular exponentiation.

3. **Handling Edge Cases:**  
   - **Considerations:**  
     - Ensure your algorithm can handle messages with characters that don’t directly map to numbers (or split messages into blocks if needed).
   - **Additional Hint:** You might define an encoding/decoding scheme to systematically convert between text and numeric form.

### Expected Outcome

- A Python function that takes a plaintext string and returns the ciphertext after applying RSA encryption.
- Test cases that demonstrate encryption works correctly with small sample messages.

### Practical Hints

- Document your encoding method—whether you convert each character individually or process blocks of characters.
- Be aware that your simulation should compare your ciphertext results against expected outcomes.

---

## Task 3: Implementing RSA Decryption

### Step-by-Step Breakdown

1. **Decryption Routine:**  
   - **Process:**  
     - The decryption formula is:
       \[
       m = c^d \mod n
       \]
       where \( c \) is the ciphertext, \( d \) is the private key, and \( m \) is the decrypted numeric message.
   - **Tip:** Again, use Python’s `pow(c, d, n)` to compute the modular exponentiation efficiently.

2. **Recovering the Plaintext:**  
   - **Task:**  
     - Convert the numeric representation back into text using the reverse of the method you chose during encryption.
   - **Challenge:**  
     - Make sure that the conversion process is robust enough to handle any special cases or padding used during encryption.

3. **Validation:**  
   - **Objective:**  
     - Ensure that decrypting the ciphertext yields the original plaintext.
   - **Test:**  
     - Encrypt a sample message, then decrypt it to verify the process is reversible.

### Expected Outcome

- A full decryption function that, when given ciphertext and the RSA private key, returns the original plaintext message.
- Detailed inline documentation that validates the correctness of your algorithm.

### Practical Hints

- Consider using try/except blocks for error handling, especially during the conversion back from numeric form to text.
- Comparing hash values of the original and decrypted messages can serve as a verification method.

---

## Task 4: Visualizing RSA Process and Reporting

### Step-by-Step Breakdown

1. **Graphical Flowchart:**  
   - **Objective:**  
     - Design a flowchart illustrating the RSA key generation, encryption, and decryption steps.
   - **Task:**  
     - Use libraries like `graphviz` to map the process, from prime selection to processing each character of the message.
   - **Tip:** Ensure the flowchart clearly annotates where modular arithmetic, Euler’s totient, and modular inverses are used.

2. **Data Visualization (Optional):**  
   - **Possibility:**  
     - Plot the computational time or responsiveness for different key sizes to visualize how increasing prime lengths affects performance.
   - **Task:**  
     - Use `matplotlib` to graph these relationships, providing a visual illustration of cost vs. security.

3. **Reporting:**  
   - **Structure:**  
     - Integrate your code, flowcharts, and decryption validation results into a cohesive report.
   - **Focus:**  
     - Explain the rationale behind each step, analyze potential vulnerabilities (such as using small primes), and relate your findings to modern RSA implementations.

### Expected Outcome

- A comprehensive report that includes:
  - A detailed description of each step in the RSA process.  
  - Flowcharts and visualizations that elucidate the process.
  - Comparative insights into the importance of key size and processing efficiency.

### Practical Hints

- Annotate your visual aids with clear captions and legends.
- Use modular, step-by-step explanations within your report to help readers follow your logic easily.

---

## Bonus Section: Advanced Challenges and Extensions

### Bonus Task 1: Prime Generation and Testing

- **Goal:**  
  - Enhance your RSA simulation by implementing a robust prime generation function using probabilistic tests (e.g., Miller-Rabin).
- **Steps:**  
  1. Create or integrate a function that uses a probabilistic method to test if a number is prime.  
  2. Use this function to generate larger primes for your RSA key pairs.
- **Considerations:**  
  - Discuss the trade-offs between security and computational intensity.

### Bonus Task 2: Implementing Padding Schemes

- **Goal:**  
  - Introduce a simple padding scheme, such as OAEP-like padding, to your encryption routine to simulate realistic safe message encryption.
- **Steps:**  
  1. Implement a basic padding mechanism to add randomness to the plaintext before encryption.  
  2. Adjust the decryption function to correctly remove the padding.
- **Discussion:**  
  - Explain how padding can improve security by preventing specific attacks on unpadded RSA.

### Bonus Task 3: Simulating an Attack on Weak RSA Keys

- **Goal:**  
  - Demonstrate the importance of key size by attempting to factor a small modulus \( n \) and recovering the private key.
- **Steps:**  
  1. Implement a simple factorization algorithm (or use trial division) for small \( n \).  
  2. Show how quickly RSA can be compromised if the primes are too small.
- **Reflection:**  
  - Discuss why modern RSA implementations require key sizes of 2048 bits or more.

---

## Bonus Section Deliverables

- **Code Implementation:**  
  - Extend your RSA module to include:
    - A probabilistic prime testing method and prime generator.
    - An implementation of a basic padding scheme.
    - A simulation of an attack on weak RSA keys.
- **Documentation:**  
  - Provide clear inline comments and a supplementary write-up that explains your enhancements.
  - Include before-and-after examples illustrating the impact of padding and the risks of small key sizes.
- **Visual Aids:**  
  - Update your flowcharts and plots to include the advanced features.
- **Analysis Report:**  
  - Discuss your results, comparing the baseline simulation with your enhanced implementations, and analyze the trade-offs in terms of security and efficiency.

---

## Deliverables

1. **Code Implementation:**  
   - A Python module containing well-documented functions to:
     - Generate RSA key pairs including the computation of \( n \), \( \phi(n) \), \( e \), and \( d \).  
     - Encrypt plaintext into ciphertext and decrypt ciphertext back into plaintext.  
     - (Bonus) Extend the basic RSA simulation with advanced prime generation, padding, and attack simulation.
2. **Comprehensive Report:**  
   - A detailed write-up that:
     - Explains the RSA process step by step.
     - Provides insights into design choices, challenges, and potential vulnerabilities.
     - Includes flowcharts, visualizations, and a comparative analysis of both the basic and enhanced implementations.
3. **Resource List:**  
   - A curated collection of readings and documentation to deepen your understanding.

---

## 🌐 Resources

- **[RSA algorithm – Wikipedia](https://en.wikipedia.org/wiki/RSA_(cryptosystem))**

- **[Introduction to Modern Cryptography by Jonathan Katz and Yehuda Lindell](https://www.crcpress.com/Introduction-to-Modern-Cryptography/Katz-Lindell/p/book/9781466570269)**

- **[Practical Cryptography in Python (Online Tutorials)](https://practicalcryptographyinpython.com/)**

- **[Graphviz Documentation for Flowcharting](https://graphviz.org/documentation/)**

- **[Matplotlib User Guide](https://matplotlib.org/stable/users/index.html)**

---

## Final Thoughts

Simulating RSA encryption and decryption will deepen your understanding of asymmetric cryptography, from its mathematical fundamentals to its practical applications. With this guided problem set, you’re encouraged to explore every step—from prime selection and key generation to encrypting realistic messages and analyzing vulnerabilities. Enjoy the journey through RSA, and let your curiosity drive you toward creating even more secure and sophisticated cryptographic systems!

---
