#!/usr/bin/env python3

import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
import asyncio
 

async def main():
    kernel = sk.Kernel()
    api_key, org_id = sk.openai_settings_from_dot_env()

    kernel.add_chat_service(
        "chat-gpt",
        OpenAIChatCompletion(ai_model_id="gpt-3.5-turbo-1106", api_key=api_key, org_id=org_id),
    )

    while True:
        command = input('''Please Select an option:
                        1. Plugins
                        3. Quit
                        ''')
        # Get user input
        if command.lower() == '1':
            plugins_dir = input("Please provide your plugins directory: ")
            plugin_name = input("Please provide your plugin's name: ") 
            function_name = input("Please provide your function's name: ")
            prompt = input("Please provide your prompt: ")
            plugin = kernel.import_semantic_plugin_from_directory("plugins", "FunPlugin")
            function = plugin[function_name]
            print(await function(prompt))


        elif command.lower() == '3':
            break

if __name__ == '__main__':
    asyncio.run(main())
