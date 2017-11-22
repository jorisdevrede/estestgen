from .esconnect import Index
from .gen import generate


def create_test_data(index, schema,
                     base_url='http://127.0.0.1:9200',
                     doc_type='document',
                     iterations=5):

    es_idx = Index(base_url, index)

    es_idx.bulk_create(doc_type, generate(schema, 'nl', iterations))
