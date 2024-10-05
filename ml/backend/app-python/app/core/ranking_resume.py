import torch
from sentence_transformers import SentenceTransformer
from ml.utils.model import SiameseFFN

class Rank:
    def __init__(self, weights: str):
        self.model = SiameseFFN(in_size=768)
        self.model.load_state_dict(torch.load(weights))

        self.encoder = SentenceTransformer('intfloat/multilingual-e5-base')
        self.encoder.eval()

    def _get_candidate_emb(self, candidates: list):
        embeddings = []
        for candidate in candidates:
            if isinstance(candidate['skills'], str):
                embedding = self.encoder.encode(
                    candidate['summary'][:400] + "[SEQ]" + candidate['skills'][:100])
            else:
                embedding = self.encoder.encode(candidate['summary'])
            embeddings.append(embedding)

        return embeddings

    def _get_vacancy_emb(self, vacancy_dict):
        embedding = self.encoder.encode(
            vacancy_dict['description'][:400] + "[SEQ]" + vacancy_dict['key_skills'][:100])
        return embedding

    def rank(self, vacancy_dict, candidates):
        vacancy_embedding = self._get_vacancy_emb(vacancy_dict)
        resume_embeddings = self._get_vacancy_emb(candidates)

        probs_positive = []
        for emb in resume_embeddings:
            logits = self.model(vacancy_embedding, emb)
            probs = torch.softmax(logits, dim=1)
            probs_positive.append(probs[:, 1].to('cpu').numpy())

        return sorted(probs_positive)