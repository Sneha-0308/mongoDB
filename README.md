# mongoDB
***MongoDB commands for database***
- use DBname: Create new or switch database
- show dbs: View all database
- db: View current database
- db.dropDatabase(): Delete database</br>
 

***MongoDB commands for collection***
- db.createCollection('collection_name'): create collection
- show collections: to view collections
- db.collection_name.drop(): to delete collection</br>


***MongoDB commands for document***
- db.collection_name.insert({
                           'field': value,
                           'field': value
                           })
  : to insert 1 document in collection
- db.collection_name.insert([{
                           'field': value,
                           'field': value
                           },
                           {
                           'field': value,
                           'field': value
                           },
                           {
                           'field': value,
                           'field': value
                           }])
  : to insert many documents in collection
- db.collection_name.find(): to show the documents in the collection
- db.collection_name.find().pretty(): to show the documents in the collection (Prettified)
- db.collection_name.find({field: value}): to search details of field
- db.collection_name.find().pretty().limit(no_of _doument): it shows only mentioned number of documents
- db.collection_name.find().count(): total number of documents
- db.collection_name.fin({field: value}).count(): total number of document which contain mentioned field and value
- db.collection_name.find().sort({field: 1 or -1}).pretty(): use to sort 
    -   field must be a number 
    -   1 used for ascending order
    -   -1 used for descending order
- db.collection_name.findone({field: value}): finds only one document
- db.collection_name.update({field: value},
                            {
                           'field': updated_value,
                           'field': updated_value}): used to update field of documents in collection
- db.collection_name.update({field: value},
                            {
                           'field': updated_value,
                           'field': updated_value},
                           {upsert: true}): used to update field of documents in collection when mentioned document is not present in collecion we use upsert: true
- db.collection_name.update({field: value},
                             {$inc: 
                             {field: 2}}): used to increment the values
   - first field is used to search
   - second filed is used to increment the value that filed must be number
- db.collection_name.update({filed: value},
                              {$rename:
                              {field: 'rename_filed'}}): renames the field based on mentioned field
- db.collection_name.remove({filed: value}): remove the related filed documents
- db.collection_name.find({field:
                           {$lt: value}}): shows the documents which is less than equal to mentioned value
- db.collection_name.find({field:
                           {$gt: value}}): shows the documents which is greater than equal to mentioned value
                           
