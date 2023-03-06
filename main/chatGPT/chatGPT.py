import openai

# openAI api key goes here
# https://platform.openai.com/account/api-keys
openai.api_key = "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"


def gpt(prompt):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.6,
        max_tokens=700
    )

    return response["choices"][0]["text"]
