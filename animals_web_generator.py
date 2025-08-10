import requests


def get_animal_info_by_name(animal_name):
    """
    Makes an API call to get information about an animal.
    Returns a list of animal data in JSON format or None in case of an error
    """
    api_url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
    response = requests.get(api_url, headers={'X-Api-Key': '7Hm0KVhv6IXpNIOD1KvPQw==QpGHB1IRQiRAgeCE'})
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        print("Error:", response.status_code, response.text)
        return None


def serialize_animal(animal):
    """
    Formats the animal data into an HTML string
    """
    # define an empty string
    output = ""
    name = animal.get("name")
    diet = animal.get("characteristics", {}).get("diet")
    location = animal.get("locations",[])[0]
    animal_type = animal.get("characteristics", {}).get("type")

    # append information to each string
    output += '<li class="cards__item">'
    output += f'<div class ="card__title">{name}<br/>\n</div>'
    output += '<p class="card__text">'
    if diet:
        output += f"<strong>Diet: </strong>{diet}<br/>\n"
    if location:
        output += f"<strong>Location: </strong>{location}<br/>\n"
    if animal_type:
        output +=f"<strong>Type: </strong>{animal_type}<br/>\n"
    output += '</p>'
    output += '</li>'
    return output


def display_animals_info(animal_info):
    output = ""
    for animal in animal_info:
        output += serialize_animal(animal)
    return output


def main():
    animal_name = "cheetah"
    animal_data = get_animal_info_by_name(animal_name)

    # Read the content of the animals_template.html
    with open("animals_template.html", "r") as file:
        read_html = file.read()

    animals_short_info = display_animals_info(animal_data)

    # Replace text in html with extracted info
    main_html = read_html.replace("__REPLACE_ANIMALS_INFO__", animals_short_info)

    # Write the new HTML content to a new file, animals.html
    with open("animals.html", "w") as final_file:
        final_file.write(main_html)


if __name__ == "__main__":
    main()
