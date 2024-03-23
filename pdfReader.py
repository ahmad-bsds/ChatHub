from pypdf import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter, SentenceTransformersTokenTextSplitter

reader = PdfReader(r"./Doc/deepLearning.pdf")
pdf_text = [p.extract_text().strip() for p in reader.pages]

# Filter the empty strings:
pdf_text = [text for text in pdf_text if text]

# print(pdf_text[0])

# Chunking by charecter:
# The character splitter allows us to divide text recursively according to certain divider charecters.

character_splitter = RecursiveCharacterTextSplitter(
    separators=["\n\n", "\n", " ", "", ". "],
    chunk_size=1000,
    chunk_overlap=0
)
character_split_text = character_splitter.split_text('\n\n'.join(pdf_text))
# print(character_split_text[10])
# print(f"\n Total chunks: {len(character_split_text)}")


# Chunking by token:
token_splitter = SentenceTransformersTokenTextSplitter(chunk_overlap=0, chunk_size=256) # 256 is max length of window.

# Re-split token split text.
token_split_texts = []
for text in character_split_text:
    token_split_texts += token_splitter.split_text(text)

print(token_split_texts[10])
print(f"\nTotal chunks: {len(token_split_texts)}")