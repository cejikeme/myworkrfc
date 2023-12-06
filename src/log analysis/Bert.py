import spacy
from spacy_transformers import Transformer
import json
from transformers import BertModel, BertConfig, AutoTokenizer,BertTokenizer
import csv
import torch

csv_file_path ='/home/chibuikeejikeme/projects/rfcnlp/myworkrfc/data/output.csv'

import csv
from transformers import BertModel, BertConfig

class bert_embeddings:
    def __init__(self):
        # Load the configuration from the JSON file
        self.config = BertConfig.from_json_file('/home/chibuikeejikeme/projects/rfcnlp/myworkrfc/data/networking_bert_rfcs_only/config.json')
        # Load the model from the .bin file
        self.model = BertModel.from_pretrained('/home/chibuikeejikeme/projects/rfcnlp/myworkrfc/data/networking_bert_rfcs_only/pytorch_model.bin', config=self.config)
        # load the tokenizer
        self.tokenizer = BertTokenizer.from_pretrained('/home/chibuikeejikeme/projects/rfcnlp/myworkrfc/data/networking_bert_rfcs_only')

    def obtain_text(self, csv_file_path):
        texts = []
        with open(csv_file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header if your CSV has one
            for row in csv_reader:
                text = row[0]
                texts.append(text)
                # Do something with the text, like obtaining embeddings
                # embeddings = self.model.encode(text)
                print(text)
        return texts  # Return the list of texts
    
    def obtain_tokenization(self, texts):
        tokenized_texts = []
        for text in texts:
            inputs = self.tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
            tokenized_texts.append(inputs)
        return tokenized_texts
        


#define tokenizer         
# tokenizer = AutoTokenizer.from

#     # Loop through the rows in the CSV file
#     for row in csv_reader:
#         # Assuming the text is in the first column
#         text = row[0]

#         # Do something with the text
#         print(text)
#         # Tokenize the text
#         
#         # Get embeddings
#         with torch.no_grad():
#          outputs = model(**inputs)


    

#     return nlp

# # Usage
# nlp = setup_spacy_bert_pipeline()


# # def main():
# #     nlp = setup_spacy_bert_pipeline()

# #     text1 = "This is a sentence."
# #     text2 = "This is another sentence."
# #     csv_file_path = '/home/chibuikeejikeme/projects/rfcnlp/myworkrfc/data/output.csv'
# #     with open(csv_file_path, mode='r', encoding='utf-8') as file:
# #     # Create a CSV reader
# #     csv_reader = csv.reader(file)

# #     doc1 = nlp(text1)
# #     doc2 = nlp(text2)

# #     print(f"Vector for the first token in text1 ('{doc1[0].text}'): {doc1[0].vector[:5]}")
# #     similarity = doc1.similarity(doc2)
# #     print(f"Similarity between text1 and text2: {similarity}")

# if __name__ == "__main__":
#     main()














# # Load the configuration from the JSON file
#     with open('/home/chibuikeejikeme/projects/rfcnlp/myworkrfc/data/networking_bert_rfcs_only/config.json') as config_file:
#         transformer_config = json.load(config_file)

# Create a blank English language class
 #   nlp = spacy.blank("en")    
    
    #transformer= nlp.add_pipe("transformer", config=transformer_config)