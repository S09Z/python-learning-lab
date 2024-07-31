from transformers import AutoModelForCausalLM, AutoTokenizer
from transformers import logging
import sentencepiece

logging.set_verbosity_error()

model_name = "airesearch/wangchanberta-base-att-spm-uncased"  # Example model name

def load_model_and_tokenizer(model_name):
    try:
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(model_name)
        return tokenizer, model
    except Exception as e:
        print(f"Error loading model and tokenizer: {e}")
        return None, None

tokenizer, model = load_model_and_tokenizer(model_name)

def generate_thai_text(prompt):
    if tokenizer and model:
        inputs = tokenizer.encode(prompt, return_tensors='pt')
        outputs = model.generate(inputs, max_length=100, num_return_sequences=1)
        text = tokenizer.decode(outputs[0], skip_special_tokens=True)
        return text
    else:
        return "Error generating text. Model not loaded."

# Example usage
# if __name__ == "__main__":
#     prompt = "ใส่ข้อความต้นแบบของคุณที่นี่"  # Your text prompt in Thai
#     generated_thai_text = generate_thai_text(prompt)
#     print(generated_thai_text)
