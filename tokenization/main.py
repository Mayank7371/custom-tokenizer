import tiktoken

# Encoder for GPT-4o model
encoder = tiktoken.encoding_for_model("gpt-4o")

text = "Hey there, my name is Piyush Garg."

# Tokenization
tokens = encoder.encode(text)
print("Tokens:", tokens)

# Detokenization
decoded = encoder.decode(tokens)
print("Decoded:", decoded)
