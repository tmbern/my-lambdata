import pandas

from my_lambdata_tmb.my_mod import enlarge


print("Hello World")

df = pandas.DataFrame({"state": ["CT", "CO", "CA", "TX"]})
print(df.head())

print(enlarge(9))