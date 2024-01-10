from setuptools import setup,find_packages

setup(
    name = "mcqgenai",
    version = "0.0.1",
    author = "Aswini",
    author_email = "ashwinijalla@gmail.com",
    install_requires = ["openai","langchain","PyPDF2","streamlit","python-dotenv"],
    packages = find_packages()
)