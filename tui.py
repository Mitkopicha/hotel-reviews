"""
TUI is short for Text-User Interface. This module is responsible for communicating with the user.
The functions in this module will display information to the user and/or retrieve a response from the user.
Each function in this module should utilise any parameters and perform user input/output.
A function may also need to format and/or structure a response e.g. return a list, tuple, etc.
Any errors or invalid inputs should be handled appropriately.
Please note that you do not need to read the data file or perform any other such processing in this module.
"""
import csv
import json


def welcome():
    title = "Hotel Reviews"
    num_ast = len(title)
    welcome_mes = f"\n{'*' * num_ast} {title} {'*' * num_ast}\n"
    print(welcome_mes)


def error(msg):
    print(f"Error! {msg}.")


def progress(operation, value):
    status = []
    if value == 0:
        status = "initiated"
        print(f" Operation: {operation} [  {value}%]")

    elif 0 < value < 100:
        status = "In progress"
        print(f" Operation: In progress [ {value}%] completed\n")

    elif value == 100:
        status = "completed"
        print(f" Operation: {operation}  [{value}%]\n")


def main_menu():
    print(
        "\t\t\t|| MENU ||\n\t\t[1] Process Data\n\t\t[2] Visualise Data\n\t\t[3] Export Data\n\t\t[4] Exit\n")
    variant = input("Select an option from the above menu:")

    if variant == 1:
        print("You have selected to process data.\n")

    elif variant == 2:
        print("You have selected to visualise data.\n")
        return int(variant)
    elif variant == 3:
        print("You have selected to export data.\n")
        return int(variant)
    elif variant == 4:
        print('[4] Exit')
        return int(variant)

    return variant


def sub_menu(variant):
    if not variant or variant == 0:
        print("       Error has occurred. "
              "Please choose a different option.")
        return 0

    elif variant == 1:
        print(
            "\t\t\t|| MENU ||\n\t\t[1] Reviews for Hotels by name\n\t\t[2] Reviews for Hotels by dates\n\t\t[3] Reviews for Hotels by nationality\n\t\t[4] Reviews Summary by date\n\t\t[5] Reviews Summary by name\n\t\t[6] Negative and Positive reviews by date\n\t\t[7] Negative and Positive reviews by hotel name\n")

    elif variant == 2:
        print(
            "\n\t\t\t|| MENU ||\n\t\t[1] Positive/Negative Pie Chart\n\t\t[2] Reviews Per Nationality Chart\n\t\t[3] Animated Summary\n")

    elif variant == 3:
        print("\n\t\t\t|| MENU ||\n\t\t[1] All Reviews\n\t\t[2] Reviews for Specific Hotel\n")

    else:
        print("Invalid option selected! Please try again.")
        return 0
    while True:
            option = input("Please select an option from the above menu:")
            if option not in ['1', '2', '3', '4', '5', '6', '7']:
                print("Error: Invalid option. Please try again.\n")
                continue

            if variant == 1 and int(option) in [1, 2, 3, 4, 5, 6, 7]:
                print(f"You have selected option {option}.")
            elif variant == 2 and option == '1':
                print("You have selected to see a positive/negative pie chart.")
            elif variant == 2 and option == '2':
                print("You have selected to see the reviews per nationality chart.")
            elif variant == 2 and option == '3':
                print("You have selected to see a animated summary of the hotel reviews.")
            else:
                print(" Invalid option. Please try again.\n")
                continue
            return option


def total_reviews(num_reviews):
    print(f" There are {num_reviews} reviews in the data set.")


def hotel_name():
    print("Please enter a hotel name (e.g. Hotel Arena): ")
    hotel_n = input()
    return hotel_n


def review_dates():
    dates = []
    while True:
        review_input = input("Enter a review date in the format mm/dd/yyyy(e.g.06/24/2017) or 9 to stop: ")
        if review_input == '9':  # -Conditional statement
            break  # - Break from the while loop
        split_input = review_input.split('/')  # -Split the review_input string using the '/' delimiter
        if len(split_input) != 3:  # -Comparing the amount of "split_input" if its not 3
            print("Invalid data format")  # -Printing a error message
            continue

        try:  # exception handling
            month = int(split_input[0])  # Convert the split strings into integers
            day = int(split_input[1])
            year = int(split_input[2])
        except ValueError:  # Appropriately handling the case where the data format is invalid.
            print("Invalid data format")  # -Printing a error message
            continue

        if not (1 <= month <= 12):  # -If the month input is not more than 12 and less than 1
            print("Month out of range")
            continue
        elif not (1 <= day <= 31):  # -If the day input is not more than 31 and less than 1
            print("Day out of range")
            continue
        elif not (2014 <= year <= 2017):  # -If the year input is not more than 2017 and less than 2014
            print("Year out of range")
            continue
        dates.append(review_input)  # Append the review_input to the dates list return dates #
    print(dates)
    return dates


def display_review(review, cols=None):
    if cols is None or len(cols) == 0:
        print(review)
    else:
        col_ind = [review[x] for x in cols]
        print(col_ind)


def display_reviews(reviews, cols=None):
    reviews = []
    for review in reviews:
        if cols is None:
            print(review)
        else:
            display_data = []
            for col in cols:
                if col < len(review):
                    display_data.append(review[col])
            print(display_data)


def load_csv(hotel_reviews):  # We are defining a function inside of "tui" in order to load our csv file
    reviews_date = []
    try:  # exception handling
        with open(hotel_reviews) as r:  # open the file hotel_reviews
            reader = csv.reader(r)  # we introduce the reader
            next(reader)
            for review in reader:  # introduce a for loop to irritate through the data in the csv file
                reviews_date.append(review)  # import the csv file into a list
        return reviews_date
    except FileNotFoundError:  # Appropriately handling the case where the file cannot be found or loaded.
        error("         Error!"
              "File could not be found.")
        print(reviews_date)
    return reviews_date





#def print_summary_by_name(total_negative_reviews, total_positive_reviews, average_rating, user_name):
     #   print(f"\nSummary for {user_name}:")
      #  print(f"Total Negative Reviews: {total_negative_reviews}")
     #   print(f"Total Positive Reviews: {total_positive_reviews}")
     #   print(f"Average Rating: {average_rating:.2f}")

def print_summary_by_date(total_negative_reviews, total_positive_reviews, average_rating,user_date):

    print(f"\nSummary for {user_date}:")
    print(f"Total Negative Reviews: {total_negative_reviews}")
    print(f"Total Positive Reviews: {total_positive_reviews}")
    print(f"Average Rating: {average_rating:.2f}\n")



def by_date_pos_neg(positive_reviews, negative_reviews, user_date, reviews_date, calculate_average):
    if positive_reviews and negative_reviews:
        print("\nPositive Reviews:")
        for review in positive_reviews:
            print(f"-{review}")

        print("\nNegative Reviews:")
        for review in negative_reviews:
            print(f"-{review}")

    if len(user_date) == 10:
        average = calculate_average(reviews_date, user_date)
        print(f"\nThe average rating for '{user_date}' review date is: {average}\n")
    else:
        print("No reviews found for the given date."
              "  Please enter a different date.")


class ReviewExporter:
    def __init__(self, reviews):
        self.reviews = reviews

    def export_to_json(self, hotel_reviews):
        data = []
        for review in self.reviews:
            review_data = {
                'Review_Date': review[0],
                'Hotel_Name': review[1],
                'Positive_Review': review[2],
                'Negative_Review': review[3],
                'Reviewer_Nationality': review[4],
                'Reviewer_Score': review[5],
                'Total_Reviews_By_Reviewer': review[6],
                'Tags': review[7],
                'days_since_review': review[8]
            }
            data.append(review_data)

        with open(hotel_reviews, 'w') as file:
            json.dump(data, file, indent=4)

    def export_to_csv(self, hotel_reviews):
        with open(hotel_reviews, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Review_Date', 'Hotel_Name', 'Positive_Review', 'Negative_Review', 'Reviewer_Nationality',
                             'Reviewer_Score', 'Total_Reviews_By_Reviewer', 'Tags', 'days_since_review'])
            writer.writerows(self.reviews)


def find_hotel_reviews():
    while True:
        hotel_name = input("Please enter the hotel name (e.g. Hotel Arena) or '9' to stop: ")
        if hotel_name == '9':
            break
        with open('hotel_reviews.csv', 'r') as file:
            reader = csv.DictReader(file)
            found_hotel = False
            for row in reader:
                if row[1] == hotel_name:
                    found_hotel = True
                    print('\nPositive Review:', row['Positive_Review'])
                    print('\nNegative Review:', row['Negative_Review'])
                    print('\nReviewer Nationality:', row['Reviewer_Nationality'])
                    print('Reviewer Score:', row['Reviewer_Score'])
                    print('Total Reviews by Reviewer:', row['Total_Reviews_By_Reviewer'])
                    print('Days Since Review:', row['days_since_review'])
                    print('-------------------------')
            if not found_hotel:
                print("Invalid hotel name. Please try again.")



def load_csv_dict(hotel_reviews):
    reviews_data_dict = []

    with open(hotel_reviews) as file:
        reader = csv.DictReader(file)
        for row in reader:
            reviews_data_dict.append(row)
    return reviews_data_dict


def is_valid_date(date_str):
    parts = date_str.split('/')
    if len(parts) != 3:
        return False

    try:
        month = int(parts[0])
        day = int(parts[1])
        year = int(parts[2])

        if not (1 <= month <= 12 and 1 <= day <= 31 and 2015 <= year <= 2017):
            print("Incorrect date! Please try again")

    except ValueError:
        return False

    return True



#def get_hotel_index(user_name, reviews_data):
  #  for index, row in enumerate(reviews_data):
      #  if row[1] == user_name:
        #    return index


