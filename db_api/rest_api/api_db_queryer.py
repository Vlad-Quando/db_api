import psycopg2


# Database connection for REST API
connection = None


def set_connection() -> None:
    '''Starts the database connection for rest api'''
    global connection
    
    pg_connection_dict = {
        'dbname': 'postgres',
        'user': 'postgres',
        'password': '123321',
        'port': '5432',
        'host': 'localhost'
    }

    connection = psycopg2.connect(**pg_connection_dict)


def get_quantity() -> dict|str:
    '''Queries the database and returnes an amount of records in the table'''
    global connection

    if connection is not None:
        with connection.cursor() as cursor:
            cursor.execute('SELECT COUNT(*) FROM public.viantec_table')
            result = cursor.fetchone()
            
            return result
        
    else:
        return 'DB connection error'
    

def get_record_by_id(id: int) -> dict|str:
    '''Queries the database and returns a record with specified id, else record-not-found error'''
    global connection

    if connection is not None:
        with connection.cursor() as cursor:
            try:
                cursor.execute('SELECT id, firstname, lastname FROM public.viantec_table WHERE id = %s', (id,))
                result = cursor.fetchall()

                if result:
                    return {'Record': result}
                else:
                    return {'Result': 'Error', 'Code': '404', 'Content': 'Record not found'}
                
            except Exception as e:
                print("DB query exceprion:", e)

    else:
        return 'DB connection error'