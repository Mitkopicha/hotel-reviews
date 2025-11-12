
import csv
import matplotlib.pyplot as plt  # For creating visualizations
import matplotlib.animation as animation


"""
This module is responsible for visualising the data using Matplotlib.
"""



"""
Task 22 - 24: Write suitable functions to visualise the data as follows:

1- Display a pie chart showing the total number of positive and negative reviews for a specified hotel.
2- Display the number of reviews per the nationality of a reviewer. This should by ordered by the number of reviews, highest first, and should show the top 15 + “Other” nationalities.
3- Display a suitable animated visualisation to show how the number of positive reviews, negative reviews and the average rating change over time.
#use dict from reviewer score!!!!!!
Each function should visualise the data using Matplotlib.
"""

# Define a function to display a pie chart of positive and negative reviews for a specified hotel
def positive_negative_pie_chart():
    # Prompt the user to enter the hotel and date
    hotel_name = input("Enter the hotel name: ")

    # Introduce variables for positive and negative review counts
    positive_reviews = 0
    negative_reviews = 0

    # Read the CSV file and count the number of positive and negative reviews
    with open('hotel_reviews.csv', 'r') as file:
        reader = csv.reader(file)  # Generate the reader
        next(reader)  # Skip the header row
        for row in reader:
            # Extract the hotel name, positive review, and negative review from each row
            # by their indexes
            hotel, positive_review, negative_review =  row[1], row[2], row[3]
            if hotel == hotel_name:
                if positive_review != 'No Positive': # Increment the positive_reviews count if a positive review exists
                    positive_reviews += 1
                if negative_review != 'No Negative': # Increment the negative_reviews count if a negative review exists
                    negative_reviews += 1

    # Create a pie chart
    labels = ['Positive', 'Negative']
    sizes = [positive_reviews, negative_reviews]
    colors = ['#3D9140', '#DC143C']
    plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=60)
    plt.axis('equal')

    # Set the title
    plt.title(f"Positive and Negative Reviews for '{hotel_name}' ")

    # Display the chart
    plt.show()

def visualize_reviews_by_nationality(reviews_date):
    nationality_count = {}



    for row in reviews_date:
        nationality = row[4]

        if nationality in nationality_count:
            nationality_count[nationality] += 1
        else:
            nationality_count[nationality] = 1

# Sort the nationality count dictionary by count in descending order
    sorted_nationalities = sorted(nationality_count.items(), key=lambda x: x[1], reverse=True)

    # Select the top 15 nationalities
    top_nationalities = sorted_nationalities[:15]

    # Extract the nationalities and counts for plotting
    labels = [nationality for nationality, count in top_nationalities]
    counts = [count for nationality, count in top_nationalities]

    # Add "Other" category to account for remaining nationalities
    other_count = sum(count for nationality, count in sorted_nationalities[15:])
    labels.append("Other Nationality's")
    counts.append(other_count)
    # Rearrange the data to move "Other" to the bottom
    other_index = labels.index("Other Nationality's")
    labels.insert(0, labels.pop(other_index))
    counts.insert(0, counts.pop(other_index))

    # Plot the data
    plt.barh(range(len(labels)), counts, align='center')
    plt.yticks(range(len(labels)), labels)
    plt.xlabel('Number of Reviews')
    plt.ylabel('Nationality')
    plt.title('Number of Reviews per Nationality')

    plt.show()





def read_csv(hotel_reviews):
    data = []
    with open(hotel_reviews, 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for row in reader:
            # Select desired columns (index 2, index 3, index 5)
            selected_data = [float(row[2]), float(row[3]), float(row[5])]
            data.append(selected_data)
    return data

def animate_visualization(data):
    # Animation code
    fig, ax = plt.subplots()
    # Creating animation frames and updating plot
    def update(frame):
        ax.clear()
        x = [row[2] for row in data[:frame]]
        y = [row[3] for row in data[:frame]]
        z = [row[5] for row in data[:frame]]
        ax.plot(x, y, z)  # Plot x, y, and z values


    # Create animation
    anim = animation.FuncAnimation(fig, update, frames=720, interval=50)
    plt.show()
