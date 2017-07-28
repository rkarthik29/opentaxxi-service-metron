#! /usr/bin/env python

from cabby import create_client

try:
    # create a connection
    client = create_client(host='localhost', port='9898', discovery_path='/services/discovery')

    # iterate through each defined collection
    collections = client.get_collections(uri='http://localhost:9898/services/collection')

    for collection in collections:
        # how many records in each collection?
        count = client.get_content_count(collection_name=collection.name, uri='http://localhost:9898/services/poll')
        print "%-50s %-10d" % (collection.name, count.count)
except:
    print "Services not defined"
