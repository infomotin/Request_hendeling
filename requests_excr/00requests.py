import requests
def main():
    response = requests.get("https://api.exchangeratesapi.io/latest?base=USD&GBP")
    if response.status_code !=200:
        print(response.status_code)
        raise Exception("Something Wrong")
    data = response.json()
    
    for k,v in data.items():
        print(k,v)











if __name__ == "__main__":
    main()