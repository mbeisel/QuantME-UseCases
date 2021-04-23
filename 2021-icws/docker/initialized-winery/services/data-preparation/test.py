import asyncio
import json

import requests


async def apply_wu_palmer(url_root, job_id, data_url):
    request_url = url_root + '/api/wu-palmer/' + \
                  str(job_id) + \
                  '?input_data_url=' + data_url
    response = json.loads(requests.request("POST", request_url, headers={}, data={}).text)
    return response['distance_matrix_url']


async def test_data_preparation():
    print('Starting test of data preparation service...')

    url_root = 'http://127.0.0.1:5000'
    data_url = 'https://raw.githubusercontent.com/UST-QuAntiL/QuantME-UseCases/master/2021-icws/data/Subset40.csv'
    job_id = 0

    await apply_wu_palmer(url_root, job_id, data_url)

if __name__ == '__main__':
    asyncio.run(test_data_preparation())
