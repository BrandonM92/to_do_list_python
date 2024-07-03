# with open("files/doc.txt") as file:
#     print(file.read())


# # contents = ["All carrots are fun", "The carrots got sliced","I really don't like carrots"]
# #
# filenames = ["doc.txt","report.txt","presentation.txt"]
# #
# #
# # for content, filename in zip(contents,filenames):
# #     file = open(f"files/{filename}",'w')
# #     file.write(content)
#
# #
# # new_name = input("Add a new member: ")
# # name = '\n' + new_name
# # file = open('files/members.txt','a')
# # file.write(f'{name}')
#
# for filename in filenames:
#     file = open(f'files/{filename}','r')
#     data = file.read()
#     print(type(data))
#     print(f"I am {data}")
#

# user_entries = ['10', '19.1', '20']
# sum_total = 0
# for x in user_entries:
#     sum_total += float(x)
#
# print(sum_total)

# temperature = [10,12,14]
# temp = [str(i) + '\n' for i in temperature]
#
# file = open("files/file.txt",'w')
# file.writelines(temp)
