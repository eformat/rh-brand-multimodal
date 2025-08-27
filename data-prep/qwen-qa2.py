import os
import re
import glob
import dspy
import openai
from tqdm import tqdm

LLM_URL=os.getenv('LLM_URL', 'http://localhost:8080/v1')
API_KEY=os.getenv('API_KEY', 'fake')
LLM_MODEL=os.getenv('LLM_MODEL', 'openai/models/Llama-3.2-3B-Instruct-Q8_0.gguf')
MAX_TOKENS=os.getenv('MAX_TOKENS', 6000)
TEMPERATURE=os.getenv('TEMPERATURE', 0.2)
BATCH_SIZE = 5
dspy.enable_logging()

lm = dspy.LM(model=LLM_MODEL,
             api_base=LLM_URL,
             api_key=API_KEY,
             temperature=TEMPERATURE,
             model_type='chat',
             cache=False,
             stream=False)
dspy.configure(lm=lm)
dspy.settings.configure(track_usage=True)

print("--- Chain of Thought ---")

class ImageClassificationSignature(dspy.Signature):
    """Classify the object in the image."""
    image_input: dspy.Image = dspy.InputField(desc="An image to classify")
    image_name = dspy.InputField(desc="Name of the image")
    answer: str = dspy.OutputField(desc="Describe this image")

files = glob.glob('/home/mike/Downloads/Brand/Icons/Technology icons/**/*')
pbar = tqdm(total=len(files)-1)

for f in files:
    pbar.update()
    filename = os.path.basename(f)
    file_size_bytes = os.path.getsize(f)
    print("--- Processing --- " + filename + " " + str(file_size_bytes))
    # skip files we cannot seem to process for now
    if os.path.splitext(filename)[1].lower() == ".svg":
        print("--- Skipping svg file --- ")
        continue
    if re.match(r".*UI-icons-only.*", filename):
        print("--- Skipping UI-icons-only file --- ")
        continue
    if re.match(r".*Extra-small-icon.*", filename):
        print("--- Skipping Extra-small-icon file --- ")
        continue

    # Instantiate a Predict module with the signature
    classify_image = dspy.Predict(ImageClassificationSignature)

    # Load an image (e.g., from a URL)
    #image_url = "https://example.com/some_image.jpg" # Replace with a valid image URL
    #my_image = dspy.Image.from_url(image_url)

    my_image = dspy.Image.from_file(f)

    # Call the module with the image input
    prediction = classify_image(image_input=my_image, image_name=filename)

    print(f"Answer: {prediction.answer}")

# Optional: Inspect LM history to see the CoT prompt
#print("\n--- Inspecting LM History ---")
#dspy.inspect_history(n=len(files))
