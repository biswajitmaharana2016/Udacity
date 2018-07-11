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
    city = input("Would you like to have city in between chicago,new york city,washington: ")
    cities=['chicago','new york city','washington']
    city = city.lower()
    try:
        for key in cities:
            if city == key:
                city = key
                break
    except Exception as e:
        print("Error:".format(e))
    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("Would you like to have month in between january,february,...,june: ")
    months=['january', 'february', 'march', 'april', 'may', 'june']
    month = month.lower()
    #print(month)
    try:
        for key in months:
            if month == key:
                month=key
                break
            elif 'all' == key:
                print("plrase provide the proper input")
    except Exception as e:
        print("Error:".format(e))


    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Would you like to provide the day of week: ")
    days=['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
    day = day.lower()
    try:
        for d in days:
            if day == d:
                day=d
                break
            elif d == 'all':
                print("plrase provide the proper input")
     
    except Exception as e:
            print("Error:".format(e))
        
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
    print(CITY_DATA[city])
    df =pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] =df['Start Time'].dt.weekday_name
    # filter by month if applicable
    try :
            if month != 'all':
                # use the index of the months list to get the corresponding int
                months = ['january', 'february', 'march', 'april', 'may', 'june']
                month =months.index(month) + 1
                #print(df[df['month'] == month])
                # filter by month to create the new dataframe
                df =df[df['month'] == month]
    except Exception as e:
                print("Error:".format(e))
        # filter by day of week if applicable
    try:    
            if day != 'all':
                # filter by day of week to create the new dataframe
                #print(df[ df['day_of_week'] ==  day.title()])
                df =df[ df['day_of_week'] ==  day.title()]
    except Exception as e:
            print("Error:".format(e))

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    try:
        # TO DO: display the most common month
        print(df['Start Time'].dt.month.mode()[0])
        #print(df['Start Time'].dt.month.value_counts())
        # TO DO: display the most common day of week
        print(df['Start Time'].dt.weekday_name.mode()[0])
        #print(df['Start Time'].dt.weekday_name.value_counts())
        # TO DO: display the most common start hour
        print(df['Start Time'].dt.hour.mode()[0])
        #print(df['Start Time'].dt.hour.value_counts())
    except  Exception as e:
        print("Error :".format(e))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print(df['Start Station'].mode()[0])

    # TO DO: display most commonly used end station
    print(df['End Station'].mode()[0])

    # TO DO: display most frequent combination of start station and end station trip
    print(df[['Start Station','End Station']].mode())
    #print(df[['Start Station', 'End Station']].apply(lambda x: ''.join(x), axis=1))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print(df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print(df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()
    try:
        # TO DO: Display counts of user types
        print(df['User Type'].value_counts())
    except Exception as e:
        print("Error:".format(e))
    # TO DO: Display counts of gender
    try:
        print(df['Gender'].value_counts())
    except Exception as e:
        print("Error:".format(e))

    # TO DO: Display earliest, most recent, and most common year of birth
    
    #print(df['Birth Year'])
    try:
        print(df['Birth Year'].max())
        print(df['Birth Year'].min())
        print(df['Birth Year'].mode()[0])
    except Exception as e:
        print("Error:".format(e))
    #print(df.sort(['Birth Year'],ascending=0).head(1))   
    #print(df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        print(city,month,day)
        df = load_data(city, month, day)
        time_stats(df)
        print(df.head(2))
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
