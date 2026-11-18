# Reference solution (rewritten after original work was lost)
# Week 1.3, Session 2: Email Extractor

raw_emails = ["UserA@gmail.com", "admin@site.com", "usera@gmail.com", "UserB@yahoo.com", "admin@site.com"]


# set comprehension to extract a clean, unique set of lowercase email addresses
# Key idea: {...} makes a set, and a set cannot hold duplicates.
# .lower() makes "UserA@gmail.com" and "usera@gmail.com" the same, so only one is kept.
clean_emails = {email.lower() for email in raw_emails}


# print the clean set of email addressed
print(clean_emails)    # 3 addresses (sets have no fixed order)


# Optional - consider the case where some of the emails are not valid (i.e., without the @ in the email address).
raw_emails2 = ["UserA@gmail.com", "SYSTEM_ALERT", "usera@gmail.com", "admin@site.com", "UserB@yahoo.com"]
# write another set comprehension for this case to extract a clean, unique set of valid, lowercase email addresses
# Key idea: add an if filter - only keep strings that contain "@"
valid_emails = {email.lower() for email in raw_emails2 if "@" in email}

print(valid_emails)
