import esgen

if __name__ == '__main__':

    source = {'naam': 'full_name',
              'leeftijd': 'age',
              'adres': {
                  'adres': 'address',
                  'stad': 'city'}
              }

    esgen.create_test_data('myindex', source)
