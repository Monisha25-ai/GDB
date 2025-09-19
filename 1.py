guests = ["Vikas","Harsha","Arjun","Bharat"]
message = "Please attend the party."
for guest in guests:
    print(f"Hey {guest}, {message}")

print("Arjun can't make it to the party.")
guests[2] = "Ravi"
for guest in guests:
    print(f"Hey {guest}, {message}")

print(guests)


guests.insert(0,"Praveen")
guests.append("Suresh")
guests.append("Ravi")

print(f"Final guests list: {guests}")

for popping in range(5):
    guests.pop()

print(f"Updated guests list: {guests}")