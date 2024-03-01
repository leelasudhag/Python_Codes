from pyspark.sql import SparkSession
import getpass
username=getpass.getuser()
spark=SparkSession.\
builder.\
config('spark.ui.port','0').\
config("spark.sql.warehouse.dir",f"/user/itv011141/warehouse").\
enableHiveSupport().\
master('yarn').\
getOrCreate()

orders_schema = ["order_id","order_item","order_location","item_status"]
users_schema = ["user_id","user_name","order_num"]

orders_list = [(1,"soap","oregon","pending"),
              (2,"dish","cali","inreview"),
              (3,"watch","wahington","inprogress"),
              (4,"handbag","utah","pending"),
              (1,"tv","oregon","pending"),
              (1,"perfume","oregon","pending")]
user_list = [(101,"leela","1"),
            (105,"sriram","2"),
             (109,"sasi","3"),
              (103,"debow","4")]

orders_df = spark.createDataFrame(orders_list,orders_schema)
orders_df.createOrReplaceTempView("orders")
users_df = spark.createDataFrame(user_list,users_schema)
users_df.createOrReplaceTempView("users")

orders_df.show()
users_df.show()

spark.sql("""select a.order_id,count(a.order_item),b.user_name from orders a join users b on a.order_id = b.order_num
          group by a.order_id,b.user_name having count(a.order_item)> 2""").show()

spark.sql("""select a.order_id,count(a.order_item),b.user_name from orders a join users b on a.order_id = b.order_num
            where item_status = "pending"
          group by a.order_id,b.user_name having count(a.order_item)> 2 """).show()