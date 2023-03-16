def add_time(start, duration, starting_week_day=''):
  week = [
    'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday',
    'sunday'
  ]

  def get_time_int(time):
    return [int(x) for x in time.split(':')]

  def format_converter(hour, batch=None, format='24-hour'):
    if format == '12-hour':
      if hour < 12: 
        return hour or 12, 'AM'
      else:
        return (hour - 12) or hour, 'PM'
    elif format == '24-hour' and batch:
      return (batch.lower() == 'am' and hour) or hour + 12, ''

  def get_days_later(days=0):
    if days <= 0:
      return ''

    if days == 1:
      return ' (next day)'
    else:
      return f' ({days} days later)'

  time, batch = start.split()
  hour, min = get_time_int(time)
  hour_add, min_add = get_time_int(duration)

  result_hour = 0
  result_min = 0
  result_days = 0
  result_weekday = ''

  result_hour = format_converter(hour, batch)[0] + hour_add
  result_min = min + min_add

  if result_min > 59:
    result_min %= 60
    result_hour += 1

  if result_hour >= 24:
    result_days = result_hour // 24
    result_hour %= 24

  if starting_week_day:
    weekday = week.index(starting_week_day.lower())
    result_weekday = f', {week[(weekday + result_days) % 7].title()}'

  result_hour, result_batch = format_converter(result_hour, None, '12-hour')
  new_time = f"{result_hour}:{str(result_min).rjust(2, '0')} {result_batch}{result_weekday}{get_days_later(result_days)}"

  return new_time