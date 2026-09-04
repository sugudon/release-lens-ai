from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI

def main():
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", "You are a helpful assistant that ranks documents based on relevance to a query."),
            ("human", "Query: {query}\nDocuments: {documents}"),
        ]
    )   

    model = ChatOpenAI(
        model="gpt-4.1-mini",
        temperature=0,
    )

    chain = (prompt | model | StrOutputParser())

    result = chain.invoke(
        {
           "release_description": (
               "Upgrade payment API from v1 to v2"
               "and increase retries from 3 to 5."
           )
        }
    )
    print("\n")
    print("=" * 80)
    print("LANGSMITH TEST")
    print("=" * 80)
    print(result)

    if __name__ == "__main__":
        main()