import tiktoken

encoder = tiktoken.encoding_for_model("gpt-4o")

text = "Hey there, my name mayank."

tokens = encoder.encode(text)
print("Tokens:", tokens)

decoded = encoder.decode(tokens)
print("Decoded:", decoded)
