# correct_task2.py

def count_valid_emails(emails):
    count = 0

    for email in emails:
        if not isinstance(email, str):
            continue

        if email.count("@") != 1:
            continue

        local, domain = email.split("@")
        if local and domain:
            count += 1

    return count
