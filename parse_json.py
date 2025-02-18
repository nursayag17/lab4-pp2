import json

with open("sample-data.json", "r", encoding="utf-8") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print("{:<50} {:<15} {:<10}".format("DN", "Speed", "MTU"))
print("-" * 80)

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    speed = attributes["speed"]
    mtu = attributes["mtu"]

    print("{:<50} {:<15} {:<10}".format(dn, speed, mtu))
