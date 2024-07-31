from TTS.api import TTS

def synthesize_thai_speech(text, model_name="tts_models/en/ljspeech/tacotron2-DDC"):
    # Ensure the text is of sufficient length for the TTS model
    min_length = 10  # Adjust this length based on the model's requirement
    if len(text) < min_length:
        text = text.ljust(min_length)
    
    tts = TTS(model_name=model_name, progress_bar=True, gpu=False)
    tts.tts_to_file(text=text, file_path="output/output.wav")
