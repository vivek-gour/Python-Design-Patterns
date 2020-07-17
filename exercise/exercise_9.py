import argparse

def myParser():
    parser = argparse.ArgumentParser(description='Generating DAG for airflow')

    parser.add_argument('-w', '--workflowdir', dest='workflowdir', required=True, help='Workflow Directory')
    parser.add_argument('-p', '--workflowprefix', dest='workflowprefix', required=True, help='prefix for workflow files')
    parser.add_argument('-d', '--datoutputdir', dest='dagoutputdir', required=True,
                        help='Direcotry where generated workflows to be written')
    parser.add_argument('-s', '--s3codedir', dest='s3codedir', required=True, help='code directory in s3')
    parser.add_argument('-o', '--owner', dest='owner', required=True, help='owner of the workflow')
    parser.add_argument('-a', '--audit', dest='audit', required=False, help='Enable audit framework')
    parser.add_argument('-de', '--delimiter', dest='delimiter', required=False, help='Specify the delimiter')
    parser.add_argument('-fb', '--file_lookup_bucket_name', dest='file_lookup_bucket_name', required=True,
                        help='Specify the file_lookup bucket name here')

    args = parser.parse_args()

    file_lookup_bucket_name = args.file_lookup_bucket_name


myParser()