#It it used to calculated to storage

Total_Storage=float(input("Enter a Total Storage:"))
Used_Storage=float(input("Enter a Used Storage:"))
print(f"Used storage in percentage:{((Used_Storage/Total_Storage)*100):.2f}%")