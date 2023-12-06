# results.py
import torch
from Bert import bert_embeddings  # Assuming bert.py contains the bert_embeddings class
from scipy.spatial.distance import cosine

# Function to instantiate the model and get embeddings
def get_embeddings_from_csv(csv_file_path):
    bert_embedder = bert_embeddings()
    texts = bert_embedder.obtain_text(csv_file_path)
    tokenized_texts = bert_embedder.obtain_tokenization(texts)
    embeddings = []
    with torch.no_grad():
        for tokenized_text in tokenized_texts:
            output = bert_embedder.model(**tokenized_text)
            embeddings.append(output.last_hidden_state.mean(dim=1))
    return embeddings

# Function to calculate cosine similarity between embeddings from two CSV files
def calculate_cosine_similarity(csv_file_path1, csv_file_path2):
    embeddings1 = get_embeddings_from_csv(csv_file_path1)
    embeddings2 = get_embeddings_from_csv(csv_file_path2)
    similarities = []
    for emb1, emb2 in zip(embeddings1, embeddings2):
        similarity = 1 - cosine(emb1.flatten(), emb2.flatten())
        similarities.append(similarity)
    return similarities

# Function to print the results of the comparison
def print_comparison_results(csv_file_path1, csv_file_path2):
    similarities = calculate_cosine_similarity(csv_file_path1, csv_file_path2)
    for i, similarity in enumerate(similarities, 1):
        print(f"Similarity between text pair {i}: {similarity:.4f}")

# Example usage
if __name__ == "__main__":
    print_comparison_results('/home/chibuikeejikeme/projects/rfcnlp/myworkrfc/data/output.csv', '/home/chibuikeejikeme/projects/rfcnlp/myworkrfc/data/fsm_output.csv')
