def generate_answer(query):
    # tokenize the query to get input_ids
    inputs = tokenizer([query], max_length=1024, return_tensors="pt")
    # use generator to predict output ids
    ids = generator.generate(inputs["input_ids"], num_beams=2, min_length=20, max_length=40)
    # use tokenizer to decode the output ids
    answer = tokenizer.batch_decode(ids, skip_special_tokens=True, clean_up_tokenization_spaces=False)[0]
    return pprint(answer)

query = "How was the first wireless message sent?"
context = query_pinecone(query, top_k=5)
query = format_query(query, context["matches"])
generate_answer(query)

for doc in context["matches"]:
    print(doc["metadata"]["passage_text"], end='\n---\n')

query = "where did COVID-19 originate?"
context = query_pinecone(query, top_k=3)
query = format_query(query, context["matches"])
generate_answer(query)