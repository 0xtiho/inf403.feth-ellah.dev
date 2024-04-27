#!/usr/bin/python3

from utils import db
from utils import Requests
import os



def menu(conn):
    while True:
        print("\nMENU:")
        print("===============")
        print("1. Show tables")
        print("2. Show rows")
        print("3. Update tables")
        print("4. Tools (SOON)")
        print("5. Exit")
        print("===============")

        choice = input("Enter your choice: ")
        if choice == '1':
            clear_screen()
            db.show_tables(conn)
        elif choice == '2':
            while True:
                print("00. Return to main menu")
                table = input("Enter table name: ")
                if table == '00':
                    clear_screen()
                    break
                else:
                    if db.check_table_existence(conn, table):
                        db.show_rows(conn, table)
                        break
                    else:
                        print("Invalid table name. Please try again.")
        elif choice == '3':
            clear_screen()
            UpdatingMenu(conn)
        elif choice == '4':
            clear_screen()
            ToolsMenu(conn)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

def UpdatingMenu(conn):
    while True:
        print("\nUpdating Menu:")
        print("===============")
        print("1. Add row")
        print("2. Update row")
        print("3. Remove row")
        print("00. Return to main menu")
        print("===============")

        choice = input("Enter your choice: ")
        if choice == '1':
            db.Add_row(conn)
        elif choice == '2':
            db.Update_row(conn)
        elif choice == '3':
            db.Remove_row(conn)
        elif choice == '00':
            clear_screen()
            print("Returning to main menu.")
            break
        else:
            print("Invalid choice")

def ToolsMenu(conn):
    while True:
        print("\nTools Menu:")
        print("===============")
        print("1. Perform a custom SQL query")
        print("2. customer information by ID")
        print("3. product information by ID")
        print("4. order information by ID")
        print("5. warehouse information by ID")
        print("6. recycling company information by ID")
        print("7. city information by postal code")
        print("8. orders for a product")
        print("9. products ordered by a customer")
        print("10. orders placed by customers in a city")
        print("11. orders placed within a date range")
        print("12. customers who placed orders on a date")
        print("13. products with a waste type")
        print("14. orders containing products from a recycling company")
        print("15. orders containing products from a warehouse")
        print("16. orders containing products from a city")
        print("17. orders containing products of a type")
        print("18. orders containing products with a waste type")
        print("19. orders containing products with a name")
        print("20. orders containing products with a ID")
        print("21. orders placed by customers with a ID")
        print("22. orders placed by customers with a name")
        print("23. customers who ordered products with a ID")
        print("24. customers who ordered products with a name")
        print("25. customers who ordered products from a city")
        print("26. customers who ordered products within a date range")
        print("27. products ordered by customers with a ID")
        print("28. products ordered by customers with a name")
        print("29. products ordered by customers from a city")
        print("30. products ordered by customers within a date range")
        print("31. products ordered by customers of a type")
        print("32. products ordered by customers with a waste type")
        print("33. products ordered by customers with a ID and within a date range")
        print("34. products ordered by customers with a name and within a date range")
        print("35. products ordered by customers from a city and within a date range")
        print("36. products ordered by customers of a type and within a date range")
        print("37. products ordered by customers with a waste type and within a date range")
        print("38. customers who ordered products with a ID and within a date range")
        print("39. customers who ordered products with a name and within a date range")
        print("40. customers who ordered products from a city and within a date range")
        print("41. customers who ordered products of a type and within a date range")
        print("42. customers who ordered products with a waste type and within a date range")
        print("43. orders containing products from a warehouse and within a date range")
        print("44. orders containing products from a recycling company and within a date range")
        print("45. orders containing products from a city and within a date range")
        print("46. orders containing products of a type and within a date range")
        print("47. orders containing products with a waste type and within a date range")
        print("48. orders containing products with a name and within a date range")
        print("49. orders containing products with a ID and within a date range")
        print("00. Return to main menu")
        print("===============")

        choice = input("Enter your choice: ")
        if choice == '1':
            perform_custom_sql_query(conn)
            input(" :) Press Enter to continue...")
        elif choice == '2':
           Requests.customer_by_id(conn)
           input(" :) Press Enter to continue...")
        elif choice == '3':
           Requests.product_by_id(conn)
           input(" :) Press Enter to continue...")
        elif choice == '4':
           Requests.order_by_id(conn)
           input(" :) Press Enter to continue...")
        elif choice == '5':
           Requests.warehouse_by_id(conn)
           input(" :) Press Enter to continue...")
        elif choice == '6':
           Requests.recycling_company_by_id(conn)
           input(" :) Press Enter to continue...")
        elif choice == '7':
           Requests.city_by_postal_code(conn)
           input(" :) Press Enter to continue...")
        elif choice == '8':
           Requests.orders_by_product_id(conn)
           input(" :) Press Enter to continue...")
        elif choice == '9':
           Requests.products_by_customer_id(conn)
           input(" :) Press Enter to continue...")
        elif choice == '10':
           Requests.orders_by_city(conn)
           input(" :) Press Enter to continue...")
        elif choice == '11':
           Requests.orders_by_date_range(conn)
           input(" :) Press Enter to continue...")
        elif choice == '12':
           Requests.customers_by_order_date(conn)
           input(" :) Press Enter to continue...")
        elif choice == '13':
           Requests.products_by_waste_type(conn)
           input(" :) Press Enter to continue...")
        elif choice == '14':
           Requests.orders_by_recycling_company(conn)
           input(" :) Press Enter to continue...")
        elif choice == '15':
           Requests.orders_by_warehouse(conn)
           input(" :) Press Enter to continue...")
        elif choice == '16':
           Requests.orders_by_city(conn)
           input(" :) Press Enter to continue...")
        elif choice == '17':
           Requests.orders_by_product_type(conn)
           input(" :) Press Enter to continue...")
        elif choice == '18':
           Requests.orders_by_product_waste_type(conn)
           input(" :) Press Enter to continue...")
        elif choice == '19':
           Requests.orders_by_product_name(conn)
           input(" :) Press Enter to continue...")
        elif choice == '20':
           Requests.orders_by_product_id(conn)
           input(" :) Press Enter to continue...")
        elif choice == '21':
           Requests.orders_by_customer_id(conn)
           input(" :) Press Enter to continue...")
        elif choice == '22':
           Requests.orders_by_customer_name(conn)
           input(" :) Press Enter to continue...")
        elif choice == '23':
           Requests.customers_by_product_id(conn)
           input(" :) Press Enter to continue...")
        elif choice == '24':
           Requests.customers_by_product_name(conn)
           input(" :) Press Enter to continue...")
        elif choice == '25':
           Requests.customers_by_city(conn)
           input(" :) Press Enter to continue...")
        elif choice == '26':
           Requests.customers_by_order_date_range(conn)
           input(" :) Press Enter to continue...")
        elif choice == '27':
           Requests.products_by_customer_id(conn)
           input(" :) Press Enter to continue...")
        elif choice == '28':
           Requests.products_by_customer_name(conn)
           input(" :) Press Enter to continue...")
        elif choice == '29':
           Requests.products_by_customer_city(conn)
           input(" :) Press Enter to continue...")
        elif choice == '30':
           Requests.products_by_customer_order_date_range(conn)
           input(" :) Press Enter to continue...")
        elif choice == '31':
           Requests.products_by_customer_type(conn)
           input(" :) Press Enter to continue...")
        elif choice == '32':
           Requests.products_by_customer_waste_type(conn)
           input(" :) Press Enter to continue...")
        elif choice == '33':
           Requests.products_by_customer_id_and_date_range(conn)
           input(" :) Press Enter to continue...")
        elif choice == '34':
           Requests.products_by_customer_name_and_date_range(conn)
           input(" :) Press Enter to continue...")
        elif choice == '35':
           Requests.products_by_customer_city_and_date_range(conn)
           input(" :) Press Enter to continue...")
        elif choice == '36':
           Requests.products_by_customer_type_and_date_range(conn)
           input(" :) Press Enter to continue...")
        elif choice == '37':
           Requests.products_by_customer_waste_type_and_date_range(conn)
           input(" :) Press Enter to continue...")
        elif choice == '38':
           Requests.customers_by_product_id_and_date_range(conn)
           input(" :) Press Enter to continue...")
        elif choice == '39':
           Requests.customers_by_product_name_and_date_range(conn)
           input(" :) Press Enter to continue...")
        elif choice == '40':
           Requests.customers_by_city_and_date_range(conn)
           input(" :) Press Enter to continue...")
        elif choice == '41':
           Requests.customers_by_product_type_and_date_range(conn)
           input(" :) Press Enter to continue...")
        elif choice == '42':
           Requests.customers_by_product_waste_type_and_date_range(conn)
           input(" :) Press Enter to continue...")
        elif choice == '43':
           Requests.orders_by_warehouse_and_date_range(conn)
           input(" :) Press Enter to continue...")
        elif choice == '44':
           Requests.orders_by_recycling_company_and_date_range(conn)
           input(" :) Press Enter to continue...")
        elif choice == '45':
           Requests.orders_by_city_and_date_range(conn)
           input(" :) Press Enter to continue...")
        elif choice == '46':
           Requests.orders_by_product_type_and_date_range(conn)
           input(" :) Press Enter to continue...")
        elif choice == '47':
           Requests.orders_by_product_waste_type_and_date_range(conn)
           input(" :) Press Enter to continue...")
        elif choice == '48':
           Requests.orders_by_product_name_and_date_range(conn)
           input(" :) Press Enter to continue...")
        elif choice == '49':
           Requests.orders_by_product_id_and_date_range(conn)
           input(" :) Press Enter to continue...")
        elif choice == '00':
            clear_screen()
            print("Returning to main menu.")
            break
        else:
            print("Invalid choice")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
def main():
    db_file = "data/MyDB.db"
    conn = db.creer_connexion(db_file)
    print("Creating the Database and Initializing Tables")
    db.mise_a_jour_bd(conn, "data/BDL2_creation.sql")
    db.mise_a_jour_bd(conn, "data/BDL2_OK_Insert.sql")
    print("Tables are created successfully :)")
    menu(conn)

if __name__ == "__main__":
    print("Welcome to BDL2 Program !")
    main()
