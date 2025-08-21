from google.cloud import aiplatform

# Initialize Vertex AI
aiplatform.init(
    project="",   # Replace with your Google Cloud Project ID
    location="YOUR_REGION"       # Example: "us-central1"
)

def generate_cold_email(name, role, company, product):
    prompt = f"""
    Write a professional cold email for:
    Name: {name}
    Role: {role}
    Company: {company}
    Product: {product}
    Keep it concise and polite.
    """

    # Load pre-trained model
    model = aiplatform.TextGenerationModel.from_pretrained("text-bison@001")
    response = model.predict(prompt, max_output_tokens=300)

    return response.text
