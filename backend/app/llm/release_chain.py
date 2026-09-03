from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

from backend.app.config import settings


prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            """
            You are ReleaseLens AI, an AI assistant for software
            engineering release analysis.

            Your job is to summarize software release descriptions
            clearly and accurately.

            Do not invent technical details that are not present
            in the release description.
            """,
        ),
        (
            "human",
            """
            Summarize the following software release.

            Release description:
            {release_description}

            Focus on:
            - What is changing
            - Potentially affected areas
            - Important technical changes

            Keep the summary concise.
            """,
        ),
    ]
)


model = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
    api_key=settings.openai_api_key,
)


parser = StrOutputParser()


chain = prompt | model | parser