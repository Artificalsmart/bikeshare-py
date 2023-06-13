import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june','july','august','september','october','november','decamber','all']
days = ['saturday','sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday' ,'all']

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
    while True:
        city=input("select from cities what city you wanna explore (chicago , new york city , washington)")
        if city not in CITY_DATA:
            print('ohhhhhh you input a wrong value')
        else:
            break
    
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month=input('Would you like to filter the data by month which month or not at all?''\n>').casefold()
        if month not in months:
            print("the month not in months")
            continue
        else:
            break
    

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day=input("please enter the(name of day)/ (all)""\n>").casefold()
        if day not in days:
            print("the input is wrong")
            continue
        else:   
            break
        
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
    df =pd.read_csv(CITY_DATA[city])
    df['Start Time']=pd.to_datetime(df['Start Time'])
    df['month']=df['Start Time'].dt.month
    df['day']=df['Start Time'].dt.day
        #filter and get month
    if month !='all':
        month=months.index(month)+1
        #filter all month
        df=df[df['month']==month]
    
        #filter and get day
    if day != 'all':
        day=days.index(day)+1
        
        #filte new dataframe
        df = df[df['day'] == day]
        
    


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['month'].mode()


    # TO DO: display the most common day of week
    df['day'].mode()


    # TO DO: display the most common start hour
    df['Start Time'].mode()


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_start=df['Start Station'].mode()[0]
    print('most_start_station', most_start)


    # TO DO: display most commonly used end station
    most_end=df['End Station'].mode()[0]
    print("most end sation",most_end)

    # TO DO: display most frequent combination of start station and end station trip
    df['most frequant']=df['Start Station'] + df['End Station']
    df['most frequant']


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['Trip Duration'].astype(int)
    total_travel=df['Trip Duration'].sum()
    
    print("total trip duration=",total_travel)


    # TO DO: display mean travel time
    mean_travel=df['Trip Duration'].mean()
    print("mean travel=",mean_travel)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    counts=df['User Type'].value_counts()
    print('count of user type=', counts)
    


    # TO DO: Display counts of gender
    if 'Gender' in df.columns:
        df['Gender'].value_counts()
    else:
        print('ohh no gender in this city')


    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year'in df.columns:
        df['Birth Year'].min()
        df['Birth Year'].max()
        df['Birth Year'].mode()
    else:
        print('this city don\'t have birth year')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
def display_raw(df):
    while True:
        user=input("please enter (head/tail)or(no)to exist\n>").casefold()
        if user=='head':
            print(df.head())
        elif user == 'tail':
             print(df.tail())
        elif user == 'no':
            break
       

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city,month,day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw(df)
        
        

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
     main()