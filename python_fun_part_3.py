# FUNCTION 1
def name_args(**lots_of_args):
    for i in lots_of_args.items():
        print(i)
    return

name_args(food="Pie", verb="is", adjective="delicious")