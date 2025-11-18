import re

email_remove_before_at = "^.*(?=@)"
email_remove_after_at = "@.*"
email_remove_high_domain = r"\.[^.]+$"
e = re.sub(email_remove_before_at, "a", "sadad@mail.com")
print(e)
