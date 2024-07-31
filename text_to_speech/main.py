from text_generation import generate_thai_text
from text_processing import tokenize_text, pos_tag_text, ner_tag_text
from text_to_speech import synthesize_thai_speech
import sys

def main():
    
    # if sys.version_info[0] < 3:
    #     reload(sys)
    #     sys.setdefaultencoding('utf-8')
        
    try:
 
        thai_text = input("Enter Thai text: ")
        # generated_thai_text = generate_thai_text(prompt)
        thai_text = str(thai_text)
        
        # print("Generated Text:", generated_thai_text)
        
        tokens = tokenize_text(thai_text)
        print("Tokens:", tokens)
        
        pos_tags = pos_tag_text(tokens)
        print("POS Tags:", pos_tags)
        
        entities = ner_tag_text(thai_text)
        print("Named Entities:", entities)
        
        synthesize_thai_speech(thai_text)
        print("Audio content written to 'output/output.wav'")
    
    except UnicodeDecodeError as e:
        print(f"UnicodeDecodeError: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
