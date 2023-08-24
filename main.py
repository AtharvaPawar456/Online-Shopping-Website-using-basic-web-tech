from flask import Flask, render_template, request
import sqlite3

DATABASE = 'data.db'
app = Flask(__name__)

# @app.route('/')
# def index():
#   return '<b>Parshu :: Aditya, Riddhi, Atharva '


@app.route('/')
def home():
#   conn = sqlite3.connect(DATABASE)
#   c = conn.cursor()
#   c.execute("SELECT * FROM card_products WHERE id IN (30, 31, 32)")
#   all_data = c.fetchall()
#   conn.close()
#   print(all_data)
#   # Update the image path with full actual path
#   path = 'product_img/'
#   all_data_with_updated_paths = [(product[0], product[1], path + product[2],
#                                   product[3], product[4], product[5])
#                                  for product in all_data]

  return render_template('index.html')


@app.route('/business')
def business():
  return render_template('business.html')


@app.route('/contact')
def contact():
  return render_template('contact.html')


@app.route('/about')
def about():
  return render_template('about.html')


@app.route('/business_plan1')
def business_plan1():
  return render_template('business_plan1.html')


@app.route('/business_plan2')
def business_plan2():
  return render_template('business_plan2.html')


# @app.route('/productpage')
# def productpage():
#   conn = sqlite3.connect(DATABASE)
#   c = conn.cursor()
#   c.execute("SELECT * FROM card_products")
#   all_data = c.fetchall()
#   conn.close()
#   print(all_data)
#   path = 'product_img/'
#   all_data_with_cat = [
#     (product[0], product[1], path + product[2],
#      'Nutrition' if product[3] == 'Health' else
#      'Personal Hygiene' if product[3] == 'Cosmetics' else 'Beverages',
#      product[4], product[5]) for product in all_data
#   ]

#   return render_template('productlist.html', data=all_data_with_cat)


# @app.route('/allproduct')
# def allproduct():
#   conn = sqlite3.connect(DATABASE)
#   print("Opened database successfully")
#   c = conn.cursor()  # c.execute("SELECT * FROM card_products")

#   c.execute("SELECT * FROM card_products WHERE category = 'Health'")
#   healthCat_data = c.fetchall()

#   c.execute("SELECT * FROM card_products WHERE category = 'Cosmetics'")
#   CosmaticsCat_data = c.fetchall()

#   c.execute("SELECT * FROM card_products WHERE category = 'Beverages'")
#   BevragesCat_data = c.fetchall()
#   conn.close()

#   def printAll(data):
#     for rowdata in data:
#       print(f"{rowdata}\n")

#   # Update the image path with full actual path
#   path = 'product_img/'
#   healthCat_data_with_updated_paths = [
#     (product[0], product[1], path + product[2], product[3], product[4],
#      product[5]) for product in healthCat_data
#   ]
#   CosmaticsCat_data_with_updated_paths = [
#     (product[0], product[1], path + product[2], product[3], product[4],
#      product[5]) for product in CosmaticsCat_data
#   ]
#   BevragesCat_data_with_updated_paths = [
#     (product[0], product[1], path + product[2], product[3], product[4],
#      product[5]) for product in BevragesCat_data
#   ]
#   # OthersCat_data_with_updated_paths     = [(product[0], product[1], path + product[2], product[3], product[4])for product in OthersCat_data]

#   # printAll(healthCat_data_with_updated_paths);
#   # printAll(CosmaticsCat_data_with_updated_paths)
#   # printAll(BevragesCat_data_with_updated_paths)
#   # printAll(OthersCat_data_with_updated_paths)

#   cardelements = [
#     healthCat_data_with_updated_paths, CosmaticsCat_data_with_updated_paths,
#     BevragesCat_data_with_updated_paths
#   ]

#   return render_template('allproducts.html', carddata=cardelements)


# # /singleproduct?productslug=johndoe-eysdcv
# @app.route('/singleproduct', methods=['GET'])
# def get_username():
#   username = request.args.get('productslug')
#   return f"<h1>The Product is:<br> {username}</h1>"


# @app.route('/products')
# def productPage():
#   conn = sqlite3.connect(DATABASE)
#   c = conn.cursor()
#   c.execute("SELECT * FROM products WHERE id = 1")
#   all_product_info = c.fetchall()
#   conn.close()
#   cat_name = all_product_info[0][6]
#   print(cat_name)

#   # Recommend 3 products cards
#   conn = sqlite3.connect(DATABASE)
#   c = conn.cursor()
#   # c.execute(f"SELECT * FROM card_products WHERE description = {cat_name} ORDER BY RANDOM() LIMIT 3;")
#   if (cat_name == 'Health'):
#     c.execute(
#       "SELECT * FROM card_products WHERE category = 'Health'  ORDER BY RANDOM() LIMIT 3;"
#     )
#   elif (cat_name == 'Cosmetics'):
#     c.execute(
#       "SELECT * FROM card_products WHERE category = 'Cosmetics'  ORDER BY RANDOM() LIMIT 3;"
#     )
#   else:
#     c.execute(
#       "SELECT * FROM card_products WHERE category = 'Beverages'  ORDER BY RANDOM() LIMIT 3;"
#     )
#   recommend_data = c.fetchall()
#   conn.close()

#   # all_product_info_with_updated_paths = all_product_info_with_updated_paths + recommend_data
#   path = 'product_img/'
#   recommend_data_with_updated_paths = [
#     (product[0], product[1], path + product[2], product[3], product[4],
#      product[5]) for product in recommend_data
#   ]

#   print(recommend_data_with_updated_paths[0])

#   # Update the image path with full actual path [10]
#   path = 'img/'
#   all_product_info_with_updated_paths = [
#     all_product_info[0][0], all_product_info[0][1],
#     path + all_product_info[0][2], all_product_info[0][3],
#     all_product_info[0][4], all_product_info[0][5], all_product_info[0][6],
#     all_product_info[0][7], recommend_data_with_updated_paths[0],
#     recommend_data_with_updated_paths[1], recommend_data_with_updated_paths[2]
#   ]

#   return render_template('product.html',
#                          data=all_product_info_with_updated_paths)


# # http://localhost:5000/product_id?input=123
# # http://localhost:5000/product_id?input=1
# @app.route('/product_id')
# def show_data():
#   input_value = request.args.get('input')
#   conn = sqlite3.connect(DATABASE)
#   c = conn.cursor()
#   c.execute(f"SELECT * FROM products WHERE id = {input_value}")
#   rowdata = c.fetchall()

#   return render_template('product.html', data=rowdata)


if __name__ == '__main__':
  app.run(debug=True)
#   app.run(host='0.0.0.0', port=81)


"""
# def Show_Data(DATABASE):
#   conn = sqlite3.connect(DATABASE)
#   # print("Opened database successfully")
#   c = conn.cursor()
# #   c.execute("SELECT sr FROM products")
#   c.execute("SELECT * FROM products WHERE id = 1")  
#   # Modify the WHERE clause to specify the desired ID

#   data = c.fetchall()
#   for rowdata in data:
#     print(f"{rowdata}\n")
#   conn.close()



"""
