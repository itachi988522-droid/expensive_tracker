import datetime
import os
import mysql.connector
from dotenv import load_dotenv

# .env file se variables load karo
load_dotenv()

# Database Connection using Environment Variables
db = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME"),
)
cursor = db.cursor()


def add_expense():
  title = input("Kharcha kis cheez par hua?: ")
  amount = float(input("Kitna kharcha hua (₹)?: "))
  category = input("Category (Food/Travel/Study/Shopping): ")
  date = datetime.date.today()

  query = "INSERT INTO expenses (title, amount, category, date) VALUES (%s, %s, %s, %s)"
  values = (title, amount, category, date)

  cursor.execute(query, values)
  db.commit()
  print("✅ Expense successfully add ho gaya!\n")


def view_expenses():
  cursor.execute("SELECT * FROM expenses")
  results = cursor.fetchall()

  print("\n---------------- SARA KHARCHA ----------------")
  if not results:
    print("Abhi koi expense record nahi hai.")
  else:
    for row in results:
      print(
          f"ID: {row[0]} | Item: {row[1]} | Amount: ₹{row[2]} | Category:"
          f" {row[3]} | Date: {row[4]}"
      )
  print("----------------------------------------------\n")


while True:
  print("1. Add Expense")
  print("2. View Expenses")
  print("3. Exit")
  choice = input("Option select karo (1/2/3): ")

  if choice == "1":
    add_expense()
  elif choice == "2":
    view_expenses()
  elif choice == "3":
    print("Project exited.")
    break
  else:
    print("Sahi option chun bhai!\n")