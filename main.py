# from ibm_db import connect, connection

# connStr = connect(
#     "DATABASE=alphacom;HOSTNAME=104.155.133.208;PORT=50000;CurrentSchema=PTTGSP;PROTOCOL=TCPIP;UID=db2inst1;PWD=password;", "", "")
# conn = connection(connStr)

# print('start !!')

# if conn:
#     print("Connected !!!")
#     cur = conn.cursor()
#     cur.execute('select * from SENSOR')
#     row = cur.fetchall()
#     print(row)
# else:
#     print("Cant connect to db !@")

# # import ibm_db
# # conn = ibm_db.connect("database","username","password")
# # sql = "SELECT EMPNO, LASTNAME FROM EMPLOYEE WHERE EMPNO > ? AND EMPNO < ?"
# # stmt = ibm_db.prepare(conn, sql)
# # max = 50
# # min = 0
# # # Explicitly bind parameters
# # ibm_db.bind_param(stmt, 1, min)
# # ibm_db.bind_param(stmt, 2, max)
# # ibm_db.execute(stmt)
# # # Process results

# # # Invoke prepared statement again using dynamically bound parameters
# # param = max, min,
# # ibm_db.execute(stmt, param)

import ibm_db
ibm_conn = ibm_db.connect(
    "DATABASE=alphacom;HOSTNAME=104.155.133.208;PORT=50000;CurrentSchema=PTTGSP;PROTOCOL=TCPIP;UID=db2inst1;PWD=password;", "", "")

if ibm_conn:
    stmt_select = ibm_db.exec_immediate(ibm_conn, "SELECT * FROM SENSOR")
    row = ibm_db.fetch_assoc(stmt_select)
    list_calibrate = []
    list_sensor = []
    list_missing = []
    while row != False:
        if str(row['INTEGRATED_TAG']) == 'CALCULATED' :
            list_calibrate.append(row)
        elif row['INTEGRATED_TAG'] != None:
            list_sensor.append(row['INTEGRATED_TAG'])
        else:
            list_missing.append(row)
        row = ibm_db.fetch_assoc(stmt_select)

# print(len(list_calibrate))
# print(list_calibrate)
# print(len(list_sensor))
print(list_sensor)
# print(len(list_missing))