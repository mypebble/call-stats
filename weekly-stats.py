from asternic_email import CallStats
import local_settings
import optparse
import arrow

last_week = arrow.get().replace(days=-7).format('YYYY-MM-DD')
help_txt = (
    "Date inside of the week you wish to create a"
    " report for. For example for last week use {}").format(last_week)

parser = optparse.OptionParser()
parser.add_option(
    '-s', dest='start_of_week', default=arrow.get().format('YYYY-MM-DD'),
    nargs=1, help=help_txt)

opts, remainder = parser.parse_args()

stats = CallStats(local_settings.EXTENSIONS)

stats.set_week(opts.start_of_week)

stats.connect_smtp(
    local_settings.SMTP_SERVER,
    local_settings.SMTP_USER,
    local_settings.SMTP_PASSWORD)
stats.fetch_stats()

print stats.stats

stats.generate_emails('Your weekly call stats are as follows:')

print ">>> DONE!"
