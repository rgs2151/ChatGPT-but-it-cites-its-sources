from datasets import load_dataset

# load the dataset from huggingface in streaming mode and shuffle it
wiki_data = load_dataset(
    'vblagoje/wikipedia_snippets_streamed',
    split='train',
    streaming=True
).shuffle(seed=960)

history = wiki_data.filter(
    lambda d: d['section_title'].startswith('History')
)

from tqdm.auto import tqdm  # progress bar

total_doc_count = 50000

counter = 0
docs = []
# iterate through the dataset and apply our filter
for d in tqdm(history, total=total_doc_count):
    # extract the fields we need
    doc = {
        "article_title": d["article_title"],
        "section_title": d["section_title"],
        "passage_text": d["passage_text"]
    }
    # add the dict containing fields we need to docs list
    docs.append(doc)

    # stop iteration once we reach 50k
    if counter == total_doc_count:
        break

    # increase the counter on every iteration
    counter += 1