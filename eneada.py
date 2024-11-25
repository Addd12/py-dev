import requests

def fetch_api_data(api_url):
    #1a fetch data from the given api
    try:
        request_data = requests.get(api_url)
        #print(request_data.json())
        return request_data.json()
    except Exception as exception:
        print(f"The data could not be fetched as a result of {exception}")
        return None

#2a extract titles from the api data, that contain a specific string
def extract_titles(api_data):
    print("----------------Extracting data using the first method-----------------------")
    specific_str = input("Please type the string you want to find in the title (ex. qui, aut, porro): ")
    titles = []
    print(f"List of titles that contain {specific_str}: ")
    for item in api_data:
        #get only the items that contain a specific string
        if specific_str in item['title'] and isinstance(item['title'], str):
            print(item['title'])
            #then store them in a list
            titles.append(item['title'])
    return titles

#2b extract titles from the api data, that contain a specific string using list comprehension
def extract_titles_using_list_comp(api_data):
    print("\n----------------Extracting data using list comprehension method-----------------------")
    specific_str = input("Please type the string you want to find in the title (ex. qui, aut, porro): ")
    print(f"List of titles that contain {specific_str}, extracted using list comprehension: ")

    #3b Ensure that each printed title is a string.
    titles = [item['title'] for item in api_data if specific_str in item['title'] and isinstance(item['title'], str)]
    for title in titles:
        #3a Format and print the filtered titles using f-strings.
        print(f'{title} contains the required string {specific_str}')

    return titles

#4a Demonstrate checking whether one of the extracted titles is of type int.
def check_title_for_int(titles):
    for title in titles:
        if isinstance(title, int):
            print(f'This title is of type int: {title}')
        else:
            print("\nNo int found in the title list.")
            return None

api_url = 'https://jsonplaceholder.typicode.com/todos'
fetched_data = fetch_api_data(api_url)

extract_titles(fetched_data)

titles_list = extract_titles_using_list_comp(fetched_data)

check_title_for_int(titles_list)