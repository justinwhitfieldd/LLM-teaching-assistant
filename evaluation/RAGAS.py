import warnings
import os
os.environ["OPENAI_API_KEY"] = "YOUR-API-KEY-HERE"
warnings.filterwarnings('ignore')
from langchain_openai import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from matplotlib import pyplot as plt
import seaborn as sns

from langchain_core.runnables import (
    RunnableParallel,
    RunnablePassthrough
)
from langchain.schema.output_parser import StrOutputParser
from datasets import Dataset

from langchain.text_splitter import RecursiveCharacterTextSplitter
import shutup;shutup.please()

import os
from PyPDF2 import PdfReader


# Function to extract text from a PDF file
def extract_text_from_pdf(file_path):
    with open(file_path, 'rb') as file:
        pdf_reader = PdfReader(file)
        text = ""
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()
        return text


if __name__ == "__main__":
    # Directory containing PDF files
    pdf_directory = "../SlidesDataset"

    # List to store text extracted from PDF files
    texts = []

    # Iterate over each PDF file in the directory
    for filename in os.listdir(pdf_directory):
        if filename.endswith(".pdf"):
            file_path = os.path.join(pdf_directory, filename)
            text = extract_text_from_pdf(file_path)
            texts.append(text)

    # Split the extracted text into chunks
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=4024, chunk_overlap=0)
    splits = text_splitter.create_documents(texts)

    # Create a vector store for the sample data
    persist_directory = 'RAGAS_Embedding/chroma/'


    embedding = OpenAIEmbeddings(model="text-embedding-3-large",
                                 openai_api_key="YOUR-API-KEY-HERE")

    vectordb = Chroma.from_documents(
        documents=splits,
        embedding=embedding,
        persist_directory=persist_directory
    )
    vectordb.persist()
    retriever = vectordb.as_retriever()
    # Define LLM
    llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0,
                     openai_api_key="YOUR-API-KEY-HERE")

    # Define prompt template
    prompt_template = """You are an assistant for question-answering tasks.
    Use the following pieces of retrieved context to answer the question.
    If you don't know the answer, just say that you don't know.
    Question: {question}
    Context: {context}
    Answer:
    """

    prompt = ChatPromptTemplate.from_template(prompt_template)

    retrieval = RunnableParallel(
        {"context": retriever, "question": RunnablePassthrough()}
    )

    chain = retrieval | prompt | llm | StrOutputParser()

    questions = [
        "Why are Functions so important?",
        "What are variable naming conventions?",
        "why coding convention is essiential and what is a good coding convention?",
        "Can you show me some syntax notes when using Python?"
    ]

    ground_truths = [
        ["One reason is that they hide detail and enable us to think at a higher level."],
        [
            "Variables must have a name to be used Your names must always start with a letter or underscore, but they can only contain these types characters Letters (capital and lowercase) Numbers Underscores. Python contains some reserved keywords valuable to the functionality of Python ○ Your variable name cannot be a Python keyword ■ It can contain a keyword (valid: className), but it cannot be solely the keyword (invalid: class) ● Have descriptive variable names (give a hint what it will be used for)"],
        [
            "Coding convention is essentially how someone writes code • Good coding convention dictates: • Good whitespace (blank lines between different sections of code) • Increases readability • Good commenting • Makes inheriting code easier for those involved • Makes looking at old code easier to follow • Boils down to a matter of opinion • Gets more apparent the more complicated the programs become."],
        [
            "Anything you want to directly print must be inside quotations • print(Hello World) will not work • You can print a blank line through print) • You can have compound print statements through two avenues: + and, • + and, must be outside of the quotations to work • + conjoins statements directly (no space between) • , adds a space between statements • Examples online may use Python version 2, which doesn't use parentheses in print statements • Python version 3 requires parentheses • If an example you find online doesn't work for you, check the version."]
    ]

    # Adding empty strings for the missing ground truths
    missing_ground_truths = [""] * (len(questions) - len(ground_truths))
    ground_truths += missing_ground_truths

    answers = []
    contexts = []

    # traversing each question and passing into the chain to get answer from the system
    for question in questions:
        answers.append(chain.invoke(question))
        contexts.append([docs.page_content for docs in retriever.get_relevant_documents(question)])

    # Flatten the list of lists into a single list of strings
    ground_truths_flat = [item[0] for item in ground_truths]

    # Preparing the dataset
    data = {
        "question": questions,
        "answer": answers,
        "contexts": contexts,
        "ground_truth": ground_truths_flat  # Use the flattened list
    }

    # Convert dict to dataset
    dataset = Dataset.from_dict(data)
    from ragas import evaluate
    from ragas.metrics import (
        faithfulness,
        answer_relevancy,
        context_recall,
        context_precision,
    )

    result = evaluate(
        dataset=dataset,
        metrics=[
            context_precision,
            context_recall,
            faithfulness,
            answer_relevancy,
        ]
    )

    df = result.to_pandas()
    df.to_csv('RAGAS_result.csv', sep=',', index=False, encoding='utf-8')

    df.groupby('question').size().plot(kind='barh', color=sns.palettes.mpl_palette('Dark2'))
    plt.gca().spines[['top', 'right', ]].set_visible(False)


