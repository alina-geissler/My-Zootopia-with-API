import data_fetcher

TEMPLATE_PATH = 'animals_template.html'
OUTPUT_HTML_PATH = 'animals.html'
PLACEHOLDER_ANIMALS_INFO = '__REPLACE_ANIMALS_INFO__'


def get_animal_by_user():
    """
    Ask user for animal the website should be about.
    :return: name of the chosen animal (or a string with a single space to select all animals)
    """
    animal = input("Enter a name of an animal (or leave blank for all animals available): ")
    if not animal or animal.count(" ") == len(animal):
        animal = ' '
    return animal


def load_template(file_path):
    """
    Load an HTML template
    :param file_path: source of the template
    :return: HTML template
    """
    with open(file_path, "r") as handle:
        return handle.read()


def serialize_animal(animal_obj):
    """
    Create HTML card element for an animal
    :param animal_obj: information to use for card element
    :return: HTML code for card element
    """
    output = ['<li class="cards__item">\n',
              f'<div class="card__title" style="margin: 20;">{animal_obj.get("name")}</div>\n',
              '<div class="card__text">\n',
              '<ul style="list-style-type:none;">\n'
              ]
    locations = animal_obj.get('locations')
    if locations:
        output.append(f'<li><strong>Location:</strong> {locations[0]}</li>\n')
    if animal_obj.get('characteristics'):
        habitat = animal_obj.get('characteristics').get('habitat')
        if habitat:
            output.append(f'<li><strong>Habitat:</strong> {habitat}</li>\n')
        diet = animal_obj['characteristics'].get('diet')
        if diet:
            output.append(f'<li><strong>Diet:</strong> {diet}</li>\n')
        animal_type = animal_obj.get('characteristics').get('type')
        if animal_type:
            output.append(f'<li><strong>Type:</strong> {animal_type}</li>\n')
        skin_type = animal_obj.get('characteristics').get('skin_type')
        if skin_type:
            output.append(f'<li><strong>Skin:</strong> {skin_type}</li>\n')
        color = animal_obj.get('characteristics').get('color')
        if color:
            output.append(f'<li><strong>Color:</strong> {color}</li>\n')
    output.append('</ul>\n')
    output.append('</div>\n')
    output.append('</li>\n')
    output_as_string = "".join(output)
    return output_as_string


def select_skin_type(skin_types):
    """
    Let user decide which animals should appear on the website.
    :param skin_types: available skin types of chosen animal
    :return: selected skin type
    """
    if None in skin_types:
        skin_types.remove(None)
    while True:
        skin_type = input(f"Choose between {skin_types} or leave blank for all animals: ").title().strip()
        if skin_type in skin_types or skin_type == "":
            return skin_type
        else:
            print("Please select an available type.")


def create_html_file(skin_type, animals_data):
    """
    Generate HTML file based on user choice.
    :param animals_data: information to use for HTML file (data from API in JSON format)
    :param skin_type: type selected by user
    """
    template = load_template(TEMPLATE_PATH)
    if skin_type == "":
        output = []
        for animal_obj in animals_data:
            output.append(serialize_animal(animal_obj))
    else:
        output = []
        for animal_obj in animals_data:
            if animal_obj.get("characteristics"):
                if animal_obj.get("characteristics").get("skin_type") == skin_type:
                    output.append(serialize_animal(animal_obj))
    output_string = "".join(output)
    html_with_data = template.replace(PLACEHOLDER_ANIMALS_INFO, output_string)
    with open(OUTPUT_HTML_PATH, "w") as handle:
        handle.write(html_with_data)


def main():
    """
    Execute the main program: greet user, get animal name and skin type input and generate HTML file accordingly.
    """
    print("\nWelcome to your Animal Repository Generator!\n")
    while True:
        print("Which animal should your website be about?")
        animal_input = get_animal_by_user()
        try:
            animals_data = data_fetcher.fetch_data(animal_input)
        except ValueError:
            print("\nInvalid API key used to fetch data! Please add a valid API key to .env file!")
            quit()
        if not animals_data:
            print(f"\nThe animal '{animal_input}' doesn't exist.\n")
            continue
        else:
            break

    skin_types = list(set([animal["characteristics"].get("skin_type") for animal in animals_data
                           if animal.get("characteristics")]))
    if skin_types:
        print("\nPlease select the SKIN TYPE you want the animals on your website to have.")
        selected_skin_type = select_skin_type(skin_types)
    else:
        selected_skin_type = ""
    create_html_file(selected_skin_type, animals_data)
    print("\nYour HTML file has been created!")


if __name__ == "__main__":
    main()







