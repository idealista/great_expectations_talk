import great_expectations as gx
from os import path
import click

@click.command()
@click.option('--checkpoint', required=True, help='Checkpoint')
@click.option('--datasource', required=True, help='Datasource')
@click.option('--asset', required=True, help='Asset')
@click.option('--month', required=False, help='Month to test against' )
@click.option('--year', required=False, help='Year to test against')
def run(checkpoint, datasource, asset, month, year):
    context = gx.get_context(context_root_dir=path.join(path.dirname(__file__), 'great_expectations'))
    
    table_asset = context.get_datasource(datasource).get_asset(asset)
    
    options = {}
    if year:
        options['year'] = int(year)
    if month:
        options['month'] = int(month)
        
    
    batch_request = table_asset.build_batch_request(options)

    checkpoint = context.get_checkpoint(checkpoint)
    checkpoint.run(batch_request=batch_request)

