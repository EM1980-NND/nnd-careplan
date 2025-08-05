import openai
import os

# OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY") or "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"

# Central Style Enforcement
STYLE_RULES = (
    "NEVER use the word 'patient'. Always refer to the client by name.\n"
    "Write background information in third person.\n"
    "Goals must be written as full sentences starting with 'I want to...'. Avoid SMART goals or frameworks. "
    "No one-liners or long paragraphs. Limit to 3–4 concise goals.\n"
    "Emergency Preparedness Plan must be concise. Only describe:\n"
    "- What to take\n"
    "- From where\n"
    "- Who to call\n"
    "- Where to evacuate\n"
    "Do NOT include speculative items like flashlights, comfort items, or post-emergency actions.\n"
    "NEVER invent or substitute names like 'Mr. Smith'. Only use the real name provided in the prompt (e.g., Jack Ma)."
)

def gpt_generate(prompt, model="gpt-4-1106-preview", temperature=0.7):
    response = openai.ChatCompletion.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature
    )
    return response.choices[0].message.content.strip()

# ===== DIAGNOSIS =====
def generate_diagnosis_summary(diagnosis, client_name):
    prompt = (
        f"{STYLE_RULES}\n\n"
        f"Write a concise clinical paragraph describing the main diagnosis for {client_name}. "
        f"Use {client_name}'s name in the paragraph, and do not refer to 'the client'. "
        f"Diagnosis: {diagnosis}."
    )
    return gpt_generate(prompt, temperature=0.6)

# ===== GOALS =====
def suggest_goals(diagnosis, services_required, client_name):
    prompt = (
        f"{STYLE_RULES}\n\n"
        f"Based on the diagnosis '{diagnosis}' and the services required '{services_required}', "
        f"generate 3–4 personal support goals for {client_name}. "
        f"Each must begin with 'I want to...' and be in full sentence format. "
        f"Do not use bullet points or label the goals. Do not refer to {client_name} in third person."
    )
    return gpt_generate(prompt, temperature=0.7)

# ===== EMERGENCY PLAN =====
def generate_emergency_plan(client_name, evacuation_point, language, contact_name, contact_phone):
    prompt = (
        f"{STYLE_RULES}\n\n"
        f"Write an Emergency Preparedness Plan for {client_name} that addresses exactly the following:\n"
        f"1. What to take (e.g. medications, documents)\n"
        f"2. From where (specific location in the home)\n"
        f"3. Who to call: {contact_name} at {contact_phone}\n"
        f"4. Where to evacuate: {evacuation_point}\n\n"
        f"Preferred language: {language}.\n"
        f"If language is not English, include a note that communication assistance may be required."
    )
    return gpt_generate(prompt, temperature=0.6)

# ===== BACKGROUND =====
def write_background(client_name, lifestyle):
    prompt = (
        f"{STYLE_RULES}\n\n"
        f"Write a third-person background summary about {client_name} using this lifestyle description:\n"
        f"{lifestyle}\n"
        f"Use {client_name}'s name in at least 2–3 sentences. Do not use the term 'the client'."
    )
    return gpt_generate(prompt, temperature=0.6)

# ===== INTERVENTIONS =====
def rewrite_interventions(raw_notes, risks=None, allergies=None, medications=None, diagnosis=None, client_name="the client"):
    context = (
        f"Client Name: {client_name}\n"
        f"Main Diagnosis: {diagnosis or 'N/A'}\n"
        f"Risks: {risks or 'N/A'}\n"
        f"Allergies: {allergies or 'N/A'}\n"
        f"Medications: {medications or 'N/A'}\n"
        f"Intervention Notes: {raw_notes or 'N/A'}"
    )
    prompt = (
        f"{STYLE_RULES}\n\n"
        f"Write a professional, bullet-point intervention plan for {client_name}. "
        f"Each point should address practical care, safety, health, or lifestyle needs. "
        f"Use the name {client_name} instead of general terms. Base the plan on this context:\n{context}"
    )
    return gpt_generate(prompt, temperature=0.7)

# ===== FEEDBACK-BASED REVISION =====
def refine_text(original_text, feedback):
    prompt = (
        f"{STYLE_RULES}\n\n"
        f"Revise the following care plan based on the user feedback below. "
        f"Keep all output aligned with the style rules and use the client’s name consistently.\n"
        f"Feedback:\n{feedback}\n\n"
        f"Original Text:\n{original_text}"
    )
    return gpt_generate(prompt, temperature=0.6)
