import data_fetcher


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
    """Receives a list of dictionaries with animal data and
    returns an HTML string containing formatted information
    for all animals.
    """
    output = ""
    for animal in animal_info:
        output += serialize_animal(animal)
    return output


def main():
    """
    Main function get name from the user, fetches the
    data from the data fetcher, generate an HTML page,
    and save it to a file.
    """
    user_animal = input("Enter the name of the animal: ")
    animal_data = data_fetcher.fetch_data(user_animal)

    # Read the content of the animals_template.html
    with open("animals_template.html", "r") as file:
        read_html = file.read()

    if animal_data:
        animals_short_info = display_animals_info(animal_data)
    else:
        # Create an error message
        error_message = f"<h2>The animal {user_animal} doesn't exist.</h2>"
        animals_short_info = error_message

    # Replace text in html with extracted info
    main_html = read_html.replace("__REPLACE_ANIMALS_INFO__", animals_short_info)

    # Write the new HTML content to a new file, animals.html
    with open("animals.html", "w") as final_file:
        final_file.write(main_html)


if __name__ == "__main__":
    main()
