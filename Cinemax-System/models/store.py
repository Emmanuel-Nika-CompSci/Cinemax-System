#import tabulate
import pandas as pd

seats = {'Twin' : [
                ['A', {'5': 'x', '6': 'x', '7': 'x', '8': 'x', '9': 'x', '10': 'x', '11': 'x', '12': 'x', '13': 'x', '14': 'x', '15': 'x', '16': 'x'}],
                ['B', {'5': 'x', '6': 'x', '7': 'x', '8': 'x', '9': 'x', '10': 'x', '11': 'x', '12': 'x', '13': 'x', '14': 'x', '15': 'x', '16': 'x'}],
        ],
    'VVIP' : [
                ['A', {'1': 'x', '2': 'x', '3': 'x', '4': 'x', '17': 'x', '18': 'x', '19': 'x', '20': 'x'}],
                ['B', {'1': 'x', '2': 'x', '3': 'x', '4': 'x', '17': 'x', '18': 'x', '19': 'x', '20': 'x'}], 
                ['C', {'1': 'x', '2': 'x', '3': 'x', '4': 'x', '5': 'x', '6': 'x', '7': 'x', '8': 'x', '9': 'x', '10': 'x', '11': 'x', '12': 'x', '13': 'x', '14': 'x', '15': 'x', '16': 'x', '17': 'x', '18': 'x', '19': 'x', '20': 'x'}], 
                ['D', {'1': 'x', '2': 'x', '3': 'x', '4': 'x', '5': 'x', '6': 'x', '7': 'x', '8': 'x', '9': 'x', '10': 'x', '11': 'x', '12': 'x', '13': 'x', '14': 'x', '15': 'x', '16': 'x', '17': 'x', '18': 'x', '19': 'x', '20': 'x'}], 
                ['E', {'1': 'x', '2': 'x', '3': 'x', '4': 'x', '5': 'x', '6': 'x', '7': 'x', '8': 'x', '9': 'x', '10': 'x', '11': 'x', '12': 'x', '13': 'x', '14': 'x', '15': 'x', '16': 'x', '17': 'x', '18': 'x', '19': 'x', '20': 'x'}], 
                ['F', {'1': 'x', '2': 'x', '3': 'x', '4': 'x', '5': 'x', '6': 'x', '7': 'x', '8': 'x', '9': 'x', '10': 'x', '11': 'x', '12': 'x', '13': 'x', '14': 'x', '15': 'x', '16': 'x', '17': 'x', '18': 'x', '19': 'x', '20': 'x'}], 
        ],  
    'VIP' : [
                ['G', {'1': 'x', '2': 'x', '3': 'x', '4': 'x', '5': 'x', '6': 'x', '7': 'x', '8': 'x', '9': 'x', '10': 'x', '11': 'x', '12': 'x', '13': 'x', '14': 'x', '15': 'x', '16': 'x', '17': 'x', '18': 'x', '19': 'x', '20': 'x'}], 
                ['H', {'1': 'x', '2': 'x', '3': 'x', '4': 'x', '5': 'x', '6': 'x', '7': 'x', '8': 'x', '9': 'x', '10': 'x', '11': 'x', '12': 'x', '13': 'x', '14': 'x', '15': 'x', '16': 'x', '17': 'x', '18': 'x', '19': 'x', '20': 'x'}], 
                ['I', {'1': 'x', '2': 'x', '3': 'x', '4': 'x', '5': 'x', '6': 'x', '7': 'x', '8': 'x', '9': 'x', '10': 'x', '11': 'x', '12': 'x', '13': 'x', '14': 'x', '15': 'x', '16': 'x', '17': 'x', '18': 'x', '19': 'x', '20': 'x'}], 
                ['J', {'1': 'x', '2': 'x', '3': 'x', '4': 'x', '5': 'x', '6': 'x', '7': 'x', '8': 'x', '9': 'x', '10': 'x', '11': 'x', '12': 'x', '13': 'x', '14': 'x', '15': 'x', '16': 'x', '17': 'x', '18': 'x', '19': 'x', '20': 'x'}], 
                ['K', {'1': 'x', '2': 'x', '3': 'x', '4': 'x', '5': 'x', '6': 'x', '7': 'x', '8': 'x', '9': 'x', '10': 'x', '11': 'x', '12': 'x', '13': 'x', '14': 'x', '15': 'x', '16': 'x', '17': 'x', '18': 'x', '19': 'x', '20': 'x'}], 
                ['L', {'1': 'x', '2': 'x', '3': 'x', '4': 'x', '5': 'x', '6': 'x', '7': 'x', '8': 'x', '9': 'x', '10': 'x', '11': 'x', '12': 'x', '13': 'x', '14': 'x', '15': 'x', '16': 'x', '17': 'x', '18': 'x', '19': 'x', '20': 'x'}],
        ],
    'Economy' : [
                    ['M', {'1': 'x', '2': 'x', '3': 'x', '4': 'x', '5': 'x', '6': 'x', '7': 'x', '8': 'x', '9': 'x', '10': 'x', '11': 'x', '12': 'x', '13': 'x', '14': 'x', '15': 'x', '16': 'x', '17': 'x', '18': 'x', '19': 'x', '20': 'x'}], 
                    ['N', {'1': 'x', '2': 'x', '3': 'x', '4': 'x', '5': 'x', '6': 'x', '7': 'x', '8': 'x', '9': 'x', '10': 'x', '11': 'x', '12': 'x', '13': 'x', '14': 'x', '15': 'x', '16': 'x', '17': 'x', '18': 'x', '19': 'x', '20': 'x'}], 
                    ['O', {'1': 'x', '2': 'x', '3': 'x', '4': 'x', '5': 'x', '6': 'x', '7': 'x', '8': 'x', '9': 'x', '10': 'x', '11': 'x', '12': 'x', '13': 'x', '14': 'x', '15': 'x', '16': 'x', '17': 'x', '18': 'x', '19': 'x', '20': 'x'}], 
                    ['P', {'1': 'x', '2': 'x', '3': 'x', '4': 'x', '5': 'x', '6': 'x', '7': 'x', '8': 'x', '9': 'x', '10': 'x', '11': 'x', '12': 'x', '13': 'x', '14': 'x', '15': 'x', '16': 'x', '17': 'x', '18': 'x', '19': 'x', '20': 'x'}]
        ]
}

count_available = []
available_seats = []


class SeatAssignment:
    @classmethod
    def count(cls):
        count = 0
        for seat in seats:
            for i in range(len(seats[seat])):
                for n in seats[seat][i][1].values():
                    if n == "x":
                        count = count + 1
        return count

    @classmethod
    def category(cls, level):
        #try:
        if level in ('Twin', 'VVIP', 'VIP', 'Economy'):
            for i in range(len(list(seats[str(level)]))):
                for col, n in seats[str(level)][i][1].items():
                    if n == "x":
                        available_seats.append(
                            str(seats[str(level)][i][0]) + str(col))
                        print(str(seats[str(level)][i][0]) + str(col))

    @classmethod
    def select(cls, selection, num_seats, level):
        count = 0
        x = 0
        selected_seats = 1
        seat_list = []
        Err = False
        for n in available_seats:
            if n == selection:
                seat_list.append(available_seats[count])
                try:
                    while selected_seats < num_seats:
                        seat_list.append(
                            available_seats[count + selected_seats])
                        selected_seats = selected_seats + 1
                except:
                    print("Available seats: None")
                    del seat_list[:]
                    Err = True
            count = count + 1

        if Err is False:
            print(seat_list)
            for value in seat_list:
                for i in range(len(list(seats[str(level)]))):
                    if seats[str(level)][i][0] == seat_list[x][0]:
                        seats[str(level)][i][1][seat_list[x][1:]] = "#"
                x = x + 1
            print("Action Successful")
            print("\n")

    @classmethod
    def reserve_seat(cls, selection, num_seats, level):
        count = 0
        x = 0
        selected_seats = 1
        seat_list = []
        Err = False
        for n in available_seats:
            if n == selection:
                seat_list.append(available_seats[count])
                try:
                    while selected_seats < num_seats:
                        seat_list.append(
                            available_seats[count + selected_seats])
                        selected_seats = selected_seats + 1
                except:
                    print("Available seats: None")
                    del seat_list[:]
                    Err = True
            count = count + 1

        if Err is False:
            print(seat_list)
            for value in seat_list:
                for i in range(len(list(seats[str(level)]))):
                    if seats[str(level)][i][0] == seat_list[x][0]:
                        seats[str(level)][i][1][seat_list[x][1:]] = "o"
                x = x + 1
            print("Action Successful")
            print("\n")

    @classmethod
    def printTable(cls):
        table = {}
        for seat in seats:
            for i in range(len(seats[seat])):
                table[seats[seat][i][0]] = {}
        for seat in seats:
            for i in range(len(seats[seat])):
                for x in table:
                    if seats[seat][i][0] == x:
                        table[x].update(seats[seat][i][1])

        print("\nSeating Chart\n")
        df = pd.DataFrame(table).T
        df.fillna(0, inplace=True)
        print(df)
        print("\n")
        #print(table)
        #print(seats[seat][i][1].values())

        #header = seats[0].keys()
        #rows = [x.values() for x in seats]
        #print("\nSeating Chart")
        #print (tabulate.tabulate(header, header, tablefmt='grid'))