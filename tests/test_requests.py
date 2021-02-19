import requests

print("doing requests test")
content = requests.get("https://ceda.ac.uk/").content.decode()
assert "archive" in content.lower()

