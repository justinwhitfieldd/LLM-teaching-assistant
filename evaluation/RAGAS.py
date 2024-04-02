import os
os.environ["OPENAI_API_KEY"] = "key"
from langchain.document_loaders import DirectoryLoader
from ragas.testset.generator import TestsetGenerator
from ragas.testset.evolutions import simple, reasoning, multi_context
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.llms import Ollama



if __name__ == "__main__":
    loader = DirectoryLoader("directory")
    documents = loader.load()
    for document in documents:
        document.metadata['filename'] = document.metadata['source']

    # generator with openai models
    generator_llm = ChatOpenAI(model="gpt-3.5-turbo")
    critic_llm = Ollama(model="llama2")
    embeddings = OpenAIEmbeddings()

    generator = TestsetGenerator.from_langchain(
        generator_llm,
        critic_llm,
        embeddings
    )

    # generate testset
    testset = generator.generate_with_langchain_docs(documents, test_size=10, distributions={simple: 0.5, reasoning: 0.25, multi_context: 0.25})
