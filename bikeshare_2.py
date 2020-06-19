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
    city_selection = input('To view the available bikeshare data, kindly type: \n The letter (a) for Chicago\n The letter (b) for New York City \n The letter (c) for Washigton:\n\n '.lower())
    while city_selection not in {'a', 'b', 'c'}:        
        print("That's invalid input.")
        city_selection = input('To view the available bikeshare data, kindly type: \n The letter (a) for Chicago\n The letter (b) for New York City \n The letter (c) for Washigton:\n '.lower())
        
    if city_selection == 'a':
        city = 'chicago'
    elif city_selection == 'b':
        city = 'new york city'
    elif city_selection == 'c':
        city = 'washington'
        
    # TO DO: get user input for month (all, january, february, ... , june)
    month_selection = input("Kindly enter the name of the month you want to show descriptive statistics for: \n Enter (jan) for January. \n Enter (feb) for February \n Enter (mar) for March \n Enter (ap) for April \n Enter (m) for may \n Enter (jun) for June \n Enter (all) to display data for all months. \n".lower())
    while month_selection not in {'jan', 'feb', 'mar', 'ap', 'm', 'jun', 'all'}:
        print("That's invalid input.")
        month_selection = input("Kindly enter the name of the month you want to show descriptive statistics for: \n Enter (jan) for January. \n Enter (feb) for February \n Enter (mar) for March \n Enter (ap) for April \n Enter (m) for may \n Enter (jun) for June \n Enter (all) to display data for all months. \n".lower())
    #The following if statement is to return the month based on the user input 
    #after checking for errors with the previous while statement.
    if month_selection == 'jan':
        month = 'January'
    elif month_selection == 'feb':
        month = 'February'
    elif month_selection == 'mar':
        month = 'March'
    elif month_selection == 'ap':
        month = 'April'
    elif month_selection =='m':
        month = 'May'
    elif month_selection == 'jun':
        month = 'June'
    elif month_selection == 'all':
        month = 'all'
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_selection = input("Kindly enter the name of the day you want to show descriptive statistics for. \n Enter (sun) for Sunday \n Enter (mon) for Monday \n Enter (tue) for Tuesday \n Enter (wed) for Wednesday \n Enter (thu) for Thursday \n Enter (fri) for Friday \n Enter (sat) for Saturday\n Enter (all) for all days \n".lower())
    while day_selection not in {'all','sun', 'mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'all'}:
        print("That's invalid input")
        day_selection = input("Kindly enter the name of the day you want to show descriptive statistics for. \n Enter (sun) for Sunday \n Enter (mon) for Monday \n Enter (tue) for Tuesday \n Enter (wed) for Wednesday \n Enter (thu) for Thursday \n Enter (fri) for Friday \n Enter (sat) for Saturday \n Enter (all) for all days \n".lower())
    if day_selection == 'sun':
        day = 'Sunday'
    elif day_selection == 'mon':
        day = 'Monday'
    elif day_selection == 'tue':
        day = 'Tuesday'
    elif day_selection == 'wed':
        day = 'Wednesday'
    elif day_selection =='thu':
        day = 'Thursday'
    elif day_selection == 'fri':
        day = 'Friday'
    elif day_selection == 'sat':
        day = 'Saturday'
    elif day_selection == 'all':
        day = 'all'
        
        
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
    # filter by month if applicable
    if month != 'all':
        df = df[df['month'] == month.title()]
    else:
        pass
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    else:
        pass
        
    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    #Set the city, month, and day variables for use inside this function
    #city, month, and day variables will be specified before running this function
    # TO DO: display the most common month
    print("The most common month for bike trips is: {}.".format(df['month'].mode()[0]))

    # TO DO: display the most common day of week
    print("The most common day of the week for all bike trips is: {}.".format(df['day_of_week'].mode()[0]))
    
    #THis series is to extract the most common day for a given month
    if month != 'all':    
        best_day_in_month = df['day_of_week'][df['month'] == month.title()].mode()[0]
    else:
        pass
    
    #This is to display most common day of the week in a certain month
    if day != 'all':
        print("The most common day in {} for bike trips is {}.".format(month.title(), best_day_in_month))
    else:
        pass

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


def user_stats(df, city):
    """Displays statistics on bikeshare users. gender_counts and birth_year 
    must be specified in the global workspace before running this function."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    subscriber_count = user_types[0]
    customer_count = user_types[1]

    print("There are {} subscribers and {} customers in this sample.".format(subscriber_count, customer_count))

    # TO DO: Display counts of gender
    if city in {'chicago', 'new york city'}:
        df_gender = df['Gender']
    
        gender_counts = df_gender.value_counts()
        male_counts = gender_counts[0]
        female_counts = gender_counts[1]
        print("There are {} male users and {} female users.".format(male_counts, female_counts))

    # TO DO: Display earliest, most recent, and most common year of birth
        birth_year = df['Birth Year']
        recent_year = int(birth_year.max())
        earliest_year = int(birth_year.min())
        most_common_year = int(birth_year.mode()[0])
        print("The most recent year of birth for a user is: {}.".format(recent_year))
        print("The earliest year of birth for a user is: {}".format(earliest_year))
        print("The most common year of birth for a user is: {}.".format(most_common_year))
    else:
        pass
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
def raw_input_wanted():
    input_selection = input("If you want to show (more) raw data,\n Enter (y) for (yes). \n Enter (n) for n for (No): \n")
    while input_selection not in {'y', 'n'}:
        print("That's invalid input.")
        input_selection = input("If you want to show data, enter (y) for (yes). \n Enter (n) for (No): \n")
    return input_selection

def print_raw_data(df, input_selection, start = 0):
    while input_selection == 'y':
        stop = start + 5
        print(df.iloc[start: stop])
        start += 5
        input_selection = raw_input_wanted()



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
#I encountered an error while executing the following line so I moved it to the global workspace.

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        input_selection = raw_input_wanted()
        print_raw_data(df, input_selection)
        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            start = 0
            break


if __name__ == "__main__":
	main()
    
    
