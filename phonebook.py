"""
=========================================
 Professional PhoneBook
 Author : QeYsAr
 Version : 1.0
=========================================
"""

import json
import os
from datetime import datetime


class PhoneBook:

    def __init__(self):

        self.file_name = "contacts.json"

        self.contacts = []

        self.load_contacts()

    # ================================
    # File
    # ================================

    def load_contacts(self):

        if not os.path.exists(self.file_name):

            with open(self.file_name, "w", encoding="utf-8") as file:

                json.dump([], file)

        try:

            with open(self.file_name, "r", encoding="utf-8") as file:

                self.contacts = json.load(file)

        except:

            self.contacts = []

    def save_contacts(self):

        with open(self.file_name, "w", encoding="utf-8") as file:

            json.dump(

                self.contacts,

                file,

                indent=4,

                ensure_ascii=False

            )

    # ================================
    # Validation
    # ================================

    def phone_exists(self, phone):

        for contact in self.contacts:

            if contact["phone"] == phone:

                return True

        return False

    # ================================
    # Add Contact
    # ================================

    def add_contact(self):

        print("\n========== ADD CONTACT ==========\n")

        name = input("Name : ").strip().title()

        phone = input("Phone: ").strip()

        if self.phone_exists(phone):

            print("\nPhone number already exists.")

            return

        email = input("Email: ").strip()

        address = input("Address: ").strip()

        category = input("Category: ").strip().title()

        contact = {

            "name": name,

            "phone": phone,

            "email": email,

            "address": address,

            "category": category,

            "favorite": False,

            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M")

        }

        self.contacts.append(contact)

        self.save_contacts()

        print("\n✅ Contact Added Successfully.")
        # ================================
    # Show Contacts
    # ================================

    def show_contacts(self):

        if len(self.contacts) == 0:

            print("\nNo contacts found.")

            return

        print("\n" + "=" * 60)
        print("CONTACT LIST")
        print("=" * 60)

        for index, contact in enumerate(self.contacts, start=1):

            star = "⭐" if contact["favorite"] else ""

            print(f"""
[{index}] {star}

Name      : {contact['name']}
Phone     : {contact['phone']}
Email     : {contact['email']}
Address   : {contact['address']}
Category  : {contact['category']}
Created   : {contact['created_at']}
""")

            print("-" * 60)

    # ================================
    # Search
    # ================================

    def search_contact(self):

        keyword = input("\nSearch: ").strip().lower()

        found = False

        for contact in self.contacts:

            if (

                keyword in contact["name"].lower()

                or keyword in contact["phone"]

                or keyword in contact["email"].lower()

            ):

                found = True

                print("\n-----------------------------")

                print(f"Name     : {contact['name']}")

                print(f"Phone    : {contact['phone']}")

                print(f"Email    : {contact['email']}")

                print(f"Category : {contact['category']}")

        if not found:

            print("\nNo contact found.")

    # ================================
    # Delete
    # ================================

    def delete_contact(self):

        phone = input("\nPhone: ").strip()

        for contact in self.contacts:

            if contact["phone"] == phone:

                self.contacts.remove(contact)

                self.save_contacts()

                print("\nContact deleted.")

                return

        print("\nContact not found.")

    # ================================
    # Edit
    # ================================

    def edit_contact(self):

        phone = input("\nPhone: ").strip()

        for contact in self.contacts:

            if contact["phone"] == phone:

                print("\nLeave empty to keep old value.\n")

                name = input(f"Name ({contact['name']}): ")

                email = input(f"Email ({contact['email']}): ")

                address = input(f"Address ({contact['address']}): ")

                category = input(f"Category ({contact['category']}): ")

                if name:

                    contact["name"] = name.title()

                if email:

                    contact["email"] = email

                if address:

                    contact["address"] = address

                if category:

                    contact["category"] = category.title()

                self.save_contacts()

                print("\nContact updated.")

                return

        print("\nContact not found.")
        # ================================
    # Favorites
    # ================================

    def toggle_favorite(self):

        phone = input("\nPhone: ").strip()

        for contact in self.contacts:

            if contact["phone"] == phone:

                contact["favorite"] = not contact["favorite"]

                self.save_contacts()

                if contact["favorite"]:

                    print("\n⭐ Added to favorites.")

                else:

                    print("\nRemoved from favorites.")

                return

        print("\nContact not found.")

    def show_favorites(self):

        found = False

        print("\n========== FAVORITES ==========\n")

        for contact in self.contacts:

            if contact["favorite"]:

                found = True

                print(f"""
Name      : {contact['name']}
Phone     : {contact['phone']}
Email     : {contact['email']}
Category  : {contact['category']}
""")

                print("-" * 50)

        if not found:

            print("No favorite contacts.")

    # ================================
    # Sort
    # ================================

    def sort_contacts(self):

        self.contacts.sort(

            key=lambda contact: contact["name"].lower()

        )

        self.save_contacts()

        print("\nContacts sorted successfully.")

    # ================================
    # Statistics
    # ================================

    def statistics(self):

        total = len(self.contacts)

        favorites = 0

        family = 0

        friends = 0

        work = 0

        for contact in self.contacts:

            if contact["favorite"]:

                favorites += 1

            category = contact["category"].lower()

            if category == "family":

                family += 1

            elif category == "friend":

                friends += 1

            elif category == "work":

                work += 1

        print("\n========== STATISTICS ==========\n")

        print(f"Total Contacts : {total}")

        print(f"Favorites      : {favorites}")

        print(f"Family         : {family}")

        print(f"Friends        : {friends}")

        print(f"Work           : {work}")
        # ================================
    # Main Menu
    # ================================

    def menu(self):

        while True:

            print("\n" + "=" * 50)
            print("      PROFESSIONAL PHONEBOOK")
            print("=" * 50)
            print("1. Add Contact")
            print("2. Show Contacts")
            print("3. Search Contact")
            print("4. Edit Contact")
            print("5. Delete Contact")
            print("6. Favorite / Unfavorite")
            print("7. Show Favorites")
            print("8. Sort Contacts")
            print("9. Statistics")
            print("0. Exit")
            print("=" * 50)

            choice = input("Choose: ").strip()

            if choice == "1":

                self.add_contact()

            elif choice == "2":

                self.show_contacts()

            elif choice == "3":

                self.search_contact()

            elif choice == "4":

                self.edit_contact()

            elif choice == "5":

                self.delete_contact()

            elif choice == "6":

                self.toggle_favorite()

            elif choice == "7":

                self.show_favorites()

            elif choice == "8":

                self.sort_contacts()

            elif choice == "9":

                self.statistics()

            elif choice == "0":

                print("\nSaving contacts...")

                self.save_contacts()

                print("Good Bye 👋")

                break

            else:

                print("\nInvalid Choice!")


# ===================================
# Program Start
# ===================================

if __name__ == "__main__":

    phonebook = PhoneBook()

    phonebook.menu()