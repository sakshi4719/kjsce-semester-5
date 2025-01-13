!pip install spacy
!pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.5.0/en_core_web_sm-3.5.0.tar.gz
import spacy
nlp = spacy.load("en_core_web_sm")

# Sample healthcare-related text
healthcare_text = """
    The patient was diagnosed with type 2 diabetes and hypertension.
    They were prescribed metformin and lisinopril. Further, the patient will undergo
    a cardiac stress test at St. Mary's Hospital next week."""

# Process the text
doc = nlp(healthcare_text)

# Print named entities
print("Entities in the text:")
for ent in doc.ents:
    print(f"{ent.text} - {ent.label_}")

# Print explanations of entity labels
print("\nEntity Label Explanations:")
for ent in doc.ents:
    print(f"{ent.text}: {spacy.explain(ent.label_)}")

# Sample healthcare-related text
healthcare_text = """
    The patient was diagnosed with type 2 diabetes and hypertension.
    They were prescribed metformin and lisinopril. Further, the patient will undergo
    a cardiac stress test at St. Mary's Hospital next week."""

# Process the text
doc = nlp(healthcare_text)

# Define custom entity labels for diseases and drugs
disease_labels = ["type 2 diabetes", "hypertension"]  # Add more disease terms as needed
drug_labels = ["metformin", "lisinopril"]  # Add more drug names as needed

# Iterate through the text and identify entities based on the custom labels
entities = []
for label in disease_labels:
  if label in healthcare_text:
    entities.append((label, "DISEASE"))
for label in drug_labels:
  if label in healthcare_text:
    entities.append((label, "DRUG"))

# Print the identified entities
print("Entities in the text:")
for entity, label in entities:
    print(f"{entity} - {label}")

