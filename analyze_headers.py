import csv
import re
import sys

csv.field_size_limit(sys.maxsize)

INPUT_FILES = ["emails.csv", "emails 2.csv"]
OUTPUT_FILE = "results.csv"


def get_header(text, header_name):
    pattern = rf"(?im)^{re.escape(header_name)}:\s*(.*)"
    match = re.search(pattern, text)
    return match.group(1).strip() if match else "Not found"


def analyze_email(text):
    sender = get_header(text, "From")
    subject = get_header(text, "Subject")
    message_id = get_header(text, "Message-ID")

    spf = "pass" if "spf=pass" in text.lower() else "fail"
    dkim = "pass" if "dkim=pass" in text.lower() else "fail"
    dmarc = "pass" if "dmarc=pass" in text.lower() else "fail"

    if spf == "pass" and dkim == "pass" and dmarc == "pass":
        classification = "Legitimate"
    else:
        classification = "Suspicious"

    return [sender, subject, message_id, spf, dkim, dmarc, classification]


results = []

for file in INPUT_FILES:
    print(f"Processing {file}...")

    with open(file, "r", encoding="utf-8", errors="ignore") as f:
        reader = csv.reader(f)

        for row in reader:
            if len(row) == 0:
                continue

            
            content = " ".join(row)

            results.append(analyze_email(content))



with open(OUTPUT_FILE, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["From", "Subject", "Message-ID", "SPF", "DKIM", "DMARC", "Result"])
    writer.writerows(results)


print("Done. Results saved to results.csv")