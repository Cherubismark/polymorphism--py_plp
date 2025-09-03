# 🐍 Python OOP Assignment

This project contains solutions for **Assignment 1** and **Activity 2** based on Object-Oriented Programming (OOP) in Python.

---

## 📘 Assignment 1: Design Your Own Class

We designed a **Smartphone** class with the following features:

- **Attributes:** brand, model, and price (encapsulated as a private variable).
- **Methods:** 
  - `call()` → Simulates making a phone call.
  - `get_price()` → Returns the phone’s price.
- **Encapsulation:** The `__price` attribute is private and can only be accessed through `get_price()`.
- **Inheritance:** `SmartPhoneWithCamera` inherits from `Smartphone` and adds a new attribute `camera_megapixels` and a method `take_photo()`.

### Example Usage
```python
phone1 = Smartphone("Samsung", "Galaxy S23", 900)
phone1.call("0722334455")
print(phone1.get_price())

phone2 = SmartPhoneWithCamera("Apple", "iPhone 15", 1200, 48)
phone2.take_photo()
phone2.call("0112233445")
🎭 Activity 2: Polymorphism Challenge
We demonstrate polymorphism by creating different classes (Dog, Bird, Car, Plane) that all implement a move() method. Each class defines its own behavior for move().

Example Usage
python
Copy
Edit
things = [Dog(), Bird(), Car(), Plane()]

for thing in things:
    thing.move()
Output
csharp
Copy
Edit
Dog is running 🐕💨
Bird is flying 🐦✈️
Car is driving 🚗
Plane is flying ✈️
🚀 Key OOP Concepts Covered
Classes and Objects

Constructors (__init__)

Encapsulation

Inheritance

Polymorphism

▶️ How to Run
Clone or download this project.

Open a terminal and navigate to the project folder.

Run any file using:

bash
Copy
Edit
python filename.py
Example:

bash
Copy
Edit
python class.py
python polymorphism.py
