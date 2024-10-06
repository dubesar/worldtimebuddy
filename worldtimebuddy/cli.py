import datetime
import pytz
import click

MAJOR_TIMEZONES = ['UTC', 'US/Pacific', 'Asia/Kolkata']

@click.command()
@click.option('--format', default='%Y-%m-%d %H:%M:%S', help='DateTime format string')
@click.option('--major', is_flag=True, help='Show only major timezones')
@click.option('--timezone', '-tz', help='Show time for a specific timezone')
@click.option('--list', 'list_timezones', is_flag=True, help='List all available timezones')
def cli(format, major, timezone, list_timezones):
    """
    Display current time for all timezones, major timezones, or a specific timezone.
    """
    if list_timezones:
        for tz in pytz.all_timezones:
            click.echo(tz)
        return

    now = datetime.datetime.now(pytz.utc)
    
    if timezone:
        try:
            tz = pytz.timezone(timezone)
            time = now.astimezone(tz)
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