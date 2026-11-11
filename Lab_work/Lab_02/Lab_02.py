import csv
import sys

# Initial default list (4 fields)
globalList = [
    {"name":"Bob", "phone":"0631234567", "email":"bob@mail.com", "age":"20"},
    {"name":"Emma", "phone":"0631234567", "email":"emma@mail.com", "age":"21"},
    {"name":"Jon",  "phone":"0631234567", "email":"jon@mail.com", "age":"22"},
    {"name":"Zak",  "phone":"0631234567", "email":"zak@mail.com", "age":"19"}
]


def printAllList(listForPrinting):
  for item in listForPrinting:
    str_out = (
        f"Name = {item['name']}, Phone = {item['phone']},"
        f" Email = {item['email']}, Age = {item['age']}"
    )
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
  nameForUpdate = input("Please enter the name of the student to update: ")
  indexForUpdate = findPosition(listForUpdate, nameForUpdate)

  if (
      indexForUpdate < len(listForUpdate)
      and listForUpdate[indexForUpdate]["name"] == nameForUpdate
  ):
    del listForUpdate[indexForUpdate]
    print("Please enter new details for the student:")
    newElem = getElement()
    addElemToSortedList(listForUpdate, newElem)
    print("Element has been updated successfully")
    return True
  else:
    print("Element hasn't been found")
    return False


def load_from_csv(filename, list_to_load):
  """Loads student data from a CSV file via command-line argument."""
  try:
    with open(filename, mode="r", encoding="utf-8") as file:
      reader = csv.DictReader(file)
      list_to_load.clear()
      for row in reader:
        list_to_load.append({
            "name": row.get("name", ""),
            "phone": row.get("phone", ""),
            "email": row.get("email", ""),
            "age": row.get("age", ""),
        })
    print(f"Data successfully loaded from {filename}")
  except FileNotFoundError:
    print(
        f"File {filename} not found. Keeping default or empty student list."
    )
  except Exception as e:
    print(f"Error loading file: {e}")


def save_to_csv(filename, list_to_save):
  """Saves student data to a CSV file before exiting."""
  try:
    with open(filename, mode="w", encoding="utf-8", newline="") as file:
      fieldnames = ["name", "phone", "email", "age"]
      writer = csv.DictWriter(file, fieldnames=fieldnames)
      writer.writeheader()
      for item in list_to_save:
        writer.writerow(item)
      print(f"Data successfully saved to {filename}")
  except Exception as e:
    print(f"Error saving file: {e}")


def main():
  # Check if CSV filename is passed via command-line arguments (sys.argv)
  csv_filename = "students.csv"  # default fallback filename
  if len(sys.argv) > 1:
    csv_filename = sys.argv[1]
    load_from_csv(csv_filename, globalList)
  else:
    print(
        "No CSV file provided in command-line arguments. Using default list."
    )

  while True:
    chouse = input(
        "Please enter the command [C - add new elem, D - delete elem, P - print"
        " all List, U - update element, X - exit]: "
    )
    match chouse:
      case "C" | "c":
        newElem = getElement()
        addElemToSortedList(globalList, newElem)
      case "D" | "d":
        nameElemForDel = input("Please enter the name for delete: ")
        if deleteElem(globalList, nameElemForDel):
          print("Element has been deleted")
        else:
          print("Element hasn't been found")
      case "P" | "p":
        printAllList(globalList)
      case "U" | "u":
        updeteElement(globalList)
      case "X" | "x":
        # Save current state to CSV before exit
        save_to_csv(csv_filename, globalList)
        print("Exit")
        break
      case _:
        print("Wrong operation")


if __name__ == "__main__":
  main()