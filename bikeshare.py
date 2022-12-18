import time
import pandas as pd
import numpy as np


//comment
CITY_DATA = {'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv'}

def check_input(input_str,input_type):
    """
    check the validity of user input.
    input_str: is the input of the user
    input_type: is the type of input: 1 = city, 2 = month, 3 = day
    """
    while True:
        input_r=input(input_str)
        try:
            if input_r in ['chicago','new york city','washington'] and input_type == 1:
                break
            elif input_r in ['january', 'february', 'march', 'april', 'may', 'june','all'] and input_type == 2:
                break
            elif input_r in ['sunday','monday','tuesday','wednesday','thursday','friday','saturday','all'] and input_type == 3:
                break
            else:
                if input_type == 1:
                    print("Sorry, pleace input: chicago new york city or washington")
                if input_type == 2:
                    print("Sorry, pleace input: january, february, march, april, may, june or all")
                if input_type == 3:
                    print("Sorry, pleace input: sunday, ... friday, saturday or all")
        except ValueError:
            print("Wrong input pleace try again!")
    return input_r



def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = check_input("Would you like to see the data for chicago, new york city or washington?",1)
    # get user input for month (all, january, february, ... , june)
    month = check_input("Which Month (all, january, ... june)?", 2)
    # get user input for day of week (all, monday, tuesday, ... sunday)
    day = check_input("Which day? (all, monday, tuesday, ... sunday)", 3)
    print('-'*40)
    return city, month, day



def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month, day of week, hour from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df



def stats_of_time(df):


    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].mode()[0]
    print('Most Popular Month:', common_month)

    # display the most common day of week
    common_day_of_week = df['day_of_week'].mode()[0]
    print('Most Day Of Week:',  common_day_of_week)

    # display the most common start hour
    common_start_hour = df['hour'].mode()[0]
    print('Most Common Start Hour :', common_start_hour)
    print("\nThis took %s seconds ." % (time.time() - start_time))
    print('-'*40)



def stats_of_station(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_start_station = df['Start Station'].mode()[0]
    print('Most Start Station:', common_start_station)

    # display most commonly used end station
    common_end_station = df['End Station'].mode()[0]
    print('Most End Station:', common_end_station)

    # display most frequent combination of start station and end station trip
    group_field=df.groupby(['Start Station','End Station'])
    common_combination_station = group_field.size().sort_values(ascending=False).head(1)
    print('Most frequent combination of Start Station and End Station trip:\n', common_combination_station)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def trip_duration(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()
    print('Total Travel Time:', total_time)

    # display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('Mean Travel Time:', mean_time)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)



def user_stats(df,city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print('User Type Stats :')
    print(df['User Type'].value_counts())
    if city != 'washington':
        # Display counts of gender
        print('Gender Stats :')
        print(df['Gender'].value_counts())
        # Display earliest, most recent, and most common year of birth
        print('Birth Year Stats :')
        most_recent_year = df['Birth Year'].max()
        print('Most Recent Year :',most_recent_year)
        most_common_year = df['Birth Year'].mode()[0]
        print('Most Common Year :',most_common_year)
        earliest_year = df['Birth Year'].min()
        print('Earliest Year :',earliest_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




    #Function to display the data as per user request
def display_data(df):

    LIST = ['yes', 'no']
    data = ''

    i = 0
    while data not in LIST:
        print("\nDo you wish to view the raw data? Accepted responses:\nYes or yes\nNo or no")
        data = input().lower()

        if data == "yes":
            print(df.head())
        elif data not in LIST:
            print("Input does not seem to match any of the accepted responses.")
            print("\nRestarting...\n")


    while data == 'yes':
        print("Do you wish to view more raw data?")
        i += 5
        data = input().lower()
        if data == "yes":
             print(df[i:i+5])
        elif data != "yes":
             break

    print('-'*80)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_data(df)
        stats_of_time(df)
        stats_of_station(df)
        trip_duration(df)
        user_stats(df,city)

        restart = input('\nDo you want to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
