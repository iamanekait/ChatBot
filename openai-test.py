import openai

openai.api_key = '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'

messages = [{"role": "system", "content": "You are an intelligent assistant."}]

while True:
    message = input("User : ")
    if message:
        messages.append({"role": "user", "content": message})

        try:
            chat = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", messages=messages
            )
            reply = chat.choices[0].message.content
            print(f"ChatGPT: {reply}")
            messages.append({"role": "assistant", "content": reply})

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            break  # Break out of the loop on error or when conversation ends