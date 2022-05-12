import apache_beam as beam
from apache_beam.options.pipeline_options import PipelineOptions
import logging
import re
import argparse


class convertToDict:

    def parse_method (self, element):
        values = re.split('\t', element)

        row = dict(
            zip(('AffiliationId',
'Rank',
'NormalizedName',
'DisplayName',
'GridId',
'RorId',
'OfficialPage',
'WikiPage',
'PaperCount',
'PaperFamilyCount',
'CitationCount',
'Iso3166Code',
'Latitude',
'Longitude',
'CreatedDate',
'UpdatedDate',
),values))
        return row


def run():
        parser = argparse.ArgumentParser()
        # parser.add_argument('--my-arg', help='description')
        args, beam_args = parser.parse_known_args()
        # Read from GCS and write to BQ Table
        data_ingestion = convertToDict()
        # Args:
        #     input file uri
        #     output table id (dataset_id.table_id)
        input_file_path='gs://open-alex-main/Affiliations.txt'
        bq_table_id='open_alex.affiliations'
        schema='AffiliationId:BIGNUMERIC,Rank:INTEGER,NormalizedName:STRING,DisplayName:STRING,GridId:STRING,RorId:STRING,OfficialPage:STRING,WikiPage:STRING,PaperCount:BIGNUMERIC,PaperFamilyCount:BIGNUMERIC,CitationCount:BIGNUMERIC,Iso3166Code:STRING,Latitude:FLOAT,Longitude:FLOAT,CreatedDate:STRING,UpdatedDate:TIMESTAMP'

        beam_options = PipelineOptions(
            beam_args,
            runner='DataflowRunner',
            project='springer-nature-analytics',
            job_name='oa-affiliations-beam',
            temp_location='gs://open-alex/templates',
            region='us-central1')



        p = beam.Pipeline(options=beam_options)

        (p | 'Read from a File' >> beam.io.ReadFromText(input_file_path, skip_header_lines=1)
         | 'String To BigQuery Row' >> beam.Map(lambda s: data_ingestion.parse_method(s)) |
         'Write to BigQuery' >> beam.io.Write(
                    beam.io.BigQuerySink(bq_table_id,
        schema=schema,                create_disposition=beam.io.BigQueryDisposition.CREATE_IF_NEEDED,
                        write_disposition=beam.io.BigQueryDisposition.WRITE_TRUNCATE)))
        p.run().wait_until_finish()
        
if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    run()