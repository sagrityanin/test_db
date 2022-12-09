CREATE TABLE station_rel_d (
        id UInt8,
        id_base1 UInt8,
        id_base2 UInt8,
        station_id1 UInt8,
        station_id2 UInt8,
        distance UInt8,
        node UInt8,
        deleted UInt8,
        verify UInt8,
        user_id UInt8,
        date_update DateTime
) engine = MySQL('127.0.0.1:3306', 'vtk', 'station_rel_d', 'root', '123qwe', replace_query, 'on_duplicate_clause')
