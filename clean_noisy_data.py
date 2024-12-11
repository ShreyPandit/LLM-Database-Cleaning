import torch
from transformers import pipeline
import pandas as pd
from tqdm import tqdm

df = pd.read_csv("/home/snp2453/DBMS/train_v3_drcat_01_noisy_1000.csv")

pipe = pipeline(
    "text-generation",
    model="google/gemma-2-9b-it",
    model_kwargs={"torch_dtype": torch.bfloat16},
    device_map="auto",
)

def make_prompt(noisy_text):
    sys_prompt = f""" 
    You are a text cleaning expert. Clean the given text by removing:
    1. Invisible Unicode characters and formatting marks
    2. Random injected character strings
    3. Duplicated words in sequence
    4. HTML/XML tags and entities
    5. Control characters and irregular line endings
    6. Encoding artifacts (like mojibake)
    7. Excessive or special whitespace
    Be precise and only remove the necessary characters. Do not change the order of the words or the meaning of the text, and return the cleaned text only without any additional information.

    Examples:

    Input 1: "The quick⁠ brown fox‎ jumps jumps jumps jumps over the lazy dog &nbsp;#R$T2k9pL@"
    Output 1: "The quick brown fox jumps over the lazy dog"

    Input 2: "Hello​ World</div>â€™ï»¿   Hello    World\x00\r\r\n"
    Output 2: "Hello World Hello World"

    Clean this text:
    {noisy_text}
    """
    return sys_prompt

llm_cleaned_text = []
for i in tqdm(range(len(df))):
    try:
        noisy_text = df['Noisy_text'][i]
        messages = [
            {"role": "user", "content": make_prompt(noisy_text)},
        ]
        outputs = pipe(messages, max_new_tokens=2048)
        assistant_response = outputs[0]["generated_text"][-1]["content"].strip()
        print(assistant_response)
        llm_cleaned_text.append(assistant_response)
    except Exception as e:
        print(e)
        llm_cleaned_text.append("")
        
df['LLM_cleaned_text'] = llm_cleaned_text
df.to_csv("/home/snp2453/DBMS/train_v3_drcat_01_llm_cleaned_noisy", index=False)