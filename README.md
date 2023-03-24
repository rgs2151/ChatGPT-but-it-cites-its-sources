# ChatGPT but it cites its sources

> This project is a Python implementation of a retriever augmented abstractive question answering system that uses generative models to provide human-like responses to natural language questions. The system is built using a combination of open-source libraries and APIs, including Pinecone, Hugging Face Transformers, and Wikipedia.

## How it works

The abstractive question answering system is built using the following components:

* **Retriever Model** : This component encodes a large corpus of text, such as `Wikipedia ` or `Columbia University's website`, into vectors using the Hugging Face Transformers library. These vectors are stored in a vector database using `Pinecone`.
* **Query Model** : When a user inputs a question in natural language, the query model uses the same Hugging Face Transformers library to encode the question into a vector. This vector is then compared to the vectors in the vector database to find the most relevant documents.
* **Generator Model** : The generator model uses the Hugging Face Transformers library to generate a natural language answer based on the most relevant documents returned by the query model and the original question. The output of the generator model is a human-like answer to the user's question.

## Getting Started

To get started with this project, you will need to follow these steps:

1. Clone the repository to your local machine.
2. Install the necessary libraries using `pip install -r requirements.txt`.
3. Set up a Pinecone account and API key.
4. Run the `encode_wikipedia.py` script to encode the Wikipedia corpus into vectors using the Hugging Face Transformers library and Pinecone.
5. Run the `query.py` script to start the query model and generator model.

## Usage

To use the abstractive question answering system, follow these steps:

1. Run the `query.py` script to start the query model and generator model.
2. Input a question in natural language.
3. Wait for the system to return a human-like answer.

   Note: A visual UI with the help of `Streamlit `is coming coon

## Contributing

Contributions to this project are welcome! If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Make your changes.
3. Submit a pull request.

## License

This project is licensed under the MIT License. See `LICENSE` for more information.

## Acknowledgments

This project was inspired by the work of OpenAI and Hugging Face. Thank you to the developers of Pinecone, Hugging Face Transformers, Wikipedia, and Columbia University for providing the tools and resources necessary to build this system.
