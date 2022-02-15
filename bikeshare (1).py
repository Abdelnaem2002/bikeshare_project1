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
    name_city=input("please choose city_name : chicago, new york city , washington ").lower().strip()
    
    while name_city not in  CITY_DATA:
        print("please try Again its  invaild inputs")
        name_city=input("please choose city_name : chicago, new york city , washington ").lower().strip()

    # TO DO: get user input for month (all, january, february, ... , june)
    month = input("(Please Choose month you wanna : for example january ,february , march, april, : all) ").lower().strip()
    months=["january", "february", "march", "april", "may", "june", "all"]
    
    while month not in months:
          print("please try Again its  invaild inputs")
          month = input("(Please Choose month you wanna : for example january ,february , march, april, : all) ")
          if month in months:
                break
            
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday) 
    day = input(" Please choose day you wannna : like (saturday, sunday , monday, tuesday, wednesday, thursday, friday ) ").lower().strip()
    days=["saturday","sunday","monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]
    
    while day not in days:
        print("please try Again its  invaild inputs")
        day = input(" Please choose day you wannna : like (saturday, sunday , monday, tuesday, wednesday, thursday, friday ) ")
        if day in days:
            break
    
   
            
    print('-'*60)
    return name_city, month, day

                     
def load_data(name_city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
      
    df = pd.read_csv(CITY_DATA[name_city])

    #convert the start time column to datetime
    convert=df['Start Time']= pd.to_datetime(df['Start Time'])
    print(convert)
    

    #extract month and day of week from start time to create a new columns
    df["month"] = df["Start Time"].dt.month
    df["day_of_week"] = df["Start Time"].dt.weekday_name

    #To analyzing it  by month
    if month != "all":
        months = ["january", "february", "march", "april", "may", "june","july","augest", "setember","november","descember"]
        month = months.index(month) + 1

        #filter by month to create the new dataframe
        df = df[df['month'] == month]

        #filter by day
    if day != "all":
        #filter by day to create new dataframe
        df = df[df["day_of_week"] == day.title()]
 
    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('most common month Will Be :', common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('most common day of week Will Be :', common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print('most common hour Will Be :', common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    the_most_common_start = df["Start Station"].mode()[0]
    print(" The Most Commonly used start station will be :", the_most_common_start)

    # TO DO: display most commonly used end station
    the_most_common_end = df['End Station'].mode()[0]
    print('\nMost Commonly used end station:', the_most_common_end)

    # TO DO: display most frequent combination of start station and end station trip make concatenation betwen them.
    most_frequent_combination_of_start_station = (df['Start Station']+ ' : '  + df['End Station']).mode()[0]
    print('The most frequent combination of start station and end station trip  Will Be:' , most_frequent_combination_of_start_station)
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*60)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print( 'total travel time :',total_travel_time )
   
    # TO DO: display mean travel time
    mean_travel_time = df['Trip Duration'].mean()
    print('mean travel time :', mean_travel_time)
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('Counts of User Types Will Be : ', user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender = df['Gender'].value_counts()
        print('Gender Types  Will Be : ', gender)

    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
       earliest_year =df['Birth Year'].min()
       print('Earliest Year Will Be :', earliest_year)

       most_recent = df['Birth Year'].max()
       print('\nMost Recent Year Will Be :', most_recent)

       most_year =df['Birth Year'].mode()
       print('\nMost Common Year Will Be :', most_year)
    
    
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    
    
    
#display raw data according to user answer
def display_data(df):

     view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n').lower()
     start_loc = 0
     while (True):
       print(df.iloc[start_loc:start_loc + 5])
       start_loc += 5
       view_data = input("Do you wish to continue?: ").lower()
       if view_data =='no':
            break

    
def main():
    while True:
        name_city, month, day = get_filters()
        df = load_data(name_city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            print('Your program arrived to End Thanks for your Trip With Us (:')
            break
        


if __name__ == "__main__":
	main()
