import spacy
from spacy_transformers import Transformer

def setup_spacy_bert_pipeline():
    # Create a blank English language class
    nlp = spacy.blank("en")

    # Add the transformer model to the pipeline with proper configuration
    transformer_config = {
        "model": {
            "@architectures": "spacy-transformers.TransformerModel.v1",
            "name": "/home/chibuikeejikeme/projects/rfcnlp/myworkrfc/data/networking_bert_rfcs_only",  # Path to your custom model
            "tokenizer_config": {"use_fast": True}
        },
        "get_spans": {"@span_getters": "spacy-transformers.strided_spans.v1", "window": 128, "stride": 96}
    }
    nlp.add_pipe("transformer", config=transformer_config)

    # Initialize the pipeline
    nlp.initialize()
    
    return nlp

def main():
    nlp = setup_spacy_bert_pipeline()

    text1 = "This is a sentence."
    text2 = "This is another sentence."

    doc1 = nlp(text1)
    doc2 = nlp(text2)

    print(f"Vector for the first token in text1 ('{doc1[0].text}'): {doc1[0].vector[:5]}")
    similarity = doc1.similarity(doc2)
    print(f"Similarity between text1 and text2: {similarity}")

if __name__ == "__main__":
    main()
