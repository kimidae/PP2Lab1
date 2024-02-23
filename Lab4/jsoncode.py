import json

with open('json_file.json') as x:
    data = json.load(x)

print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<8} {}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

for filedata in data['imdata']:
    dn = filedata['l1PhysIf']['attributes']['dn']
    description = filedata['l1PhysIf']['attributes']['descr']
    speed = filedata['l1PhysIf']['attributes'].get('speed', 'inherit')
    mtu = filedata['l1PhysIf']['attributes'].get('mtu', '')
    print("{:<50} {:<20} {:<8} {}".format(dn, description, speed, mtu))