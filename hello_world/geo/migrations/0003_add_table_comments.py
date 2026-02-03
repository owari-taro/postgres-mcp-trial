# Generated migration for adding table comments

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("geo", "0002_featuremetadata_source"),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
                COMMENT ON TABLE geo_featuremetadata IS 'Metadata for geographic features including schema and source information';
                COMMENT ON COLUMN geo_featuremetadata.name IS 'Name of the feature type';
                COMMENT ON COLUMN geo_featuremetadata.description IS 'Detailed description of the feature';
                COMMENT ON COLUMN geo_featuremetadata.attributes_schema IS 'JSON schema defining the structure of feature attributes';
                COMMENT ON COLUMN geo_featuremetadata.source IS 'Source or origin of the feature data';
            """,
            reverse_sql="""
                COMMENT ON TABLE geo_featuremetadata IS NULL;
                COMMENT ON COLUMN geo_featuremetadata.name IS NULL;
                COMMENT ON COLUMN geo_featuremetadata.description IS NULL;
                COMMENT ON COLUMN geo_featuremetadata.attributes_schema IS NULL;
                COMMENT ON COLUMN geo_featuremetadata.source IS NULL;
            """
        ),
        migrations.RunSQL(
            sql="""
                COMMENT ON TABLE geo_feature IS 'Geographic features with geometry and associated attributes';
                COMMENT ON COLUMN geo_feature.geom IS 'Geometry data for the feature (Point, LineString, Polygon, etc.)';
                COMMENT ON COLUMN geo_feature.attributes IS 'JSON object containing feature-specific attributes';
                COMMENT ON COLUMN geo_feature.metadata_id IS 'Foreign key reference to feature metadata';
            """,
            reverse_sql="""
                COMMENT ON TABLE geo_feature IS NULL;
                COMMENT ON COLUMN geo_feature.geom IS NULL;
                COMMENT ON COLUMN geo_feature.attributes IS NULL;
                COMMENT ON COLUMN geo_feature.metadata_id IS NULL;
            """
        ),
    ]
