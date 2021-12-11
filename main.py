"""this is the main script"""
import argparse
import random
import sys


class DOORs:
    status = True  #to define if a door is chose-able or not
    chosen = False
    def __init__(self, car_goat:bool = False):
        """
        define if there is a car or goat behind the door
        :param car_goat:
        """
        self.car_goat = car_goat

    def open_goat_door(self):
        """this function are used for open the goat door after individual choose a door"""
        if self.chosen == False and self.car_goat == False:
            self.status = False
        else:
            self.status = True

    def pick(self):
        """ this method are used for pick a door"""
        if self.status == True:
            self.chosen = True


def get_para():
    """to get parameters from command line"""
    parser = argparse.ArgumentParser(description="set up the parameter")
    parser.add_argument('-r', '--round', dest="ROUND", help="set up round times", required=False,\
                         type = int, default=1000)
    parser.add_argument('-d', '--doors', dest="DOORs", help="the number of doors are created",\
                       required=False, type = int, default=3)
    parser.add_argument('-c', '--chose', dest="Door_c", help="the index of doors that was chosen",\
                        required=False, type=int, default=1)
    return parser.parse_args()


def modify(r, doors, chosen):
    """
    this function is used for checking the legibility of the those parameters
    :param r: times the function will repeat
    :param doors: the number of doors that will be created
    :param chosen: the index of door that are chosen
    :return: Nont
    """
    if r < 100:
        print("\nthe round that you input is too small to get a reliable result, you may want to input a larger round number\n")
    if doors < 3:
        sys.exit('\nthe doors number are needed to be more than three, please try another doors amount\n' )
    if chosen > doors:
        sys.exit('\nthe chosen number need to be less than the doors you choose\n')



def generate_doors(doors:int):
    """
    this function are used for generate a certain number of doors, and place a car behind a door
    :param doors: int
    :return: list, n(the index of door that has car)
    """
    door_list = []
    n = random.randint(0, doors-1)
    for i in range(doors):
        if i != n:
            door = DOORs(False)
            door_list.append(door)
        else:
            door = DOORs(True)
            door_list.append(door)
    return door_list, n


def close_doors(door_list:list[DOORs]):
    """
    this function should close all of doors that are not chosen and don't have cars.
    :param door_list:
    :return:
    """
    for i in door_list:
        i.open_goat_door()

def main():
    args = get_para()
    r, doors, chosen = args.ROUND, args.DOORs, args.Door_c-1
    modify(r, doors, chosen)

    change_mind_win_count = 0
    not_change_mind_win_count = 0

    for _ in range(r):
        door_list, n = generate_doors(doors)
        door_list[chosen].pick()
        close_doors(door_list)
        #donot change my mind
        if door_list[chosen].car_goat == True and door_list[chosen].chosen == True:
            not_change_mind_win_count += 1
        change_mind_win_count = r - not_change_mind_win_count



    #output result
    print(f"\n\tchange\t\tnot_change")
    print(f"win\t{change_mind_win_count}\t\t{not_change_mind_win_count}")
    print(f"loss\t{r-change_mind_win_count}\t\t{r-not_change_mind_win_count}")
    print(f"\nThe winning possibility if you change your mind is: {change_mind_win_count/r:.2%}\n")

if __name__ == '__main__':
    main()












