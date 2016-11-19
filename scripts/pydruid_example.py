from pydruid.client import *
from pydruid.utils.aggregators import doublesum

query = PyDruid("http://localhost:32769", 'druid/v2')

ts = query.topn(
    datasource='demo',
    granularity='all',
    intervals='2016-10-02/p10w',
    aggregations={'value': doublesum('value')},
    dimension='gdp',
    metric='value',
    threshold=10
)
print(ts.result_json)
