# Smart Transport Load Balancing System  
Day-5 Challenge  
Course Code: CSE205  
Department of Computer Science and Engineering  
SRM University–AP  

---

## Problem Overview

This program classifies package weights received by a logistics company into different load categories and applies a personalized adjustment rule based on PLI (Personal Logic Identifier).

---

## Base Classification Rules

- Weight < 0 → Invalid Entry  
- 0–5 → Very Light  
- 6–25 → Normal Load  
- 26–60 → Heavy Load  
- > 60 → Overload  

The program uses:
- Lists for storage  
- For loop for processing  
- Conditional statements for classification  

No list comprehension, dictionaries, sets, or built-in aggregation functions are used.

---

## Personalization Details

Full Name (excluding spaces):  
ValluruKomalSivaram  

Length (L):  
19  

PLI Calculation:  
PLI = L % 3  
PLI = 19 % 3  
PLI = 1  

---

## Applied Rule

Since PLI = 1, Rule B is applied.

Rule B:  
All Very Light items are removed from the final loading plan and counted as affected items.

---

## Additional Outputs

The program also:
- Counts total valid weights  
- Counts affected items due to PLI  
- Displays L and PLI  
- Prints final categorized lists  

---

## Conclusion

This implementation ensures safe load balancing by combining weight classification with personalized rule-based adjustment using modular arithmetic.
