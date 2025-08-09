import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r") as handle:
        return json.load(handle)


def serialize_animal(animal):
    """
    Displays selected info about  animal
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
    # Load animal data from the JSON file
    animal_date = load_data("animals_data.json")

    # Read the content of the animals_template.html
    with open("animals_template.html", "r") as file:
        read_html = file.read()

    animals_short_info = display_animals_info(animal_date)

    # Replace text in html with extracted info
    main_html = read_html.replace("__REPLACE_ANIMALS_INFO__", animals_short_info)

    # Write the new HTML content to a new file, main.html
    with open("main.html", "w") as final_file:
        final_file.write(main_html)


if __name__ == "__main__":
    main()
