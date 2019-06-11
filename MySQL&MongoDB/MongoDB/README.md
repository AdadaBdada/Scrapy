# Usage of MongoDB

**Tap the MongoDB Homebrew Tap**
```
brew tap mongodb/brew
```
**Install MongoDB**
```
brew install mongodb-community@4.0
```
**Run MongoDB**
```
mongod --config /usr/local/etc/mongod.conf

brew services start mongodb-community@4.0
```

**Connect and Use MongoDB**
```
mongo
```
Mongo Shell
```
> show dbs
  admin   0.000GB
  config  0.000GB
  local   0.000GB

> use school_db
  switched to db school_db

> db
  school_db

> db.createUser({user:"principal", pwd: "123", roles: ["readWrite","dbAdmin"]});
  Successfully added user: { "user" : "principal", "roles" : [ "readWrite", "dbAdmin" ] }

# collections are similar to tables in MySQL
> db.createCollection('students');
  { "ok" : 1 }

> show collections
  students

> db.students.insert({name: "Mike", age: 23, grade: "A"});
  WriteResult({ "nInserted" : 1 })

> db.students.find();
  { "_id" : ObjectId("5cfed8e49def10c1340b3d16"), "name" : "Mike", "age" : 23, "grade" : "A" }

> db.students.insert([{name: "Michael", age: 40, grade: "B+"},
                      {name: "Josh", age:35, grade: "C-"}]);
                      WriteResult({ "nInserted" : 1 })

> db.students.insert([{name: "Michael", age: 40, grade: "B+"},
...                   {name: "Josh", age:35, grade: "C-"}]);
  BulkWriteResult({
  	"writeErrors" : [ ],
  	"writeConcernErrors" : [ ],
  	"nInserted" : 2,
  	"nUpserted" : 0,
  	"nMatched" : 0,
  	"nModified" : 0,
  	"nRemoved" : 0,
  	"upserted" : [ ]
  })
> db.students.find()
  { "_id" : ObjectId("5cfed8e49def10c1340b3d16"), "name" : "Mike", "age" : 23, "grade" : "A" }
  { "_id" : ObjectId("5cfeda539def10c1340b3d17"), "name" : "Michael", "age" : 40, "grade" : "B+" }
  { "_id" : ObjectId("5cfeda539def10c1340b3d18"), "name" : "Josh", "age" : 35, "grade" : "C-" }

> db.students.find()
  { "_id" : ObjectId("5cfed8e49def10c1340b3d16"), "name" : "Mike", "age" : 23, "grade" : "A" }
  { "_id" : ObjectId("5cfeda539def10c1340b3d17"), "name" : "Michael", "age" : 40, "grade" : "B+" }
  { "_id" : ObjectId("5cfeda539def10c1340b3d18"), "name" : "Josh", "age" : 35, "grade" : "C-" }

> db.students.find().pretty()
  {
  	"_id" : ObjectId("5cfed8e49def10c1340b3d16"),
  	"name" : "Mike",
  	"age" : 23,
  	"grade" : "A"
  }
  {
  	"_id" : ObjectId("5cfeda539def10c1340b3d17"),
  	"name" : "Michael",
  	"age" : 40,
  	"grade" : "B+"
  }
  {
  	"_id" : ObjectId("5cfeda539def10c1340b3d18"),
  	"name" : "Josh",
  	"age" : 35,
  	"grade" : "C-"
  }

# remove the collections
> db.students.remove({})
  WriteResult({ "nRemoved" : 3 })
  # curly parenthesis will remove all the collections

> db.students.find().pretty()

# remove the database or drop the database
> db.dropDatabase()
  { "dropped" : "school_db", "ok" : 1 }

```


# Dependency Download

```
sudo pip install pymongo
```

```setting.py
```

Before

```
# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
# ITEM_PIPELINES = {
#   'books_crawler.pipelines.SomePipeline': 300,
# }
```

After
```
# Configure item pipelines
# See http://scrapy.readthedocs.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   'books_crawler.pipelines.MongoDBpipeline': 300,
}
# will actually go to the pipeline.py and then assign class MongoDBpipeline

MONGODB_SERVER = 'localhost'
MONGODB_PORT = 27017
MONGODB_DB = 'books'
MONGODB_COLLECTION = 'product'
```

```pipelines.py
```

Before

```
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class BooksCrawlerPipeline(object):
    def process_item(self, item, spider):
        return item
```

After

```
from pymongo import MongoClient
from scrapy.conf import settings

class MongoDBPipeline(object):

    def __init__(self):
        connection = MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT'])
        db = connection[settings['MONGODB_DB']]
        self.collection = db[settings['MONGODB_COLLECTION']]

    def process_item(self, item, spider):
        self.collection.insert(dict(item))
        return item
```

```
> mongo
> show dbs
  admin   0.000GB
  books   0.000GB
  config  0.000GB
  local   0.000GB

> use books
  switched to db books

> show collections
  products

  > db.products.find()
    { "_id" : ObjectId("5d001969e2f5bd2350e62441"), "upc" : "a897fe39b1053632", "product_type" : "Books", "price_without_tax" : "£51.77", "price_with_tax" : "£51.77", "tax" : "£0.00", "availability" : "In stock (22 available)", "number_of_reviews" : "0" }
    { "_id" : ObjectId("5d001969e2f5bd2350e62442"), "upc" : "a34ba96d4081e6a4", "product_type" : "Books", "price_without_tax" : "£35.02", "price_with_tax" : "£35.02", "tax" : "£0.00", "availability" : "In stock (19 available)", "number_of_reviews" : "0" }
    { "_id" : ObjectId("5d001969e2f5bd2350e62443"), "upc" : "3b1c02bac2a429e6", "product_type" : "Books", "price_without_tax" : "£52.29", "price_with_tax" : "£52.29", "tax" : "£0.00", "availability" : "In stock (19 available)", "number_of_reviews" : "0" }
    { "_id" : ObjectId("5d001969e2f5bd2350e62444"), "upc" : "feb7cc7701ecf901", "product_type" : "Books", "price_without_tax" : "£23.88", "price_with_tax" : "£23.88", "tax" : "£0.00", "availability" : "In stock (19 available)", "number_of_reviews" : "0" }
    { "_id" : ObjectId("5d001969e2f5bd2350e62445"), "upc" : "e30f54cea9b38190", "product_type" : "Books", "price_without_tax" : "£37.59", "price_with_tax" : "£37.59", "tax" : "£0.00", "availability" : "In stock (19 available)", "number_of_reviews" : "0" }
    { "_id" : ObjectId("5d001969e2f5bd2350e62446"), "upc" : "deda3e61b9514b83", "product_type" : "Books", "price_without_tax" : "£57.25", "price_with_tax" : "£57.25", "tax" : "£0.00", "availability" : "In stock (19 available)", "number_of_reviews" : "0" }
    { "_id" : ObjectId("5d001969e2f5bd2350e62447"), "upc" : "a18a4f574854aced", "product_type" : "Books", "price_without_tax" : "£51.33", "price_with_tax" : "£51.33", "tax" : "£0.00", "availability" : "In stock (19 available)", "number_of_reviews" : "0" }
    { "_id" : ObjectId("5d001969e2f5bd2350e62448"), "upc" : "a22124811bfa8350", "product_type" : "Books", "price_without_tax" : "£45.17", "price_with_tax" : "£45.17", "tax" : "£0.00", "availability" : "In stock (19 available)", "number_of_reviews" : "0" }
    { "_id" : ObjectId("5d001969e2f5bd2350e62449"), "upc" : "ce6396b0f23f6ecc", "product_type" : "Books", "price_without_tax" : "£17.46", "price_with_tax" : "£17.46", "tax" : "£0.00", "availability" : "In stock (19 available)", "number_of_reviews" : "0" }
    { "_id" : ObjectId("5d001969e2f5bd2350e6244a"), "upc" : "30a7f60cd76ca58c", "product_type" : "Books", "price_without_tax" : "£20.66", "price_with_tax" : "£20.66", "tax" : "£0.00", "availability" : "In stock (19 available)", "number_of_reviews" : "0" }
    { "_id" : ObjectId("5d001969e2f5bd2350e6244b"), "upc" : "0312262ecafa5a40", "product_type" : "Books", "price_without_tax" : "£13.99", "price_with_tax" : "£13.99", "tax" : "£0.00", "availability" : "In stock (19 available)", "number_of_reviews" : "0" }
    { "_id" : ObjectId("5d001969e2f5bd2350e6244c"), "upc" : "1dfe412b8ac00530", "product_type" : "Books", "price_without_tax" : "£52.15", "price_with_tax" : "£52.15", "tax" : "£0.00", "availability" : "In stock (19 available)", "number_of_reviews" : "0" }
    { "_id" : ObjectId("5d001969e2f5bd2350e6244d"), "upc" : "e10e1e165dc8be4a", "product_type" : "Books", "price_without_tax" : "£22.60", "price_with_tax" : "£22.60", "tax" : "£0.00", "availability" : "In stock (19 available)", "number_of_reviews" : "0" }
    { "_id" : ObjectId("5d001969e2f5bd2350e6244e"), "upc" : "e72a5dfc7e9267b2", "product_type" : "Books", "price_without_tax" : "£17.93", "price_with_tax" : "£17.93", "tax" : "£0.00", "availability" : "In stock (19 available)", "number_of_reviews" : "0" }
    { "_id" : ObjectId("5d001969e2f5bd2350e6244f"), "upc" : "4165285e1663650f", "product_type" : "Books", "price_without_tax" : "£54.23", "price_with_tax" : "£54.23", "tax" : "£0.00", "availability" : "In stock (20 available)", "number_of_reviews" : "0" }
    { "_id" : ObjectId("5d001969e2f5bd2350e62450"), "upc" : "2597b5a345f45e1b", "product_type" : "Books", "price_without_tax" : "£33.34", "price_with_tax" : "£33.34", "tax" : "£0.00", "availability" : "In stock (19 available)", "number_of_reviews" : "0" }
    { "_id" : ObjectId("5d001969e2f5bd2350e62451"), "upc" : "f77dbf2323deb740", "product_type" : "Books", "price_without_tax" : "£22.65", "price_with_tax" : "£22.65", "tax" : "£0.00", "availability" : "In stock (19 available)", "number_of_reviews" : "0" }
    { "_id" : ObjectId("5d00196ae2f5bd2350e62452"), "upc" : "e00eb4fd7b871a48", "product_type" : "Books", "price_without_tax" : "£47.82", "price_with_tax" : "£47.82", "tax" : "£0.00", "availability" : "In stock (20 available)", "number_of_reviews" : "0" }
    { "_id" : ObjectId("5d00196ae2f5bd2350e62453"), "upc" : "6957f44c3847a760", "product_type" : "Books", "price_without_tax" : "£50.10", "price_with_tax" : "£50.10", "tax" : "£0.00", "availability" : "In stock (20 available)", "number_of_reviews" : "0" }
    { "_id" : ObjectId("5d00196ae2f5bd2350e62454"), "upc" : "90fa61229261140a", "product_type" : "Books", "price_without_tax" : "£53.74", "price_with_tax" : "£53.74", "tax" : "£0.00", "availability" : "In stock (20 available)", "number_of_reviews" : "0" }
    > db.products.find();
    { "_id" : ObjectId("5d001969e2f5bd2350e62441"), "upc" : "a897fe39b1053632", "product_type" : "Books", "price_without_tax" : "£51.77", "price_with_tax" : "£51.77", "tax" : "£0.00", "availability" : "In stock (22 available)", "number_of_reviews" : "0" }
    { "_id" : ObjectId("5d001969e2f5bd2350e62442"), "upc" : "a34ba96d4081e6a4", "product_type" : "Books", "price_without_tax" : "£35.02", "price_with_tax" : "£35.02", "tax" : "£0.00", "availability" : "In stock (19 available)", "number_of_reviews" : "0" }
    { "_id" : ObjectId("5d001969e2f5bd2350e62443"), "upc" : "3b1c02bac2a429e6", "product_type" : "Books", "price_without_tax" : "£52.29", "price_with_tax" : "£52.29", "tax" : "£0.00", "availability" : "In stock (19 available)", "number_of_reviews" : "0" }
    { "_id" : ObjectId("5d001969e2f5bd2350e62444"), "upc" : "feb7cc7701ecf901", "product_type" : "Books", "price_without_tax" : "£23.88", "price_with_tax" : "£23.88", "tax" : "£0.00", "availability" : "In stock (19 available)", "number_of_reviews" : "0" }
    { "_id" : ObjectId("5d001969e2f5bd2350e62445"), "upc" : "e30f54cea9b38190", "product_type" : "Books", "price_without_tax" : "£37.59", "price_with_tax" : "£37.59", "tax" : "£0.00", "availability" : "In stock (19 available)", "number_of_reviews" : "0" }
    { "_id" : ObjectId("5d001969e2f5bd2350e62446"), "upc" : "deda3e61b9514b83", "product_type" : "Books", "price_without_tax" : "£57.25", "price_with_tax" : "£57.25", "tax" : "£0.00", "availability" : "In stock (19 available)", "number_of_reviews" : "0" }
    { "_id" : ObjectId("5d001969e2f5bd2350e62447"), "upc" : "a18a4f574854aced", "product_type" : "Books", "price_without_tax" : "£51.33", "price_with_tax" : "£51.33", "tax" : "£0.00", "availability" : "In stock (19 available)", "number_of_reviews" : "0" }
    { "_id" : ObjectId("5d001969e2f5bd2350e62448"), "upc" : "a22124811bfa8350", "product_type" : "Books", "price_without_tax" : "£45.17", "price_with_tax" : "£45.17", "tax" : "£0.00", "availability" : "In stock (19 available)", "number_of_reviews" : "0" }
    { "_id" : ObjectId("5d001969e2f5bd2350e62449"), "upc" : "ce6396b0f23f6ecc", "product_type" : "Books", "price_without_tax" : "£17.46", "price_with_tax" : "£17.46", "tax" : "£0.00", "availability" : "In stock (19 available)", "number_of_reviews" : "0" }
    { "_id" : ObjectId("5d001969e2f5bd2350e6244a"), "upc" : "30a7f60cd76ca58c", "product_type" : "Books", "price_without_tax" : "£20.66", "price_with_tax" : "£20.66", "tax" : "£0.00", "availability" : "In stock (19 available)", "number_of_reviews" : "0" }
    { "_id" : ObjectId("5d001969e2f5bd2350e6244b"), "upc" : "0312262ecafa5a40", "product_type" : "Books", "price_without_tax" : "£13.99", "price_with_tax" : "£13.99", "tax" : "£0.00", "availability" : "In stock (19 available)", "number_of_reviews" : "0" }
    { "_id" : ObjectId("5d001969e2f5bd2350e6244c"), "upc" : "1dfe412b8ac00530", "product_type" : "Books", "price_without_tax" : "£52.15", "price_with_tax" : "£52.15", "tax" : "£0.00", "availability" : "In stock (19 available)", "number_of_reviews" : "0" }
    { "_id" : ObjectId("5d001969e2f5bd2350e6244d"), "upc" : "e10e1e165dc8be4a", "product_type" : "Books", "price_without_tax" : "£22.60", "price_with_tax" : "£22.60", "tax" : "£0.00", "availability" : "In stock (19 available)", "number_of_reviews" : "0" }
    { "_id" : ObjectId("5d001969e2f5bd2350e6244e"), "upc" : "e72a5dfc7e9267b2", "product_type" : "Books", "price_without_tax" : "£17.93", "price_with_tax" : "£17.93", "tax" : "£0.00", "availability" : "In stock (19 available)", "number_of_reviews" : "0" }
    { "_id" : ObjectId("5d001969e2f5bd2350e6244f"), "upc" : "4165285e1663650f", "product_type" : "Books", "price_without_tax" : "£54.23", "price_with_tax" : "£54.23", "tax" : "£0.00", "availability" : "In stock (20 available)", "number_of_reviews" : "0" }
    { "_id" : ObjectId("5d001969e2f5bd2350e62450"), "upc" : "2597b5a345f45e1b", "product_type" : "Books", "price_without_tax" : "£33.34", "price_with_tax" : "£33.34", "tax" : "£0.00", "availability" : "In stock (19 available)", "number_of_reviews" : "0" }
    { "_id" : ObjectId("5d001969e2f5bd2350e62451"), "upc" : "f77dbf2323deb740", "product_type" : "Books", "price_without_tax" : "£22.65", "price_with_tax" : "£22.65", "tax" : "£0.00", "availability" : "In stock (19 available)", "number_of_reviews" : "0" }
    { "_id" : ObjectId("5d00196ae2f5bd2350e62452"), "upc" : "e00eb4fd7b871a48", "product_type" : "Books", "price_without_tax" : "£47.82", "price_with_tax" : "£47.82", "tax" : "£0.00", "availability" : "In stock (20 available)", "number_of_reviews" : "0" }
    { "_id" : ObjectId("5d00196ae2f5bd2350e62453"), "upc" : "6957f44c3847a760", "product_type" : "Books", "price_without_tax" : "£50.10", "price_with_tax" : "£50.10", "tax" : "£0.00", "availability" : "In stock (20 available)", "number_of_reviews" : "0" }
    { "_id" : ObjectId("5d00196ae2f5bd2350e62454"), "upc" : "90fa61229261140a", "product_type" : "Books", "price_without_tax" : "£53.74", "price_with_tax" : "£53.74", "tax" : "£0.00", "availability" : "In stock (20 available)", "number_of_reviews" : "0" }
    > db.products.find().pretty();
    {
    	"_id" : ObjectId("5d001969e2f5bd2350e62441"),
    	"upc" : "a897fe39b1053632",
    	"product_type" : "Books",
    	"price_without_tax" : "£51.77",
    	"price_with_tax" : "£51.77",
    	"tax" : "£0.00",
    	"availability" : "In stock (22 available)",
    	"number_of_reviews" : "0"
    }
    {
    	"_id" : ObjectId("5d001969e2f5bd2350e62442"),
    	"upc" : "a34ba96d4081e6a4",
    	"product_type" : "Books",
    	"price_without_tax" : "£35.02",
    	"price_with_tax" : "£35.02",
    	"tax" : "£0.00",
    	"availability" : "In stock (19 available)",
    	"number_of_reviews" : "0"
    }
    {
    	"_id" : ObjectId("5d001969e2f5bd2350e62443"),
    	"upc" : "3b1c02bac2a429e6",
    	"product_type" : "Books",
    	"price_without_tax" : "£52.29",
    	"price_with_tax" : "£52.29",
    	"tax" : "£0.00",
    	"availability" : "In stock (19 available)",
    	"number_of_reviews" : "0"
    }
    {
    	"_id" : ObjectId("5d001969e2f5bd2350e62444"),
    	"upc" : "feb7cc7701ecf901",
    	"product_type" : "Books",
    	"price_without_tax" : "£23.88",
    	"price_with_tax" : "£23.88",
    	"tax" : "£0.00",
    	"availability" : "In stock (19 available)",
    	"number_of_reviews" : "0"
    }
    {
    	"_id" : ObjectId("5d001969e2f5bd2350e62445"),
    	"upc" : "e30f54cea9b38190",
    	"product_type" : "Books",
    	"price_without_tax" : "£37.59",
    	"price_with_tax" : "£37.59",
    	"tax" : "£0.00",
    	"availability" : "In stock (19 available)",
    	"number_of_reviews" : "0"
    }
    {
    	"_id" : ObjectId("5d001969e2f5bd2350e62446"),
    	"upc" : "deda3e61b9514b83",
    	"product_type" : "Books",
    	"price_without_tax" : "£57.25",
    	"price_with_tax" : "£57.25",
    	"tax" : "£0.00",
    	"availability" : "In stock (19 available)",
    	"number_of_reviews" : "0"
    }
    {
    	"_id" : ObjectId("5d001969e2f5bd2350e62447"),
    	"upc" : "a18a4f574854aced",
    	"product_type" : "Books",
    	"price_without_tax" : "£51.33",
    	"price_with_tax" : "£51.33",
    	"tax" : "£0.00",
    	"availability" : "In stock (19 available)",
    	"number_of_reviews" : "0"
    }
    {
    	"_id" : ObjectId("5d001969e2f5bd2350e62448"),
    	"upc" : "a22124811bfa8350",
    	"product_type" : "Books",
    	"price_without_tax" : "£45.17",
    	"price_with_tax" : "£45.17",
    	"tax" : "£0.00",
    	"availability" : "In stock (19 available)",
    	"number_of_reviews" : "0"
    }
    {
    	"_id" : ObjectId("5d001969e2f5bd2350e62449"),
    	"upc" : "ce6396b0f23f6ecc",
    	"product_type" : "Books",
    	"price_without_tax" : "£17.46",
    	"price_with_tax" : "£17.46",
    	"tax" : "£0.00",
    	"availability" : "In stock (19 available)",
    	"number_of_reviews" : "0"
    }
    {
    	"_id" : ObjectId("5d001969e2f5bd2350e6244a"),
    	"upc" : "30a7f60cd76ca58c",
    	"product_type" : "Books",
    	"price_without_tax" : "£20.66",
    	"price_with_tax" : "£20.66",
    	"tax" : "£0.00",
    	"availability" : "In stock (19 available)",
    	"number_of_reviews" : "0"
    }
    {
    	"_id" : ObjectId("5d001969e2f5bd2350e6244b"),
    	"upc" : "0312262ecafa5a40",
    	"product_type" : "Books",
    	"price_without_tax" : "£13.99",
    	"price_with_tax" : "£13.99",
    	"tax" : "£0.00",
    	"availability" : "In stock (19 available)",
    	"number_of_reviews" : "0"
    }
    {
    	"_id" : ObjectId("5d001969e2f5bd2350e6244c"),
    	"upc" : "1dfe412b8ac00530",
    	"product_type" : "Books",
    	"price_without_tax" : "£52.15",
    	"price_with_tax" : "£52.15",
    	"tax" : "£0.00",
    	"availability" : "In stock (19 available)",
    	"number_of_reviews" : "0"
    }
    {
    	"_id" : ObjectId("5d001969e2f5bd2350e6244d"),
    	"upc" : "e10e1e165dc8be4a",
    	"product_type" : "Books",
    	"price_without_tax" : "£22.60",
    	"price_with_tax" : "£22.60",
    	"tax" : "£0.00",
    	"availability" : "In stock (19 available)",
    	"number_of_reviews" : "0"
    }
    {
    	"_id" : ObjectId("5d001969e2f5bd2350e6244e"),
    	"upc" : "e72a5dfc7e9267b2",
    	"product_type" : "Books",
    	"price_without_tax" : "£17.93",
    	"price_with_tax" : "£17.93",
    	"tax" : "£0.00",
    	"availability" : "In stock (19 available)",
    	"number_of_reviews" : "0"
    }
    {
    	"_id" : ObjectId("5d001969e2f5bd2350e6244f"),
    	"upc" : "4165285e1663650f",
    	"product_type" : "Books",
    	"price_without_tax" : "£54.23",
    	"price_with_tax" : "£54.23",
    	"tax" : "£0.00",
    	"availability" : "In stock (20 available)",
    	"number_of_reviews" : "0"
    }
    {
    	"_id" : ObjectId("5d001969e2f5bd2350e62450"),
    	"upc" : "2597b5a345f45e1b",
    	"product_type" : "Books",
    	"price_without_tax" : "£33.34",
    	"price_with_tax" : "£33.34",
    	"tax" : "£0.00",
    	"availability" : "In stock (19 available)",
    	"number_of_reviews" : "0"
    }
    {
    	"_id" : ObjectId("5d001969e2f5bd2350e62451"),
    	"upc" : "f77dbf2323deb740",
    	"product_type" : "Books",
    	"price_without_tax" : "£22.65",
    	"price_with_tax" : "£22.65",
    	"tax" : "£0.00",
    	"availability" : "In stock (19 available)",
    	"number_of_reviews" : "0"
    }
    {
    	"_id" : ObjectId("5d00196ae2f5bd2350e62452"),
    	"upc" : "e00eb4fd7b871a48",
    	"product_type" : "Books",
    	"price_without_tax" : "£47.82",
    	"price_with_tax" : "£47.82",
    	"tax" : "£0.00",
    	"availability" : "In stock (20 available)",
    	"number_of_reviews" : "0"
    }
    {
    	"_id" : ObjectId("5d00196ae2f5bd2350e62453"),
    	"upc" : "6957f44c3847a760",
    	"product_type" : "Books",
    	"price_without_tax" : "£50.10",
    	"price_with_tax" : "£50.10",
    	"tax" : "£0.00",
    	"availability" : "In stock (20 available)",
    	"number_of_reviews" : "0"
    }
    {
    	"_id" : ObjectId("5d00196ae2f5bd2350e62454"),
    	"upc" : "90fa61229261140a",
    	"product_type" : "Books",
    	"price_without_tax" : "£53.74",
    	"price_with_tax" : "£53.74",
    	"tax" : "£0.00",
    	"availability" : "In stock (20 available)",
    	"number_of_reviews" : "0"
    }
> exit;


```
