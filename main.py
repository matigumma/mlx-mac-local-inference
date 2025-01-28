from openai import OpenAI
import time  # Import the time module
import sys

# start local server first
# pip install mlx-omni-server
# then run
# mlx-omni-server


user_prompt = sys.argv[1] if len(sys.argv) > 1 else None

if user_prompt is None:
    print("Please provide a prompt as a command-line argument. ex:")
    print("uv run main.py \"<prompt>\"")
    sys.exit(1)

# Configure client to use local server
client = OpenAI(
    base_url="http://localhost:10240/v1",  # Point to local server
    api_key="not-needed"  # API key is not required for local server
)

try:
    start_time = time.time()
    # Chat Completion Example
    chat_completion = client.chat.completions.create(
        model="mlx-community/Llama-3.2-1B-Instruct-4bit",
        messages=[
            {"role": "system", "content": "**ROLE** Te llamas Miky y sos muy amable."},
            {"role": "user", "content": user_prompt}
        ]
    )

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(chat_completion.choices[0].message.content)
    print("---------------------")
    print(f"Response Time: {elapsed_time:.2f} seconds | Prompt Tokens: {chat_completion.usage.prompt_tokens} | Completion Tokens: {chat_completion.usage.completion_tokens} | model: {chat_completion.model}")
except Exception as e:
    print(f"An error occurred: {e}")
