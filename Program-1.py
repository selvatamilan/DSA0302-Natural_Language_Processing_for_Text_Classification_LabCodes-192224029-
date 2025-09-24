import re
text = """
My email is example123@gmail.com and my phone number is (123)-456-7890.
I also use another email: test.user@domain.org
"""
email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
emails = re.findall(email_pattern, text)
print("Emails found:", emails)
phone_pattern = r"\(\d{3}\)-\d{3}-\d{4}"
phones = re.findall(phone_pattern, text)
print("Phone numbers found:", phones)
match = re.search(email_pattern, text)
if match:
    print("First email found:", match.group())
if re.match("My", text):
    print("The text starts with 'My'")
masked_text = re.sub(email_pattern, "[EMAIL HIDDEN]", text)
print("\nText after masking emails:\n", masked_text)
