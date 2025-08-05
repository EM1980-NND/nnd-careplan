def generate_care_plan(responses):
    return f"""
Care Plan for: {responses.get("Client's full name?", '[Name]')}

Diagnosis: {responses.get("Diagnosis?", '[Not specified]')}
Services Required: {responses.get("Services required?", '[Not specified]')}

Background: {responses.get("Living situation?", '[Not specified]')}

Support Goals:
- {responses.get("Support goals?", '[To be defined]')}

Emergency Plan:
- Evacuation Point: {responses.get("Evacuation point?", '[Not specified]')}

Interventions:
- Provide tailored care aligned to goals and diagnosis.
- Encourage daily routine and maintain safety.
- Provide companionship and assist with functional tasks.

— Nurse Next Door Werribee
"""
