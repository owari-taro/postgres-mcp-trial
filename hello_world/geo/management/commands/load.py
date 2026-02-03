import djclick as click
import geopandas as gpd
from geo.models import Feature, FeatureMetaData
from django.db import transaction
import numpy as np

@click.command()
@click.argument('filepath', type=click.Path(exists=True))
@click.argument('name')
@click.argument('source')
@click.option("--description","-d",default="",help="Description of the dataset")
@transaction.atomic
def command(filepath:str, name:str,source:str,description:str):
    """Load data from a file."""
    click.echo(f"Loading data from: {filepath}")
    click.echo(f"Name: {name}")
    gdf=gpd.read_file(filepath)
    schema=get_attributes_schema(gdf)
    #gdf.dtypes.apply(lambda x: x.name).to_dict()
    schema.pop("geometry",None)  
    medata=FeatureMetaData.objects.create(
        name=name,
        description=description,
        source=source,
        attributes_schema=schema,
    )  
    tmp=[]
    gdf = gdf.replace({np.nan: None})
    for each in gdf.itertuples():
        geom=each.geometry.wkt
        attributes={k:v for k,v in each._asdict().items() if k!="geometry"}
        feature=Feature(
            geom=geom,
            attributes=attributes,
            metadata=medata
        )    
        tmp.append(feature)
        if len(tmp)>=10000:
            Feature.objects.bulk_create(tmp)
            tmp=[]
    if tmp:
        Feature.objects.bulk_create(tmp)
    # Add your data loading logic here


def get_attributes_schema(gdf: gpd.GeoDataFrame) -> dict:
    '''
    Docstring for get_attributes_schema
    {"key":"column_name_1","type":"data_type_1"}
    
    :param gdf: Description
    :type gdf: gpd.GeoDataFrame
    :return: Description
    :rtype: dict
    '''
    schema = {}
    for column, dtype in gdf.dtypes.items():
        if column == 'geometry':
            continue
        schema[column] = str(dtype)
    
    return schema