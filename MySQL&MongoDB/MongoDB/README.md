# Usage

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
