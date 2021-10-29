import csv 
filename = "orders.csv"
header = ("Order_Num", "Cake", "Name", "Email", "Phone")
data = [
('3703', 'confetti', 'rayyan', 'rayyanshikoh5@gmail.com', '0505251175')
]

def writer(header, data, filename):
  with open (filename, "w", newline = "") as csvfile:
    movies = csv.writer(csvfile)
    movies.writerow(header)
    for x in data:
      movies.writerow(x)


def new_writer(filename, header, name, email, phone, cake, order_num):
    with open (filename, "a", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, header, extrasaction='ignore')
        writer.writerow({'Name': name, 'Email': email, 'Phone': phone, 'Cake': cake, 'Order_Num': order_num})

# def deleter(filename, errorrow):
#     lines = []
#     with open(filename, 'r') as readFile:
#         reader = csv.reader(readFile)
#         for row in reader:
#             lines.append(row)
#             for field in row:
#                 if field == errorrow:
#                     lines.remove(row)
#     with open(filename, 'w') as writeFile:
#         writer = csv.writer(writeFile)
#         writer.writerows(lines)

def deleter(filename, errorrow):
    import pandas as pd
    df = pd.read_csv(filename)
    df_s = df
    df_s.set_index('Order_Num', inplace=True)
    df_s = df_s.drop(errorrow)
    df_s.to_csv(filename)


writer(header, data, filename)
new_writer(filename, header, name="Rayyan", email="rayyanshikoh5@gmail.com", phone="0505767", cake="free cake", order_num='3543')