def print_formatted_text(formatted_rows):
    print("".join(formatted_rows))


def add_list(type_of_list):
    global formatted_text
    while True:
        number_of_rows = int(input("- Number of rows: > "))
        if number_of_rows >= 1:
            break
        else:
            print("The number of rows should be greater than zero")
    raw_list = [input(f"- Row #{actual_row}: > ") for actual_row in range(1, number_of_rows + 1)]
    if type_of_list == "ordered":
        formatted_text += (list(map(lambda n_of_row, list_text:
                                    f"{n_of_row}. {list_text}\n", range(1, number_of_rows + 1), raw_list)))
    elif type_of_list == "unordered":
        formatted_text += (list(map(lambda list_text: f"* {list_text}\n", raw_list)))
    return None


def add_text(type_of_text):
    global formatted_text
    raw_text = input("- Text: > ")
    if type_of_text == "plain":
        formatted_text.append(f"{raw_text}")
    elif type_of_text == "bold":
        formatted_text.append(f"**{raw_text}**")
    elif type_of_text == "italic":
        formatted_text.append(f"*{raw_text}*")
    elif type_of_text == "inline-code":
        formatted_text.append(f"`{raw_text}`")
    return None


def add_link():
    global formatted_text
    label_of_link = input("- Label: > ")
    url_link = input("- URL: > ")
    formatted_text.append(f"[{label_of_link}]({url_link})")
    return None


def add_newline():
    global formatted_text
    formatted_text.append("\n")
    return None


def add_header():
    global formatted_text
    level_of_header = int(input("- Level: > "))
    if 1 <= level_of_header <= 6:
        text = input("- Text: > ")
        formatted_text.append(f"{'#' * level_of_header} {text}\n")
    else:
        return False
    return True


def save_results_file():
    global formatted_text
    result_file = open('output.md', 'wt')
    result_file.writelines(formatted_text)
    result_file.close()


formatted_text = []

while True:
    command = input("- Choose a formatter: > ")
    if command == "!help":
        print("Available formatters: plain bold italic header link inline-code ordered-list unordered-list new-line")
        print("Special commands: !help !done")

    elif command == "plain":
        add_text("plain")

    elif command == "bold":
        add_text("bold")

    elif command == "italic":
        add_text("italic")

    elif command == "header":
        right_level = add_header()
        if not right_level:
            print("The level should be within the range of 1 to 6")
            continue

    elif command == "link":
        add_link()

    elif command == "inline-code":
        add_text("inline-code")

    elif command == "ordered-list":
        add_list("ordered")

    elif command == "unordered-list":
        add_list("unordered")

    elif command == "new-line":
        add_newline()

    elif command == "!done":
        save_results_file()
        break

    else:
        print("Unknown formatting type or command. Please try again.")
        continue

    # Print the result
    print_formatted_text(formatted_text)
