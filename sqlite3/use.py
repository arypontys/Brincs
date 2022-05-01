from dml import db_insert, db_update, db_delete, db_select
from pprint import pprint


#db_insert( 'teste_use1', '8899334422', 'teste_use1@gmail.com')

select = db_select('84982738372', 'phone')
pprint(select)


#db_delete( 'teste_use1', '8899334422', 'teste_use1@gmail.com')