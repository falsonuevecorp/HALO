import re

with open('snippets/ms-icon.liquid', 'r') as f:
    content = f.read()

# Strip <?xml ... ?>
content = re.sub(r'<\?xml[^>]*\?>', '', content)
# Strip <?xpacket ... ?>
content = re.sub(r'<\?xpacket[^>]*\?>', '', content)
# Strip <metadata>...</metadata>
content = re.sub(r'<metadata>.*?</metadata>', '', content, flags=re.DOTALL)
# Strip <!DOCTYPE ... >
content = re.sub(r'<!DOCTYPE[^>]*>', '', content)

with open('snippets/ms-icon.liquid', 'w') as f:
    f.write(content)

