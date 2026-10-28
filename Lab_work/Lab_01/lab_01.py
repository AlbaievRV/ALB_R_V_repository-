globalList = [
    {"name":"Bob", "phone":"0631234567", "email":"bob@mail.com", "age":"20"},
    {"name":"Emma", "phone":"0631234567", "email":"emma@mail.com", "age":"21"},
    {"name":"Jon",  "phone":"0631234567", "email":"jon@mail.com", "age":"22"},
    {"name":"Zak",  "phone":"0631234567", "email":"zak@mail.com", "age":"19"}
]

def printAllList(listForPrinting):
    for item in listForPrinting:
        # Extended to print all 4 fields
        str_out = f"Name = {item['name']}, Phone = {item['phone']}, Email = {item['email']}, Age = {item['age']}"
        print(str_out)

def findPosition(listForFinding, nameForFinding):
    index = 0
    for item in listForFinding:
        if item["name"] < nameForFinding: 
            index += 1
        else:
            break
    return index

def addElemToSortedList(listForAdd, newElem):
    positionForInsert = findPosition(listForAdd, newElem["name"])
    listForAdd.insert(positionForInsert, newElem)
    return

def getElement():
    # Extended input to gather all 4 fields
    name = input("Please enter the name: ")
    phone = input("Please enter the phone: ")
    email = input("Please enter the email: ")
    age = input("Please enter the age: ")
    return {"name": name, "phone": phone, "email": email, "age": age}

def deleteElem(listForDel, name):
    indexForDel = findPosition(listForDel, name)
    if indexForDel < len(listForDel) and listForDel[indexForDel]["name"] == name:
        del listForDel[indexForDel]
        return True
    else:
        return False

def updeteElement(listForUpdate):
    # Implemented from scratch: updates student info and keeps the list sorted
    nameForUpdate = input("Please enter the name of the student to update: ")
    indexForUpdate = findPosition(listForUpdate, nameForUpdate)
    
    if indexForUpdate < len(listForUpdate) and listForUpdate[indexForUpdate]["name"] == nameForUpdate:
        # Remove the old element and insert updated one to maintain sorting order
        del listForUpdate[indexForUpdate]
        print("Please enter new details for the student:")
        newElem = getElement()
        addElemToSortedList(listForUpdate, newElem)
        print("Element has been updated successfully")
        return True
    else:
        print("Element hasn't been found")
        return False

def main():
    while True:
        chouse = input("Please enter the command [C - add new elem, D - delete elem, P - print all List, U - update element, X - exit]: ")
        match chouse:
            case "C" | "c" :
                newElem = getElement()
                addElemToSortedList(globalList, newElem)
            case "D" | "d":
                nameElemForDel = input("Please enter the name for delete: ")
                if deleteElem(globalList, nameElemForDel):
                    print("Element has been deleted")
                else:
                    print("Element hasn't been found")
            case "P" | "p" :
                printAllList(globalList)
            case "U" | "u" :
                updeteElement(globalList)
            case "X" | "x" :
                print("Exit")
                break
            case _:
                print("Wrong operation")

main()