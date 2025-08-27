import os

import dspy
import openai

LLM_URL=os.getenv('LLM_URL', 'http://localhost:8080/v1')
API_KEY=os.getenv('API_KEY', 'fake')
LLM_MODEL=os.getenv('LLM_MODEL', 'openai/models/Llama-3.2-3B-Instruct-Q8_0.gguf')
MAX_TOKENS=os.getenv('MAX_TOKENS', 6000)
TEMPERATURE=os.getenv('TEMPERATURE', 0.2)
dspy.enable_logging()

lm = dspy.LM(model=LLM_MODEL,
             api_base=LLM_URL,
             api_key=API_KEY,
             temperature=TEMPERATURE,
             model_type='chat',
             stream=False)
dspy.configure(lm=lm)
dspy.settings.configure(track_usage=True)

print("--- Chain of Thought ---")

class ImageClassificationSignature(dspy.Signature):
    """Classify the object in the image."""
    image_input: dspy.Image = dspy.InputField(desc="An image to classify")
    image_name = dspy.InputField(desc="Name of the image")
    answer: str = dspy.OutputField(desc="Describe this image")

# Instantiate a Predict module with the signature
classify_image = dspy.Predict(ImageClassificationSignature)

# Load an image (e.g., from a URL)
#image_url = "https://example.com/some_image.jpg" # Replace with a valid image URL
#my_image = dspy.Image.from_url(image_url)

image_file = "/home/mike/Downloads/Technology_icon-Red_Hat-AI_model-White-RGB.svg/Technology_icon-Red_Hat-AI_model-White-RGB.Medium-icon.png"
my_image = dspy.Image.from_file(image_file)

# Call the module with the image input
prediction = classify_image(image_input=my_image, image_name="Technology_icon-Red_Hat-AI_model-White-RGB.Medium-icon.png")

print(f"Answer: {prediction.answer}")

# Optional: Inspect LM history to see the CoT prompt
print("\n--- Inspecting LM History ---")
dspy.inspect_history(n=1)
