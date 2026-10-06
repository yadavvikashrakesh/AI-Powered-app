from huggingface_hub import InferenceClient


def get_ai_response(prompt, hf_token):
    """
    Send prompt to Hugging Face and return AI response.
    """

    client = InferenceClient(
        api_key=hf_token
    )

    response = client.chat_completion(
        model="meta-llama/Llama-3.1-8B-Instruct",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=1500,
        temperature=0.7
    )

    return response.choices[0].message.content