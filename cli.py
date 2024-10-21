#!/usr/bin/env python3

import argparse
import asyncio

from langchain_community.llms import Ollama
from langchain_openai import ChatOpenAI


def create_parser():

    parser = argparse.ArgumentParser(description="Chat with your RPG Manual!")
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "--openai",
        action="store_true",
        help="Choose OpenAI as your language model provider.",
    )
    group.add_argument(
        "--ollama",
        action="store_true",
        help="Choose Ollama as your language model provider.",
    )
    parser.add_argument(
        "-p",
        "--prompt",
        help="Pass the specified text (or stdin) as your prompt.",
    )
    parser.add_argument(
        "-i",
        "--interactive",
        action="store_true",
        help="Start an interactive chat session.",
    )

    return parser


async def main():
    """
    docstring goes here
    """
    args = create_parser().parse_args()

    if args.openai:
        chat = ChatOpenAI()
    elif args.ollama:
        chat = Ollama(model="llama2")

    while args.interactive:
        pass


if __name__ == "__main__":
    asyncio.run(main())
