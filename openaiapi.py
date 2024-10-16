import os
import logging
import hashlib
import json


from openai import OpenAI
from dotenv import load_dotenv



# Set up logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='ebook_generation.log',
                    filemode='w')

# Add console handler
console = logging.StreamHandler()
console.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
console.setFormatter(formatter)
logging.getLogger('').addHandler(console)




load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise Exception("OPENAI_API_KEY environment variable not set.")

client = OpenAI()

CACHE_DIR = "cache"
os.makedirs(CACHE_DIR, exist_ok=True)

def get_cache_filename(prompt):
    logging.info("""Generate a unique cache filename based on the prompt.""")
    # Hash the prompt to create a unique filename
    prompt_hash = hashlib.md5(prompt.encode('utf-8')).hexdigest()
    return os.path.join(CACHE_DIR, f"{prompt_hash}.json")

def save_to_cache(filename, data):
    logging.info("""Save API response to cache.""")
    with open(filename, 'w') as cache_file:
        json.dump(data, cache_file)

def load_from_cache(filename):
    logging.info("""Load API response from cache.""")
    with open(filename, 'r') as cache_file:
        return json.load(cache_file)


def connect_api(system="You are a business idea generator.",prompt=""):
    logging.info(f"Processing prompt: {prompt}")

    # Generate cache filename
    cache_filename = get_cache_filename(prompt)

    # Check if cached response exists
    if os.path.exists(cache_filename):
        logging.info("Loading response from cache.")
        response_data = load_from_cache(cache_filename)
    else:
        logging.info("Cache miss. Calling OpenAI API.")
        messages = [
            {"role": "system", "content": system},
            {"role": "user", "content": prompt}
        ]
        try:
            response = client.chat.completions.create(
                model="gpt-4",
                messages=messages,
                max_tokens=500
            )
            response_data = response.choices[0].message.content
            save_to_cache(cache_filename, response_data)
            logging.info("Response saved to cache.")
        except Exception as e:
            logging.error(f"Error generating outline: {str(e)}")
            raise
    return response_data  
        
if __name__ == '__main__':
    prompt='Generate 10 business idea with AI'
    response=connect_api(prompt)
    print(f'Response:{response}')