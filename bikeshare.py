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
    # Define lists of accepted inputs cities, months and days
    accepted_cities = ['chicago', 'new york city', 'washington']
    accepted_months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    accepted_days = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    
    # While Loop for whole user input to enable correction of user input  
    while True:
  
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
        while True:
            city = input('\nWould you like to see data for Chicago, New York City or Washington: ').lower()
            if city in accepted_cities:
                break
            else:
                print('\n\nInvalid Input! Please select one of the available cities')
                continue

    # TO DO: get user input for month (all, january, february, ... , june)
        while True:
            month = input('\nWhich month do you want to look at? Type "all" for no month filter. (input: all, january, ... , june): ').lower()
            if month in accepted_months:
                break
            else:
                print('\n\nInvalid Input! Please select a valid month or "all"')
                continue

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
        while True:
            day = input('\nWhat day do you want to look at? Type "all" for no day filter. (input: all, monday, ... sunday): ').lower()
            if day in accepted_days:
                break
            else:
                print('\n\nInvalid Input! Please select a valid day of the week or "all"')
                continue

    # Summarizing user selection
        print('\n\nYour filter selectection is: CITY: {}, MONTH: {}, DAY: {}.\n'.format(city, month, day))

    # Continue with selected user input or restart/correct input
        input_ready = input('To continue with the calculation type "yes" - to restart and change your filter selection type "no": ').lower()

        if input_ready == 'yes':
            break
        else:
            continue


    print('\n' + '-'*40)
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
    
    # convert the End Time column to datetime
    df['End Time'] = pd.to_datetime(df['End Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.dayofweek
    
    
    # creating new column for start hour
    df['start_hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != 'all':
        
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        
        # use the index of the days list to get the corresponding int
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = days.index(day)
        
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]

    ## checking filter results
    # print(df)

    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month (only if no specific month was selected in user input)
    if month == 'all':
        
        popular_month = df['month'].mode()[0]
   
        # convert month number back to name
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        popular_month = months[popular_month-1].title()

        # print result for common month
        print('the most common month is: {}'.format(popular_month))


    # TO DO: display the most common day of week (only if no specific day was selected in user input)
    if day == 'all':
        
        popular_day = df['day_of_week'].mode()[0]
    
        # convert weekday number back to name
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        popular_day = days[popular_day].title()
    
        # print result for common day
        print('the most common day of week is: {}'.format(popular_day))
    
    
    # TO DO: display the most common start hour
    
    popular_start_hour = df['start_hour'].mode()[0]
    print('the most common start hour is: {}'.format(popular_start_hour))

    # Computation time
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    
    # calculating value counts
    vc_start_station = df['Start Station'].value_counts()
    # max value count (idxmax from: #https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.idxmax.html)
    popular_start_station = vc_start_station.idxmax()
    # printing result
    print('the most common start station is: {}'.format(popular_start_station))


    # TO DO: display most commonly used end station
    
    # calculating value counts
    vc_end_station = df['End Station'].value_counts()  
    # max value count (idxmax from: #https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.idxmax.html)
    popular_end_station = vc_end_station.idxmax()
    # printing result
    print('the most common end station is: {}'.format(popular_end_station))


    # TO DO: display most frequent combination of start station and end station trip
    
    # combining start and end station
    df['Station Combination'] = df['Start Station'] + ' --> ' + df['End Station']
    
    # calculating value counts
    vc_station_combination = df['Station Combination'].value_counts()      
    # max value count (idxmax from: #https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.idxmax.html)
    popular_station_combination = vc_station_combination.idxmax()
    # printing result
    print('the most common combination of start and end station is: {}'.format(popular_station_combination))


    # Computation time
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    
    # summarize travel time to get total travel time
    total_travel_time = df['Trip Duration'].sum()
    
    # printing result
    print('the total travel time with the selected filter is: {}'.format(total_travel_time))


    # TO DO: display mean travel time

    # calculating the mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    
    # printing result
    print('the mean travel time is: {}'.format(mean_travel_time))


    # Computation time
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    vc_user_types = df['User Type'].value_counts()   
    print('Counts of user types:')    
    print(vc_user_types)


    # gender and birth year are not available in all datasets 
    # --> checking if gender and birth year are available and calculating gender and birth year information if available

    if 'Gender' in df:
    
        # TO DO: Display counts of gender
        vc_gender = df['Gender'].value_counts()   
        print('\nCounts of gender:') 
        print(vc_gender)


    # TO DO: Display earliest, most recent, and most common year of birth
    
    if 'Birth Year' in df:
    
        # earliest birth year
        earliest_birth_year = df['Birth Year'].min()
        print('\nthe earliest year of birth is: {}'.format(earliest_birth_year))
    
        # most recent birth year
        latest_birth_year = df['Birth Year'].max()
        print('the most recent year of birth is: {}'.format(latest_birth_year))
    
        # common year of birth
        vc_birth_year = df['Birth Year'].value_counts()
        # max value count (idxmax from: #https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.idxmax.html)
        common_birth_year = vc_birth_year.idxmax()
        print('the most common year of birth is: {}'.format(common_birth_year))
    

    # Computation time
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def ind_trip_data(df):
    """
    Asks user if he/she wants to see individual trip data.
    If yes, shows 5 datasets and asks again
    
    """
    
    # count variable for rows in raw data
    head_count = 0
    
    # does user want to see individual trip data?
    while True:
        ind_data = input('\nWould you like to see individual trip data? Type "yes" or "no": ').lower()
        if ind_data == 'yes':
            print('\n\n here comes more trip data\n')
            # printing next 5 rows
            print(df[head_count:head_count+5])
            head_count += 5
            continue
        else:
            print('\n')
            break



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        ind_trip_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
