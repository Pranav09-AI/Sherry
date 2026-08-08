from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_documents(documents):

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=100,
        chunk_overlap=10,
        length_function=len,
        is_separator_regex=False,
    )

    return text_splitter.split_documents(documents)