import datetime
import pytz
import click

from worldtimebuddy.utils import get_major_tz_from_env, callDelta, DeltaValueError
from worldtimebuddy.constants import timezone_codes

MAJOR_TIMEZONES = get_major_tz_from_env() or ['UTC', 'US/Pacific', 'Asia/Kolkata']

@click.command()
@click.option('--format', default='%Y-%m-%d %H:%M:%S', help='DateTime format string')
@click.option('--major', is_flag=True, help='Show only major timezones')
@click.option('--timezone', '-tz', help='Show time for a specific timezone')
@click.option('--list', 'list_timezones', is_flag=True, help='List all available timezones')
@click.option('--delta', help='Time to add (e.g., +2hr, -30min, -1day)')
@click.option('--convert', '-c', help='Convert time from one timezone to another')
def cli(format, major, timezone, list_timezones, delta, convert):
    """
    Display current time for all timezones, major timezones, or a specific timezone.
    """
    if list_timezones:
        for tz in pytz.all_timezones:
            click.echo(tz)
        return

    now = datetime.datetime.now(pytz.utc)
    
    if timezone:
        # Map short timezone code to full name if applicable
        timezone = timezone_codes.get(timezone, timezone)
        
        try:
            tz = pytz.timezone(timezone)
            time = now.astimezone(tz)
            
            if delta:
                try:
                    time = callDelta(time, delta)
                except DeltaValueError as e:
                    click.echo(f"DeltaValueError: {e}")
                    return

            click.echo(f"{timezone:<30} {time.strftime(format)}")
        except pytz.exceptions.UnknownTimeZoneError:
            click.echo(f"Error: Unknown timezone '{timezone}'")
            click.echo("Use 'gettime --list' to see all available timezones")
    elif major:
        for tz in MAJOR_TIMEZONES:
            timezone = pytz.timezone(tz)
            time = now.astimezone(timezone)
            if tz == 'US/Pacific':
                pdt_pst = 'PDT' if time.tzinfo._dst else 'PST'
                click.echo(f"{pdt_pst:<30} {time.strftime(format)}")
            else:
                click.echo(f"{tz:<30} {time.strftime(format)}")
    else:
        for tz in pytz.all_timezones:
            timezone = pytz.timezone(tz)
            time = now.astimezone(timezone)
            click.echo(f"{tz:<30} {time.strftime(format)}")

if __name__ == '__main__':
    cli()