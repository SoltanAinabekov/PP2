# Using data file sample-data.json, create output that resembles the following by parsing the included JSON file.
import json

#This path works on my pc only
with open(r'C:\Users\Admin\Desktop\PP2-Repos\PP2\TSIS4_LAB4\Json_task\sample-data.json', 'r') as file:
    data = json.load(file)

imdata = data["imdata"]
headers = ["DN", "Description", "Speed", "MTU"]
print("=" * 80)
print(f"{headers[0]:<50} {headers[1]:<20} {headers[2]:<10} {headers[3]:<10}")
print("-" * 50, "  ", "-" * 20, "  ", "-" * 6, "  ", "-" * 6)
for item in imdata:
    attributes = item['l1PhysIf']['attributes']
    dn = attributes.get("dn")
    descr = attributes.get("descr")
    speed = attributes.get("speed")
    mtu = attributes.get("mtu")

    print(f"{dn:<50} {descr:<20} {speed:<10} {mtu:<10}")
