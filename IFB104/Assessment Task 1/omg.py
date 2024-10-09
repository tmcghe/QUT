import re

# Sample HTML content simulating a part of an HTML document
html_content = '''
<a href="mailto:false-face@mailinator.com">Send Email</a>
<p>Some other content here</p>
<a href="mailto:cynthia@l7b2l4k8.com">Contact Cynthia</a>
<a href="https://example.com">Visit Example</a>
<a href="mailto:phantom@matrix.33mail.com">Phantom Email</a>
<a href="mailto:hider@trashmail.com">Hider Email</a>
'''

# Regular expression to find all mailto email addresses
regex = r'href="mailto:([^"]+)"'

# Using re.findall to extract all matching email addresses
found_emails = re.findall(regex, html_content)

# Printing the found email addresses
print("Found emails:", found_emails)
