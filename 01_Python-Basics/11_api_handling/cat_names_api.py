# Fetching cat names using a random API

import requests
print("Program Started")
def fetch_cat_detail():
    print("Before request")
    url = "https://api.freeapi.app/api/v1/public/cats/12"
    response = requests.get(url)

    print("After request")
    data = response.json()
    print("JSON Loaded")

    if data["success"] and "data" in data and "message" in data:
        cat_name = data["data"]["alt_names"]
        cat_details = data["data"]["description"]
        success_message = data["message"]
        return cat_name,cat_details,success_message
    
    else:
        raise Exception("Failed to get the details")


def main():
    print("Inside main")
    try:
        cat_name,cat_details,success_message = fetch_cat_detail()
       # print(f"Cat Name :-{cat_name} \nAbout Cat :-{cat_details} \n{success_message}")
        print(cat_details,cat_name,success_message)

    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()               

