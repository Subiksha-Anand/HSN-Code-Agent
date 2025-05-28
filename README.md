#  HSN Code Validation and Suggestion Agent

This project implements an intelligent agent to validate and suggest Harmonized System Nomenclature (HSN) codes using Python. Built as part of an internship assessment using Google's ADK (Agent Developer Kit) principles, the agent loads a master Excel dataset, validates HSN codes, and provides smart suggestions based on product descriptions.

---

##  Features

-  **Validate HSN Codes**  
  Checks if the input HSN code:
  - Has correct format (numeric, 2/4/6/8 digits)
  - Exists in the master dataset
  - Has valid hierarchical parent codes (like 01 → 0101 → 010110)

-  **Suggest HSN Codes**  
  Uses fuzzy matching to suggest relevant HSN codes from user-provided product or goods descriptions.

-  **Excel-based Master Dataset**  
  Reads from `HSN_Master_Data.xlsx`, which contains official HSN codes and their descriptions.

---

##  Folder Structure

