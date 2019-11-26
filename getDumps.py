import mwxml

dump = mwxml.Dump.from_file(open("dump.xml"))
print(dump.site_info.name, dump.site_info.dbname)

for page in dump[:1]:
    print(page)
