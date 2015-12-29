import click

from shub.utils import get_job


HELP = """
Given a job ID, fetch requests made for that job from Scrapy Cloud and output
them as JSON lines.

A job ID consists of the Scrapinghub project ID, the numerical spider ID, and
the job ID, separated by forward slashes, e.g.:

    shub requests 12345/2/15

You can omit the project ID if you have a default target defined in your
scrapinghub.yml:

    shub requests 2/15

Or use any target defined in your scrapinghub.yml:

    shub requests production/2/15
"""


SHORT_HELP = "Fetch requests from Scrapy Cloud"


@click.command(help=HELP, short_help=SHORT_HELP)
@click.argument('job_id')
def cli(job_id):
    job = get_job(job_id)
    for item in job.requests.iter_json():
        click.echo(item)