import csv
from datetime import datetime

DEGREE_SYMBOL = u"\N{DEGREE SIGN}C"


def format_temperature(temp):
    """Takes a temperature and returns it in string format with the degrees
        and Celcius symbols.

    Args:
        temp: A string representing a temperature.
    Returns:
        A string contain the temperature and "degrees Celcius."
    """
    return f"{temp}{DEGREE_SYMBOL}"


def convert_date(iso_string):
    """Converts and ISO formatted date into a human-readable format.

    Args:
        iso_string: An ISO date string.
    Returns:
        A date formatted like: Weekday Date Month Year e.g. Tuesday 06 July 2021
    """
    dt = datetime.fromisoformat(iso_string)
    formatted_date = dt.strftime("%A %d %B %Y")
    return formatted_date
    # pass


def convert_f_to_c(temp_in_fahrenheit):
    """Converts a temperature from Fahrenheit to Celcius.
    Formula: C = (F - 32) * 5 / 9

    Args:
        temp_in_fahrenheit: float representing a temperature.
    Returns:
        A float representing a temperature in degrees Celcius, rounded to 1 decimal place.
    """
    temp_in_celcius = (float(temp_in_fahrenheit) - 32) * 5 / 9
    return round(temp_in_celcius, 1)
    # pass


def calculate_mean(weather_data):
    """Calculates the mean value from a list of numbers.

    Args:
        weather_data: a list of numbers.
    Returns:
        A float representing the mean value.
    """
    sum_value = 0
    count_value = 0
    for value in weather_data:
        sum_value += float(value)
        count_value += 1
    mean_value = sum_value / count_value
    return mean_value   
    # pass


def load_data_from_csv(csv_file):
    """Reads a csv file and stores the data in a list.

    Args:
        csv_file: a string representing the file path to a csv file.
    Returns:
        A list of lists, where each sublist is a (non-empty) line in the csv file.
    """
    list_data = []
    with open(csv_file, newline="") as file:
        csv_reader = csv.reader(file)
        next(csv_reader) #skip headers

        for row in csv_reader:
            if row:
                date = row[0]
                min_temp = int(row[1])
                max_temp = int(row[2])
                list_data.append([date, min_temp, max_temp])
    return list_data
    # pass


def find_min(weather_data):
    """Calculates the minimum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The minimum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    float_weather_data = []
    if weather_data:
        for value in weather_data:
            float_data = float(value)
            float_weather_data.append(float_data)

        min_value = min(float_weather_data)
        for i in range(len(float_weather_data)-1, -1, -1):
            if float_weather_data[i] == min_value:
                return (min_value, i)
    else:
        return ()
    # pass


def find_max(weather_data):
    """Calculates the maximum value in a list of numbers.

    Args:
        weather_data: A list of numbers.
    Returns:
        The maximum value and it's position in the list. (In case of multiple matches, return the index of the *last* example in the list.)
    """
    if not weather_data:
        return ()
    
    float_weather_data = [float(value) for value in weather_data]
    max_value = max(float_weather_data)

    for i in range(len(weather_data)-1, -1, -1):
        if float_weather_data[i] == max_value:
            return(max_value, i)
    # pass


def generate_summary(weather_data):
    """Outputs a summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """
    total_days = len(weather_data)

    if total_days == 0:
        return "No Weather Data Available"

    min_temp_list_c = []
    max_temp_list_c = []
    sum_min = 0
    sum_max = 0

    for daily_weather in weather_data:
        min_temp_c = round((float(daily_weather[1]) - 32) * 5 / 9, 1)  #C = (F - 32) * 5 / 9
        max_temp_c = round((float(daily_weather[2]) - 32) * 5 / 9, 1)  #C = (F - 32) * 5 / 9
        min_temp_list_c.append(min_temp_c)
        max_temp_list_c.append(max_temp_c)

        sum_min += min_temp_c
        sum_max += max_temp_c
    
    lowest_temp = min(min_temp_list_c)
    highest_temp = max(max_temp_list_c)

    avg_low = round(sum_min/total_days, 1)
    avg_high = round(sum_max/total_days, 1)

    index_min_temp = min_temp_list_c[::-1].index(lowest_temp)
    index_max_temp = max_temp_list_c[::-1].index(highest_temp)
    index_min_date = total_days - index_min_temp - 1 # To get the index of sublist in the list of weather_data
    index_max_date = total_days - index_max_temp - 1


    iso_date_min_temp = datetime.fromisoformat(weather_data[index_min_date][0]) 
    iso_date_max_temp = datetime.fromisoformat(weather_data[index_max_date][0])
    formatted_date_min_temp = iso_date_min_temp.strftime("%A %d %B %Y")
    formatted_date_max_temp = iso_date_max_temp.strftime("%A %d %B %Y")

    summary = (
    f"{total_days} Day Overview\n" 
    f"  The lowest temperature will be {lowest_temp}{DEGREE_SYMBOL}, and will occur on {formatted_date_min_temp}.\n"
    f"  The highest temperature will be {highest_temp}{DEGREE_SYMBOL}, and will occur on {formatted_date_max_temp}.\n"
    f"  The average low this week is {avg_low}{DEGREE_SYMBOL}.\n"
    f"  The average high this week is {avg_high}{DEGREE_SYMBOL}.\n"
    )

    return summary      
    # pass

def generate_daily_summary(weather_data):
    """Outputs a daily summary for the given weather data.

    Args:
        weather_data: A list of lists, where each sublist represents a day of weather data.
    Returns:
        A string containing the summary information.
    """  
    
    daily_summary = ""

    if not weather_data:
        return "No Weather Data Available"
    
    for daily_weather in weather_data:
        iso_date = datetime.fromisoformat(daily_weather[0])
        formatted_date = iso_date.strftime("%A %d %B %Y")
        min_temp_f = daily_weather[1]
        min_temp_c = round((min_temp_f - 32) * 5 / 9, 1)
        max_temp_f = daily_weather[2]
        max_temp_c = round((max_temp_f - 32) * 5 / 9, 1)

        result = (
            f"---- {formatted_date} ----\n"
            f"  Minimum Temperature: {min_temp_c}{DEGREE_SYMBOL}\n"
            f"  Maximum Temperature: {max_temp_c}{DEGREE_SYMBOL}\n\n"
            )
        
        daily_summary += result
    
    return daily_summary
    # pass
