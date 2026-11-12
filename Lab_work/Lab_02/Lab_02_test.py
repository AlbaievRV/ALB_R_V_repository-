from lab_02 import addElemToSortedList
from lab_02 import deleteElem
from lab_02 import findPosition


def test_findPosition():
  listForFind = [
      {
          "name": "Bob",
          "phone": "0631234567",
          "email": "bob@mail.com",
          "age": "20",
      },
      {
          "name": "Emma",
          "phone": "0631234567",
          "email": "emma@mail.com",
          "age": "21",
      },
      {
          "name": "Jon",
          "phone": "0631234567",
          "email": "jon@mail.com",
          "age": "22",
      },
      {
          "name": "Zak",
          "phone": "0631234567",
          "email": "zak@mail.com",
          "age": "19",
      },
  ]

  assert findPosition(listForFind, "Bob") == 0
  assert findPosition(listForFind, "Emma") == 1
  assert findPosition(listForFind, "Zak") == 3
  assert findPosition(listForFind, "Michael") == 3


def test_addElemToSortedList():
  listForAdd = [
      {
          "name": "Emma",
          "phone": "0631234567",
          "email": "emma@mail.com",
          "age": "21",
      },
  ]

  addElemToSortedList(
      listForAdd,
      {
          "name": "Anna",
          "phone": "12121212",
          "email": "anna@mail.com",
          "age": "18",
      },
  )
  assert listForAdd[0]["name"] == "Anna"

  addElemToSortedList(
      listForAdd,
      {"name": "Bob", "phone": "12121212", "email": "bob@mail.com", "age": "20"},
  )
  assert listForAdd[1]["name"] == "Bob"


def test_deleteElem():
  listForDel = [
      {
          "name": "Bob",
          "phone": "0631234567",
          "email": "bob@mail.com",
          "age": "20",
      },
      {
          "name": "Emma",
          "phone": "0631234567",
          "email": "emma@mail.com",
          "age": "21",
      },
      {
          "name": "Jon",
          "phone": "0631234567",
          "email": "jon@mail.com",
          "age": "22",
      },
      {
          "name": "Zak",
          "phone": "0631234567",
          "email": "zak@mail.com",
          "age": "19",
      },
  ]

  assert listForDel[0]["name"] == "Bob"
  assert deleteElem(listForDel, "Bob") == True
  assert listForDel[0]["name"] == "Emma"