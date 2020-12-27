from azure.cosmos import exceptions, CosmosClient, PartitionKey
import cats
import creds

# Initialize the Cosmos client
creds = creds.get_creds()

# <create_cosmos_client>
client = CosmosClient(creds["endpoint"], creds["key"])

# Create a database if it doesn't exist already
database_name = 'Animals'
database = client.create_database_if_not_exists(id=database_name)

# Create a container
# Using a good partition key improves the performance of database operations. (Indexing)
container_name = 'Cats'
container = database.create_container_if_not_exists(
    id=container_name,
    partition_key=PartitionKey(path="/type"),
    offer_throughput=400
)

cats_to_create = cats.get_cats()

# Create new items
for cat in cats_to_create:
    container.create_item(body=cat)

# query Items using SQL Syntax
query = "SELECT * FROM c"

items = list(container.query_items(
    query=query,
    enable_cross_partition_query=True
))

request_charge = container.client_connection.last_response_headers['x-ms-request-charge']

for cat in items:
    print(cat)
print("User {0} request units".format(request_charge))
