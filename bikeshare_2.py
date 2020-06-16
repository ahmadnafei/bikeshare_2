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
        city = input('Enter the name of a city (chicago, new york city, washington). Note: case-sensitive... ')
            
        

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Enter a month from january to june. Note: lowercase sensitive... ")
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    while (month not in months) and month != all:
        print("Invalid entry for month. Try a lowercase month name from january through june... ")
        month =  input("Enter a month from january to june. Otherwise, choose all months by entering 'all'. Note: lowercase sensitive... ")
    
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    day = input("Enter the day you want to show data for in lowercase. If no specific day is wanted, enter 'all'...")
    while day not in days:
        print("Invalid entry for a day. Try again.")
        #day = input("Enter the day you want to show data for in lowercase. If no specific day is wanted, enter 'all'...")
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
    #and convert the Start Time column to datetime
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month_name()
    df['day_of_week'] = df['Start Time'].dt.day_name()
    #get filters from user input using the get_filters() function
    city, month, day = get_filters()
    # filter by month if applicable
    if month != 'all':
        df = df[df['month'] == month.title()]  
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
        
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    #Set the city, month, and day variables for use inside this function
    city, month, day = get_filters()
    # TO DO: display the most common month
    print("The most common month for bike trips is: {}.".format(df['month'].mode()[0]))

    # TO DO: display the most common day of week
    print("The most common day of the week for all bike trips is: {}.".format(df['day_of_week'].mode()[0]))
    
    #THis series is to extract the most common day for a given month
    best_day_in_month = df['day_of_week'][df['month'] == month.title()].mode()[0]
    
    #This is to display most common day of the week in a certain month
    print("The most common day in {} for bike trips is {}.".format(month.title(), best_day_in_month))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print("The most common hour of the day for bike trips is: {}.".format(df['hour'].mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print("The most popular start station is {}. ".format(df['Start Station'].mode()[0]))

    # TO DO: display most commonly used end station
    print("The most popular end station is: {}.".format(df['End Station'].mode()[0]))

    # TO DO: display most frequent combination of start station and end station trip
    #The combination variable is a series of combined start and end stations
    combination = df['Start Station'] + df['End Station']
    print("The most frequent combination of start station and end station trip is: {}.".format(combination.mode()[0]))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    #time_taken is a series formed of subtraction of end and start times
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    #We make a series of the time taken (difference between start and end times)
    time_taken = df['End Time'] - df['Start Time']
    print("The sum of time taken for all trips is: {} days.".format(time_taken.sum()))

    # TO DO: display mean travel time
    #First, we calculate the mean, then convert it into seconds for more clarity
    
    mean_in_seconds = time_taken.mean().total_seconds()
    print("The mean time for a trip is: {} seconds.".format(mean_in_seconds))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()

    print("Following are user type counts:\n {}".format(user_types))

    # TO DO: Display counts of gender
    gender_counts = df['Gender'].value_counts()
    print("Following are gender counts: \n {}".format(gender_counts))

    # TO DO: Display earliest, most recent, and most common year of birth
    birth_year = df['Birth Year']
    print("The most recent year of birth for a user is: {}.".format(birth_year.max()))
    print("The earliest year of birth for a user is: {}".format(birth_year.min()))
    print("The most common year of birth for a user is: {}.".format(birth_year.mode()[0]))
    
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
    
    
