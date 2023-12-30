import os, re

# Main entrypoint
def run():
    print("New action submitted for validation...")
    
    # Get the issue text and labels
    issue_text = os.environ['INPUT_ISSUE']
    labels = os.environ['INPUT_LABELS'].replace('"','').split(',')
    
    print(f"Issue text:\n\n{issue_text}\n")
    
    # Get the needed parameters from the issue text using regex
    pattern = r"### 📂 Name\s*\n*(.*?)\n*\s*### 📜 Format\s*\n*(.*?)\n*\s*### 📋 Schema\s*\n*(.*?)\n*\s*### 📝 Description"
    matches = re.findall(pattern, issue_text, re.DOTALL)
    title = matches[0][0]
    format = matches[0][1]
    schema = matches[0][2]
    
    # Test to see if the workflow works
    print(f"Title: {title}\nFormat: {format}\nSchema: {schema}\n")

if __name__ == '__main__': run()