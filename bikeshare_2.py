import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input('Enter the name of a city (chicago, new york city, washington). Note: case-sensitive... ')
    while city not in CITY_DATA.keys():
        print("Invalid entry for city name. Try again... ")
        break
        

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Enter a month from january to june. Note: lowercase sensitive... ")
    while month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
        print("Invalid entry for month. Try a lowercase month name from january through june... ")
        break 
    
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Enter the day you want to show data for. If no specific day is wanted, enter 'all'...")

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['months'] = df['Start Time'].dt.month_name
    df['days'] = df['Start Time'].dt.day_name()
    df = df[df['months'] == month]
    df = df[df['days'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print("The most common month for bike trips is: {}.".format(df['months'].mode()))

    # TO DO: display the most common day of week
    print("The most common day of the week for bike trips is: {}.".format(df['days'].mode()))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("The most common hour of the day for bike trips is: {}.".format(df['hour'].mode()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most popular start station is {}.: ".format(df['Start Station'].mode()))

    # TO DO: display most commonly used end station
    print("The most popular end station is: {}.".format(df['End Station'].mode()))

    # TO DO: display most frequent combination of start station and end station trip
    #The combination variable is a series of combined start and end stations
    combination = df['Start Station'] + df['End Station']
    print("The most frequent combination of start station and end station trip is: {}.".format(combination.mode()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    #time_taken is a series formed of subtraction of end and start times
    df['End Time'] = pd.to_datetime(df['End Time'])
    time_taken = df['End Time'] - df['Start Time']
    print("The sum of time taken for all trips is: {} seconds.".format(time_taken.sum()))

    # TO DO: display mean travel time
    print("The mean time for a trip is: {} seconds.".format(time_taken.mean()))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    print("Following are user type counts:/n {}".format(user_types))

    # TO DO: Display counts of gender
    gender_counts = df['Gender'].value_counts()
    print("Following are gender counts: \n {}".format(gender_counts))

    # TO DO: Display earliest, most recent, and most common year of birth
    birth_year = df['Birth Year']
    print("The most recent year of birth for a user is: {}.".format(birth_year.max()))
    print("The earliest year of birth for a user is: {}".format(birth_year.min()))
    print("The most common year of birth for a user is: {}.".format(birth_year.mode))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
