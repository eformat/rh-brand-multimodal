import os
import re
import glob
import dspy
import openai
from tqdm import tqdm
import itertools as it
import json
from rich import print

LLM_URL=os.getenv('LLM_URL', 'http://localhost:8080/v1')
API_KEY=os.getenv('API_KEY', 'fake')
LLM_MODEL=os.getenv('LLM_MODEL', 'openai/RedHatAI/Qwen2.5-VL-7B-Instruct-FP8-Dynamic')
MAX_TOKENS=os.getenv('MAX_TOKENS', 6000)
TEMPERATURE=os.getenv('TEMPERATURE', 0.2)
BATCH_SIZE=os.getenv('BATCH_SIZE', 10)
FILE_LOC=os.getenv('FILE_LOC', '/home/mike/Downloads/Brand/Icons/**/**/*')
FILE_LSTRIP=os.getenv('LSTRIP', '/home/mike/Downloads/')
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

print("--- Day 2: Chain of Thought ---")

class ImageClassificationSignature(dspy.Signature):
    """Classify the object in the image."""
    image_input: dspy.Image = dspy.InputField(desc="An image to classify")
    image_name = dspy.InputField(desc="Name of the image")
    answer: str = dspy.OutputField(desc="Describe this image")

files = glob.glob(FILE_LOC)
pbar = tqdm(total=len(files)-1)
files_tuple = tuple(it.batched(files, BATCH_SIZE))

classify_image = dspy.Predict(ImageClassificationSignature)

for t in files_tuple:
    pbar.update(BATCH_SIZE)
    pbar.update(1)
    files_list = list()

    for f in t:
        filename = os.path.basename(f)
        file_size_bytes = os.path.getsize(f)
        print("--- Processing --- " + filename + " " + str(file_size_bytes))
        # skip files we cannot seem to process for now
        extension = os.path.splitext(filename)[1].lower()
        if extension == ".svg":
            print("--- Skipping svg file --- ")
            continue
        if re.match(r".*UI-icons-only.*", filename):
            print("--- Skipping UI-icons-only file --- ")
            continue
        if re.match(r".*Extra-small-icon.*", filename):
            print("--- Skipping Extra-small-icon file --- ")
            continue
        if extension != ".png" and extension != ".jpg" and extension != ".jpeg":
            print("--- Skipping file unknown extension --- ")
            continue
        files_list.append(f)

    if len(files_list) == 0:
        continue

    examples = list()

    for y in files_list:
        my_image = dspy.Image.from_file(y)
        filename = os.path.basename(y)
        examples.append(dspy.Example(image_input=my_image, image_name=filename, answer=None).with_inputs("image_input", "image_name"))

    parallel_executor = dspy.Parallel(num_threads=len(examples)) 

    # Execute the DSPy program on the examples in parallel
    prediction = parallel_executor(
        [(classify_image, example) for example in examples]
    )

    # Print the results
    for i, result in enumerate(prediction):
        image_path = files_list[i]
        image_name = examples[i].image_name
        print("-" * 20)
        print(f"> Results {i+1}:")
        print(f"  Question: {image_name}")
        print(f"  Answer: {result.answer}")
        # print to jsonl
        fname = 'brand.jsonl'
        data = { "image_name": image_name, "image_path": image_path.lstrip(FILE_LSTRIP), "answer": result.answer }
        try:
            with open(fname, "a") as json_file:
                json.dump(data, json_file)
                json_file.write('\n')
        except IOError as e:
            print(f"Error creating JSON file: {e}")
