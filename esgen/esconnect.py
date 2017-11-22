import requests


class Index:

    def __init__(self, baseurl, index):
        self._baseurl = baseurl
        self._index = index

        if requests.head(baseurl + '/' + index).status_code == 404:
            response = requests.put(baseurl + '/' + index)
            if not response.ok:
                print('create failed: {} {}'.format(response.status_code,
                                                    response.text))

    def bulk_create(self, doctype, documents):

        for document in documents:
            response = requests.post(self._baseurl + '/' +
                                    self._index + '/' +
                                    doctype,
                                    json=document)
            if not response.ok:
                print('add failed: {} {}'.format(response.status_code,
                                                 response.text))
