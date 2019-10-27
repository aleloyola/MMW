import mysql.connector


class MySQLController:
    def __init__(self):
        pass

    # instance method
    def insertaventa(self, server, username, password, db, info_venta):
        cnx = mysql.connector.connect(
            host=server,
            user=username,
            passwd=password,
            database=db)

        cursor = cnx.cursor()
        add_venta = ('INSERT INTO sell_in '
                     '(soc,sales_org,distri_channel,channel_descr,sector,sector_descr,request_code,payment_resp_code,payment_resp_descr,payment_condition,payment_condition_descr,center,center_descr,invoice_class,invoice_number,invoice_class_descr,legal_invoice_number,invoice_creation_date,invoice_issue_date,SKU, SKU_descr,sale_unit,incoterms,incoterms_descr,incoterms2,state,sale_office,sale_office_descr,sales_force_group,sales_force_group_descr,SKU_type,SKU_type_descr,article_group,article_group_descr,classification_lvl_1,classification_lvl_2,classification_lvl_3,classification_lvl_4,classification_lvl_5,classification_lvl_6,classification_lvl_7,product_line_mkt,sale_zone,sale_zone_descr,division,division_descr,year,month,sale_qty,volume,cost,price_list,discount_automatic,discount_manual,transport_total,price_net,tax)'
                     # ) "
                     'VALUES (%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s,%s, %s, %s, %s,%s, %s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s, %s, %s,%s, %s, %s,%s, %s, %s,%s, %s, %s, %s, %s)')
        #)")

        for venta in info_venta:
            data_venta = (
            venta['soc'], venta['sales_org'], venta['distri_channel'], venta['channel_descr'], venta['sector'],
            venta['sector_descr'], venta['request_code'], venta['payment_resp_code'], venta['payment_resp_descr'],
            venta['payment_condition'], venta['paymento_condition_descr'], venta['center'], venta['center_descr'],
            venta['invoice_class'], venta['invoice_number'], venta['invoice_class_descr'], venta['legal_invoice_number']
            , venta['invoice_creation_date'], venta['invoice_issue_date'], venta['SKU'],
            venta['SKU_descr'], venta['sale_unit'], venta['incoterms'], venta['incoterms_descr'], venta['incoterms2'],
            venta['state'], venta['sale_office'], venta['sale_office_descr'], venta['sales_force_group'],
            venta['sales_force_group_desc'], venta['SKU_type'], venta['SKU_type_descr'], venta['article_group'],
            venta['article_group_descr'], venta['classification_lvl_1'], venta['classification_lvl_2'],
            venta['classification_lvl_3'], venta['classification_lvl_4'], venta['classification_lvl_5'],
            venta['classification_lvl_6'], venta['classification_lvl_7'], venta['product_line_mkt'], venta['sale_zone'],
            venta['sale_zone_descr'], venta['division'], venta['division_descr'], venta['year'], venta['month'],
                float(venta['sale_qty'].replace(',', '.')),  float(
                    venta['volume'].replace(',', '.')), float(venta['cost'].replace(',', '.')),
                float(venta['price_list'].replace(',', '.')), float(venta['discount_automatic'].replace(',', '.')), float(
                    venta['discount_manual'].replace(',', '.')), float(venta['transport_total'].replace(',', '.')),
                float(venta['price_net'].replace(',', '.')), float(venta['tax'].replace(',', '.')))
            print("se inserta registro")
            print(add_venta)
            print(data_venta)
            # Insert new employee
            cursor.execute(add_venta, data_venta)
            #emp_no = cursor.lastrowid
            print(data_venta)
        # Make sure data is committed to the database
        cnx.commit()

        cursor.close()
        cnx.close()
