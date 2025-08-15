# Write to a File

filename = "output.txt"
content = "This is a sample text written to a file."

with open(filename, "w") as file:
    file.write(content)

print(f"Content written to {filename}")
