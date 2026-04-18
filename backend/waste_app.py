print("♻️ Punarth Waste Segregation System")
print("-----------------------------------")

item = input("Enter waste item: ").lower()

if "bottle" in item:
    print("Type: Dry Waste")
    print("How to dispose: Clean and recycle in plastic/glass bin")

elif "banana" in item or "peel" in item:
    print("Type: Wet Waste")
    print("How to dispose: Compost it or throw in wet waste bin")

elif "newspaper" in item or "paper" in item:
    print("Type: Dry Waste")
    print("How to dispose: Send for recycling or reuse")

elif "battery" in item:
    print("Type: E-Waste")
    print("How to dispose: Take to e-waste collection center")

else:
    print("Item not recognized. Try more general words like bottle, paper, etc.")