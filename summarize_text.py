import re
from openai import OpenAI

client = OpenAI(api_key="your_openai_api_key_in_here") 

def sanitize_filename(filename):
    """Remove invalid characters from a filename."""
    return re.sub(r'[\\/:*?"<>|]', '', filename)

def summarize_text(text):
    """Use the GPT API to summarize text in one concise sentence."""
    try:
        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are an assistant summarizing text in one concise sentence."},
                {"role": "user", "content": text}
            ]
        )
        summary = completion.choices[0].message.content
        return summary.strip()
    except Exception as e:
        print(f"Error during summarization: {e}")
        return "summary_error"
