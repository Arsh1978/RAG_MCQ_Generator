from setuptools import find_packages,setup

setup(
    name='Modular RAG Chatbot',
    version='0.0.1',
    author='Harsh Tyagi',
    author_email='harshtyagi145@gmail.com',
    description='A modular RAG chatbot to chat with multiple files',
        install_requires=[
        'langchain',
        'langchain-cohere',
        'python-dotenv',
        'chromadb',
        'urllib3',
        'PyMuPDF',
        'streamlit',
        'unstructured',
        'extract-msg',
        'pandoc',
        'pypandoc',
        'tqdm',
        'sentence_transformers',
        'langchain-community',
        'tiktoken',
        'langchain-openai',
        'langchainhub',
        'chroma-migrate',
        'llama-index',
        'langchain-experimental',
        'ollama'
    ],

    packages=find_packages()
)