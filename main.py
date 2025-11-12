
from process import *
from tui import *
from visual import *

# Task 11: Import required modules and create an empty list named 'reviews_data'.
"""
This module is responsible for the overall program flow. It controls how the user interacts with the
program and how the program behaves. It uses the other modules to interact with the user, carry out
processing, and for visualising information.

Note:   any user input/output should be done using the appropriate functions in the module 'tui'
        any processing should be done using the appropriate functions in the module 'process'
        any visualisation should be done using the appropriate functions in the module 'visual'
"""

# This will be used to store the data read from the source data file.
hotel_reviews = 'hotel_reviews.csv'# - Replace with the path to the CSV file
reviews_date = load_csv(hotel_reviews)# - Loading the CSV file into the variable


def run():
    # Task 12: Call the function welcome of the module 'tui'.
    # This will display our welcome message when the program is executed.
    welcome()  # calling the function to display the welcoming message

    # Task 13: Load the data.
    # - Use the appropriate function in the module 'tui' to display a message to indicate that the data loading
    # operation has started.
    progress("Initiating", 0)

    # - Load the data. Each line in the file should represent a review in the list 'reviews_data'.
    # - Use the appropriate functions in the module 'tui' to display a message to indicate how many reviews have
    total_reviews(num_reviews=len(reviews_date)-1)

    # been loaded and that the data loading operation has completed.
    progress("Completed", 100)
    print("\t")
    while True:
        # Task 14: Using the appropriate function in the module 'tui', display the main menu
        # Assign the value returned from calling the function to a suitable local variable

        main_menu_choice = main_menu()

        # Task 15: Check if the user selected the option for processing data.
        if main_menu_choice == '1':
            # If so, then do the following:
            progress("Initiating", 0)  # - Using the appropriate function in the module tui to display a message to
            # indicate that the data processing
            # operation has started.

            # - Process the data (see below).

            # - Use the appropriate function in the module tui to display a message to indicate that the data processing
            # operation has completed.
            progress("Completed", 100)
            # To process the data, do the following:
            # - Use the appropriate function in the module 'tui' to display a sub-menu of options for processing the data
            # (menu variant 1).

            opt_sub_menu = sub_menu(1)
            if opt_sub_menu == '1':
                # - Check what option has been selected
                #   - If the user selected the option to retrieve reviews by hotel name then
                #       - Use the appropriate function in the module 'tui' to indicate that the review retrieval process
                #       has started.
                progress("Initiating", 0)
                # - Use the appropriate function in the module 'process' to retrieve the review and
                #   then appropriately  display it.
                by_name(reviews_date)
                #       - Use the appropriate function in the module 'tui' to indicate that the review retrieval process has
                #       completed.
                progress("Completed", 100)

            # If user selected the option to retrieve reviews by review dates then
            elif opt_sub_menu == '2':
                #  - Use the appropriate function in the module 'tui' to indicate that the reviews retrieval
                #       process has started.
                progress("Initiating", 0)
                #  - Use the appropriate function in the module 'process' to retrieve the reviews
                by_dates(reviews_date)
                #  - Use the appropriate function in the module 'tui' to indicate that the reviews retrieval
                #       process has completed.
                progress("Completed", 100)

            #  - If the user selected the option to group reviews by nationality then
            elif opt_sub_menu == '3':
                #      - Use the appropriate function in the module 'tui' to indicate that the grouping
                #       process has started.
                progress("Initiating", 0)
                #  - Use the appropriate function in the module 'process' to group the reviews
                by_nationality(reviews_date)
                #  - Use the appropriate function in the module 'tui' to display the groupings.

                #  - If required, you may add a suitable function to the module 'tui' to display the groupings
                #  - Use the appropriate function in the module 'tui' to indicate that the grouping
                #  process has completed.
                progress("Completed", 100)

            elif opt_sub_menu == '4':
                #       - Use the appropriate function in the module 'tui' to indicate that the summary
                #       process has started.
                progress("Initiating", 0)
                #       - Use the appropriate function in the module 'process' to summarise the reviews.
                positive_reviews, negative_reviews, user_date = extract_reviews_by_date(reviews_date)
                total_positive_reviews = len(positive_reviews)
                total_negative_reviews = len(negative_reviews)
                average_rating = calculate_average(reviews_date, user_date)
                # Call the summarize_reviews function to display the summary
                print_summary_by_date(total_negative_reviews, total_positive_reviews, average_rating,user_date)

            elif opt_sub_menu == '5':
                progress("Initiating", 0)
                get_hotel_reviews_summary(reviews_date)
                progress("Completed", 100)

            #   - If the user selected the option to summarise the reviews then
            elif opt_sub_menu == '6':
                progress("Initiating", 0)
                positive_reviews, negative_reviews,user_date = extract_reviews_by_date(reviews_date)
                by_date_pos_neg(positive_reviews,negative_reviews,user_date,reviews_date,calculate_average)
                progress("Completed", 100)

            elif opt_sub_menu == '7':
                progress("Initiating", 0)

                find_hotel_reviews()
                progress("Completed", 100)



        # Task 21: Check if the user selected the option for visualising data.
        elif main_menu_choice == '2':
            opt_sub_menu = sub_menu(2)
            if opt_sub_menu == '1':
                # - Use the appropriate function in the module 'tui' to indicate that the data visualisation operation
                # has started.
                progress("Initiating", 0)

                # - Visualise the data by doing the following:
                #   - call the appropriate function in the module 'tui' to determine what visualisation is to be done.
                progress("In progress", 49)
                #   - call the appropriate function in the module 'visual' to display the visual
                positive_negative_pie_chart()
                # - Use the appropriate function in the module 'tui' to display a message to indicate that the
                # data visualisation operation has completed.
                progress("Completed", 100)
            elif opt_sub_menu == '2':

                visualize_reviews_by_nationality(reviews_date)
            elif opt_sub_menu == '3':
                # Call the animation function
                animate_visualization(reviews_date)
                # Show the animation
                plt.show()

    # Task 25: Check if the user selected the option for exporting reviews.  If so, then do the following:
        elif main_menu_choice == '3':

            reviews_to_export = review_dates()  # Use the appropriate function to retrieve the reviews
            exporter = ReviewExporter(reviews_to_export)
            progress("Initiating", 0)
            exporter.export_to_json('reviews.json')  # Export the reviews to JSON file
            progress("\nCompleted", 100)

    # Task 26: Check if the user selected the option for exiting the program.
    # If so, then break out of the loop
        elif main_menu_choice == '4':
            break
    # Task 27: If the user selected an invalid option then use the appropriate function of the
    # module tui to display an error message
        elif main_menu_choice is not [1,2,3,4]:
            print("No such option. Please try again.")


run()