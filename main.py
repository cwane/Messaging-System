import json
import os

# File paths
USERS_FILE = "users.json"
MESSAGES_FOLDER = "messages"

# Function to load user data from JSON file
def load_users():
    if not os.path.exists(USERS_FILE):
        return {}
    with open(USERS_FILE, 'r') as file:
        try:
            return json.load(file)
        except json.decoder.JSONDecodeError:
            return {}


# Function to save user data to JSON file
def save_users(users):
    with open(USERS_FILE, 'w') as file:
        json.dump(users, file, indent=4)

# Function to create a new user account
def create_account(username, password):
    users = load_users()
    if username in users:
        print("Username already exists. Please choose a different username.")
        return False
    users[username] = {"password": password, "messages": {}}
    save_users(users)
    print("Account created successfully.")
    return True

# Function to login user
def login(username, password):
    users = load_users()
    if username in users and users[username]["password"] == password:
        print("Login successful.")
        return True
    else:
        print("Invalid username or password.")
        return False

# Function to search for users
def search_user(username):
    users = load_users()
    if username in users:
        print(f"User '{username}' found.")
    else:
        print(f"User '{username}' not found.")

# Function to send message
def send_message(sender, receiver, message):
    message_data = {
        "sender": sender,
        "message": message
    }
    if not os.path.exists(MESSAGES_FOLDER):
        os.makedirs(MESSAGES_FOLDER)
    message_file = os.path.join(MESSAGES_FOLDER, f"{sender}_{receiver}.json")
    with open(message_file, 'a') as file:
        json.dump(message_data, file)
        file.write('\n')

# Function to delete message history
def delete_message_history(username):
    message_files = [f for f in os.listdir(MESSAGES_FOLDER) if f.startswith(username)]
    for file in message_files:
        os.remove(os.path.join(MESSAGES_FOLDER, file))
    print("Message history deleted.")

# Main function
def main():
    while True:
        print("\n1. Create Account")
        print("2. Login")
        print("3. Search User")
        print("4. Send Message")
        print("5. Delete Message History")
        print("6. Exit")
        
        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter username: ")
            password = input("Enter password: ")
            create_account(username, password)
        elif choice == '2':
            username = input("Enter username: ")
            password = input("Enter password: ")
            login(username, password)
        elif choice == '3':
            username = input("Enter username to search: ")
            search_user(username)
        elif choice == '4':
            sender = input("Enter your username: ")
            receiver = input("Enter receiver's username: ")
            message = input("Enter message: ")
            send_message(sender, receiver, message)
        elif choice == '5':
            username = input("Enter your username to delete message history: ")
            delete_message_history(username)
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
