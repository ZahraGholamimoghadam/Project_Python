
مهوش مرادی علمدارلو
چون نوشتیم dictwriter نمیتونیم لیست بدیم
سمیه رزاقی
یک سطر جدید درست کرده مطمئنا
فاطمه رحمن زاده
قبلی رو نگه میداره
سمیه رزاقی
چرا delete row نداره اخه
مهوش مرادی علمدارلو
میشه حذف کرد با csv
مهوش مرادی علمدارلو
?
سمیه رزاقی
سه تا داری
فاطمه رحمن زاده
به نظرم باید کل فایل رو بخونیم به صورت دیکشنری... یوزر مورد نظر رو تغییر بدیم بع دوباره کل فایل رو بنویسیم.... اما با کتابخونه ها یکم ساده تره
کوثر کرباسی
چرا؟ if هم که گذاشته بودیم...
زهرا غلامی مقدم
بزرگ میکنی
کوثر کرباسی
الان فایل register چی شد؟
فاطمه رحمن زاده
https://www.geeksforgeeks.org/update-column-value-of-csv-in-python/
سمیه رزاقی
فاطمه رحمن زاده
به نظرم باید کل فایل رو بخونیم به صورت دیکشنری... یوزر مورد نظر رو تغییر بدیم بع دوباره کل فایل رو بنویسیم.... اما با کتابخونه ها یکم ساده تره
بشرطی که کا فایل پاک نشه😅
کوثر کرباسی
فاطمه رحمن زاده
https://www.geeksforgeeks.org/update-column-value-of-csv-in-python/
این پانداسه
ختن سوداگر
haminja az pandas estefade konim.tamrine khubiam hast
فاطمه رحمن زاده
کوثر کرباسی
این پانداسه
سه تا مدل گفته
کوثر کرباسی
فاطمه رحمن زاده
سه تا مدل گفته
عه اره 😍
فاطمه رحمن زاده
سمیه رزاقی
بشرطی که کا فایل پاک نشه😅
کل سطرها رو اگه بخونیم دیگه نگران اونش نیستیم😄
کوثر کرباسی
https://stackoverflow.com/questions/16020858/inline-csv-file-editing-with-python
اینم دیروز سارا جون داد
فاطمه رحمن زاده
من با جیسون نوشتم اینو الان سرچ کردم😅
زهرا غلامی مقدم
pandas رو نصب کردین قبلا؟
فاطمه رحمن زاده
خب من برای همه دیتاهای هر یوزر یه فایل دارم... هر متدم جدا یدونه فایل نداره
سمیه امرایی
من تو دیباگ کرن مشکل دارم
کوثر کرباسی
فاطمه رحمن زاده
https://www.geeksforgeeks.org/update-column-value-of-csv-in-python/
فاطمه جان اینو امتحان کردی؟ جواب داده؟
فاطمه رحمن زاده
فاطمه رحمن زاده
خب من برای همه دیتاهای هر یوزر یه فایل دارم... هر متدم جدا یدونه فایل نداره
نه برای هر یوزر یه دیکشنری دارم ببخشید اشتباه شد
عادله علی بیگی
برای یاداور ما باید تسک هامون رو بتونیم اپدیت کنیم من هیچ ایده ای برای کار با فایل نداریم:/
عادله علی بیگی
+
سمیه رزاقی
+
زهرا غلامی مقدم
بله
کوثر کرباسی
+
مهسا آشنا
+
فاطمه رحمن زاده
+
ختن سوداگر
kosar in replace o diruz manzuram bud :))
زهرا غلامی مقدم
یبار دیگه میگین مسیرشو
فاطمه سبزواری
کدارو میفرستین؟
کوثر کرباسی
ختن سوداگر
kosar in replace o diruz manzuram bud :))
عه :))) چه اسمایی گفتیم :)))
فهیمه معینی
چه عالی من با colorma پایچارمم مشکل داره
زهرا غلامی مقدم
یعنی دیگه لازم نیست بریم تو vitual enviorment نصب کنیم؟
عادله علی بیگی
man fek konam daram
فاطمه رحمن زاده
یبار اگه فایل .py رو اجرا کنید درست میشه...colorama من همینجوری کار کرد
زهرا متین فر
import pandas as pd
# reading the csv file
df = pd.read_csv("pandas_csv.csv")
# updating the column value/data
df['Status'] = df['Status'].replace({'u': 'a'})
# writing into the file
df.to_csv("pandas_csv.csv", index=False)
print(df)
زهرا متین فر
Sno,RegisterNumber,Name,Status
1,111,A,u
2,222,A,u
3,333,C,a
مهرناز معروف
نه واضح نیست :)
فاطمه رحمن زاده
+
آرزو مرادی
زهرا جان با این پاندا فقط مقادیر دیتا رو تغییر میدیم؟
زهرا متین فر
# importing the pandas libraryimport pandas as pd  # reading the csv filedf = pd.read_csv("AllDetails.csv")  # updating the column value/datadf.loc[5, 'Name'] = 'SHIV CHANDRA'  # writing into the filedf.to_csv("AllDetails.csv", index=False)  print(df)
زهرا متین فر
# importing the pandas library
import pandas as pd
# reading the csv file
df = pd.read_csv("AllDetails.csv")
# updating the column value/data
df.loc[5, 'Name'] = 'SHIV CHANDRA'
# writing into the file
df.to_csv("AllDetails.csv", index=False)
print(df)
زهرا متین فر
https://www.geeksforgeeks.org/update-column-value-of-csv-in-python/
فهیمه معینی
خط 15 چی شد؟
آرزو مرادی
چون لوکیشن رو درست ندادیم
آرزو مرادی
پنج رو باید با یک یا دو عوض میکردیم
فاطمه رحمن زاده
لوکیشنش رو چطوری پیدا کردیم؟
فهیمه معینی
با replace نمیشه؟
کوثر کرباسی
صدای جیک جیک میاد؟ 😅
کوثر کرباسی
😍😍😍
عادله علی بیگی
name,password
alex,1c6637a8f2e1f75e06ff9984894d6bd16a3a36a9
jlo,4af7f9edc0f545f4de769f2e9e763df919915cab
david,43814346e21444aaf4f70841bf7ed5ae93f55a9d
naghme,cfa1150f1787186742a9a884b73a43d8cf219f9b
faraz,8bd7954c40c1e59a900f71ea3a266732609915b1
faeze,25a5e3012854728e0c6ab97fdcbb65c3a00c0965
asare,ceab25abfedcba417c7cade07076c93c1cdacc44
sahra,6216f8a75fd5bb3d5f22b6f9958cdede3fc086c2
sarah,1c6637a8f2e1f75e06ff9984894d6bd16a3a36a9
halaa,1c6637a8f2e1f75e06ff9984894d6bd16a3a36a9
adele,1c6637a8f2e1f75e06ff9984894d6bd16a3a36a9
آرزو مرادی
عادله ی اسم دیگه بده فک کنم صحرارو چن بار بهش دادی
سمیه امرایی
loc چیکار میکرد . حواسم نبود اون لحطه
کوثر کرباسی
توی اون لینکه، لوکیشن ها از 1 شروع میشن. اینجا هم نباید اون اول location = 1 بذاریم؟
ختن سوداگر
darim
ختن سوداگر
khodesh index mizare
فاطمه رحمن زاده
index چیکار میکنه؟
مهوش مرادی علمدارلو
فکر کنم از رجیستر میخونه
مهوش مرادی علمدارلو
رجیستر2 را تغییر میده
فاطمه رحمن زاده
هممون با آپدیت csv مشکل داریم
مهوش مرادی علمدارلو
توجه کنید لطفا
عادله علی بیگی
def change_password(self):
change = pd.read_csv('register2.csv')
location = 0
old_password = input("Enter old password: ")
new_password = input("Enter new password: ")
hash_old_pass = hashlib.sha1(old_password.encode()).hexdigest()
hash_new_pass = hashlib.sha1(new_password.encode()).hexdigest()
with open('register2.csv', 'r') as my_file:
# csv_writer = csv.DictWriter(my_file,fieldnames=['name','password'])
csv_reader = csv.DictReader(my_file)
for row in csv_reader:
if row['name'] == self.username and row['password'] == hash_old_pass:
self.password = hash_new_pass
print("Your password is changed.")
change.loc[location,'password'] = hash_new_pass
change.to_csv('register2.csv',index=False)
location += 1
کوثر کرباسی
😍😍😍 مبارکه
فاطمه رحمن زاده
😃😃😃
فهیمه معینی
میشه آپلود کنی؟
زهرا غلامی مقدم
سینتکسهاشو از همون سایته نوشتین؟
عادله علی بیگی
def change_password(self):
change = pd.read_csv('register.csv')
location = 0
old_password = input("Enter old password: ")
new_password = input("Enter new password: ")
hash_old_pass = hashlib.sha1(old_password.encode()).hexdigest()
hash_new_pass = hashlib.sha1(new_password.encode()).hexdigest()
with open('register.csv', 'r') as my_file:
# csv_writer = csv.DictWriter(my_file,fieldnames=['name','password'])
csv_reader = csv.DictReader(my_file)
for row in csv_reader:
if row['name'] == self.username and row['password'] == hash_old_pass:
self.password = hash_new_pass
print("Your password is changed.")
change.loc[location,'password'] = hash_new_pass
change.to_csv('register.csv',index=False)
location += 1