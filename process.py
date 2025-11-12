from tui import *

"""
This module is responsible for processing the data.  Each function in this module will take a list of reviews,
process it and return the desired result.
"""

"""
Task 16 - 20: Write suitable functions to process the data.

Each of the functions below should follow the pattern:
- Take a list of reviews (where each review is a list of data values) as a parameter.
- Process the list of reviews appropriately.  You may use the module 'tui' to retrieve any additional information 
required from the user to complete the processing.
- Return a suitable result

The required functions are as follows:
- Retrieve the total number of reviews that have been loaded.
- Retrieve the reviews for a hotel where the hotel name is specified by the user.
- Retrieve the reviews for the dates specified by the user.
- Retrieve all the reviews grouped by the reviewer’s nationality.
- Retrieve a summary of all the reviews. This should include the following information for each date in ascending order:
    - the total number of negative reviews on that date
    - the total number of positive reviews on that date
    - the average rating on that date
"""


def total_number_of_reviews(reviews_date):
    return len(reviews_date)  # -Returns the length of the provided list, which represents the total number of reviews


def by_name(reviews_date):  # -Defines a function named "by_name" that takes a list of reviews as a parameter
    while True:  # -Starts a loop to prompt the user to enter a hotel name or '9' to stop the input
        hotel_name = input("Please enter the hotel name (e.g. Hotel Arena) or '9' to stop: ")

        if hotel_name == '9':  # -Starts a loop to prompt the user to enter a hotel name or '9' to stop the input
            break

        found_hotel = False  # -Initializes a variable to track if a hotel is found
        by_names = []  # - Initializes a list to store the hotel names

        for row in reviews_date:  # Iterates over each row in the reviews
            if row[1] == hotel_name:  # Checks if the hotel name matches the user input
                print(f"\n {row}")
                by_names.append(hotel_name)  # Adds the hotel name to the list.
                found_hotel = True  # - Sets "found_hotel" to truee

        if not found_hotel:  # -If no matching hotel is found prints a message and continues to the next iteration of the loop
            print("\nNo such hotel name! Please try again.")
            continue
        return by_names  # -If a hotel is found, returns the list of hotel names


def by_dates(reviews_date):
    revs = reviews_date  # -Assign the list 'reviews_date' to 'revs'
    rev_dates = review_dates()  # -Assign the list 'reviews_date' to 'rev_dates'
    for rev in revs:  # Iterates over each review in "revs"
        if rev[0] in rev_dates:  # Iterates over each review in "revs"
            display_review(rev)
            return revs  # -Returns the list of reviews.


def by_nationality(reviews_date):
    nationalities = set(row[4] for row in reviews_date)
    # Creates a set of unique nationalities by extracting the nationality value from each row in the list of reviews
    stop = "9"  # Sets "stop_keyword" to '9'.

    while True:  # Introducing a loop to prompt the user to enter a nationality or '9' to stop
        nationality = input("\nPlease enter the nationality or '9' to stop:")
        if nationality == stop:  # Checks if the user entered '9' to break from the loop
            break
        if nationality in nationalities:  # Checks if the entered nationality is in the set
            negative_reviews = []  ##- Create a list for negative reviews
            positive_reviews = []  ##- Create a list for positive reviews

            for row in reviews_date:  # - Iterates over each row in the reviews.
                if row[4] == nationality:  # Checks if the nationality from index 4 matches the entered nationality.
                    if row[3] != "No Negative":  # Checks if the row has no negative revieews.
                        negative_reviews.append(row[3])
                    positive_reviews.append(row[2])

            if negative_reviews:  # - Checks if there are negative reviews  prints them.
                print(f"Negative reviews for {nationality} nationality.")
                for i, review in enumerate(negative_reviews, 1):
                    print(f"{i}. {review}")

            print(f"\nPositive reviews for {nationality} nationality.")  # Prints positive reviews.
            for i, review in enumerate(positive_reviews, 1):
                print(f"{i}. {review}")
        else:
            print("Invalid nationality. Please try again.")  # - Prints an error message


def extract_reviews_by_date(reviews_date):
    positive_reviews = []  # Initializes a list to store positive reviews
    negative_reviews = []  # Initializes a list to store negative reviews

    while True:  # Introduce a loop to prompt the user to enter a date in the valid format
        user_date = input("Please enter a date in the format mm/dd/yyyy (e.g. 06/24/2017): ")
        if is_valid_date(user_date):  # Checks if the entered date is valid
            break
        else:
            print("Invalid date format. Please try again.")  # Prints an error message for an invalid date format
    for review in reviews_date:  # Iterates over each review in the list of reviews
        date = review[0]  # Assign to the variable 'date' the data from index 0
        positive_review = review[2] # Assign to the variable 'positive_review' the data from index 2
        negative_review = review[3] # Assign to the variable 'negative_review ' the data from index 3

        if date == user_date:  # Checks if the reviews date matches the user entered date
            positive_reviews.append(positive_review)  # Adds the positive review to the lis
            negative_reviews.append(negative_review)  # Adds the negative review to the list
    return positive_reviews, negative_reviews, user_date
    # Returns the positive reviews, negative reviews, and the user entered date


def calculate_average(reviews_date, user_date):
    total = 0  ## Introducing a variable to store the total rating
    count = 0  ## Introducing a variable to store the count of reviews

    for row in reviews_date:  ## Iterates over each row in the list of reviews
        if row[0] == user_date:  ## Checks if the row's date matches the user entered date
            value = float(row[5])  ## Converts the rating to a float value
            total += value  ## Adds the rating value to the total
            count += 1  ## Increments the count by 1
    if count == 0:
        return None  ## -Returns None if no matching rows are found
    else:
        return total / count  ## -Calculates and returns the average rating


def calculate_average_by_name(reviews_date, user_hotel):
    total = 0  # Introducing a variable to store the total rating
    count = 0  # Introducing a variable to store the count of reviews

    for row in reviews_date:  # Iterates over each row in the list of reviews
        if row[1].lower() == user_hotel.lower():  # Checks if index 1 name matches the user entered hotel name
            value = float(row[5])  # Converts the rating to a float value
            total += value  # Adds the rating value to the total
            count += 1  # Increments the count by 1

    if count == 0:
        return None  # Returns None if no matching rows are found
    else:
        return total / count  # Calculates and returns the average rating


def get_hotel_reviews_summary(reviews_date):
    while True:  # Starts with a loop to prompt the user to enter a hotel name
        hotel_name = input("Please enter the hotel name(e.g. Hotel Arena): ")

        positive_reviews = 0  # - Variable to store the count of positive reviews
        negative_reviews = 0  # - Variable to store the count of negative reviews
        average_rating = 0.0  # - variable to store the average rating
        count = 0  # - Variable to store the count of reviews

        for review in reviews_date:  # Iterates over each row in the list of reviews
            if review[1].lower() == hotel_name.lower():  # Checks if index 1  the user entered hotel name

                positive_reviews += 1  # Increments the count of positive reviews by 1

                negative_reviews += 1  # Increments the count of negative reviews by 1
                average_rating += float(review[5])
                count += 1  # Increments the count by 1

        if count > 0:
            total_negative_reviews = negative_reviews
            total_positive_reviews = positive_reviews
            average_rating /= count  # Calculates the average rating

            print(f"\nSummary for {hotel_name}:")  # Print the hotel name inputted
            print(f"Total Negative Reviews: {total_negative_reviews}")  # Prints the total negative reviews
            print(f"Total Positive Reviews: {total_positive_reviews}")  # Prints the total positive reviews
            print(f"Average Rating: {average_rating:.2f}\n")  # Prints the average rating
            break
        else:
            print("Invalid hotel name. Please try again.\n")  # Displays and error message
