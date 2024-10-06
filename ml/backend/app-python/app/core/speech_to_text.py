import torch
from transformers import AutoModelForSpeechSeq2Seq, AutoProcessor, pipeline
from utils.ollama_run import LlamaRun

class InterviewToText:
    def __init__(self):
        self._init_whisper_model()

    def _init_whisper_model(self):
        device = "cuda:0" if torch.cuda.is_available() else "cpu"
        torch_dtype = torch.float16 if torch.cuda.is_available() else torch.float32

        model_id = "openai/whisper-large-v3-turbo"

        model = AutoModelForSpeechSeq2Seq.from_pretrained(
            model_id, torch_dtype=torch_dtype, low_cpu_mem_usage=True, use_safetensors=True
        )
        model.to(device)

        processor = AutoProcessor.from_pretrained(model_id)

        self.pipe = pipeline(
            "automatic-speech-recognition",
            model=model,
            tokenizer=processor.tokenizer,
            feature_extractor=processor.feature_extractor,
            torch_dtype=torch_dtype,
            device=device,
            return_timestamps=True
        )

    def run(self, audio_file_path: str, vacancy_dict: dict):
        template = """Use this context for give an feedback for an candidate, what he do well, what he do wrong in interview for position - {position}.
    Context of interview:
    {context}
    """
        llm_model = LlamaRun(
            template=template,
            ollama_url="https://useful-kite-settled.ngrok-free.app"
        )

        audio_transcription = self.pipe(audio_file_path)

        text = llm_model.run(position=vacancy_dict['position'],
                             context=audio_transcription['text'])
        return text