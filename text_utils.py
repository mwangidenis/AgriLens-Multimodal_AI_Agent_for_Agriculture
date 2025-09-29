# text_utils.py
from transformers import pipeline

llm = pipeline("text-generation", model="gpt2")

def generate_response(prompt, image_data):
    context = f"Leaf color: {image_data['leaf_color']}, Spots: {image_data['spots']}, Health: {image_data['estimated_health']}."
    full_prompt = f"{context} Based on this, answer: {prompt}"
    result = llm(full_prompt, max_length=100)[0]['generated_text']
    return result