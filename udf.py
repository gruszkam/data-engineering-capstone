from pyspark.sql.functions import udf
from pyspark.sql.types import StringType, DateType

from datetime import datetime, timedelta
from label_mappings import travel, visa, country, port


# UDFs - USER DEFINED FUNCTIONS
# Create udf to return the mode of travel
travel_udf = udf(lambda x: travel[x], StringType())

# Create udf to return visa code
visa_udf = udf(lambda x: visa[x], StringType())

# Create udf to return country name
country_udf = udf(lambda x: country[x], StringType())

# Create udf to return port name
port_udf = udf(lambda x: port[x], StringType())


# Create udf converting sas dates
def convert_sasdate(x):
    try:
        start = datetime(1960, 1, 1)
        return start + timedelta(days=int(x))
    except:
        return None


udf_sasdate = udf(lambda x: convert_sasdate(x), DateType())

# Create udf converting string dates
def convert_stringdate(x):
    try:
        parsed_str = datetime.strptime(x, '%m%d%Y')
        return parsed_str.date()
    except:
        return None


udf_strdate = udf(lambda x: convert_stringdate(x), DateType())
