# # # from another_module import another_var
# # #
# # # print(another_var)
# #
# # from turtle import Turtle, Screen
# # timmy=Turtle()
# # print(timmy)
# # timmy.shape("circle")
# # timmy.color("coral")
# # timmy.forward(300)
# # timmy.right(90)
# # timmy.forward(300)
# # timmy.right(90)
# # timmy.forward(300)
# # timmy.right(90)
# # timmy.forward(300)
# # my_screen= Screen()
# # print(my_screen.canvheight)
# # my_screen.exitonclick()
#
# from prettytable import PrettyTable
# table = PrettyTable()
#
# table.add_column("Pokemon Name",["Pikachu","Squirtle", "Charmander"])
# table.add_column("Type",["Electric","Water", "Fire"])
#
# # table.field_names = ["City name", "Area", "Population", "Annual Rainfall"]
# # table.add_row(["Adelaide", 1295, 1158259, 600.5])
# # table.add_row(["Brisbane", 5905, 1857594, 1146.4])
# # table.add_row(["Darwin", 112, 120900, 1714.7])
# # table.add_row(["Hobart", 1357, 205556, 619.5])
# # table.add_row(["Sydney", 2058, 4336374, 1214.8])
# # table.add_row(["Melbourne", 1566, 3806092, 646.9])
# # table.add_row(["Perth", 5386, 1554769, 869.4])
# table.align="l"
# print(table)



from turtle import Turtle,Screen
timmy=Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("coral")
for i in range(0,4):
    timmy.forward(300)
    timmy.right(90)


my_screen=Screen()
print(my_screen.canvheight)
my_screen.exitonclick()

from prettytable import PrettyTable
table=PrettyTable()
table.add_column("Pokemon Name",["Pikachu","Squirtle","Charmander","Lily"])
table.add_column(" Type",["Electric","Water","Fire","Flower"])
table.align="r"
print(table)
