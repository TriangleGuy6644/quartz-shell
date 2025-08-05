import requests

def main(args):
    url = input("Enter webhook URL: ")
    message = input("Enter message: ")
    
    data = {"content": message}
    try:
        r = requests.post(url, json=data)
        if r.status_code == 204 or r.status_code == 200:
            print("Message sent successfully!")
        else:
            print(f"Failed to send message. Status code: {r.status_code}")
    except Exception as e:
        print(f"Error: {e}")
