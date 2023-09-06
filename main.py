# write your code here
def padel_court_cost (court_type):
    if court_type == 'indoor':
        return 30
    elif court_type == 'outdoor':
        return 20
    
def recket_cost(recket_brand):

    if recket_brand=='bullpadel':
        return 100
    elif recket_brand=='nox':
        return 140
    elif recket_brand=='siux':
        return 200

def padel_balls_cost(ball_bouxes):
    if ball_bouxes== 1:
        return 2
    elif ball_bouxes== 2:
        return 3.5
    elif ball_bouxes==3:
        return 5 
    
    def padel_game_cost ():

        court_type= (input('court type indoor:\ outdoor\n'))
        recket_brand=(input('racket brand: nox \ siux \ bull \ n'))
        bell_boxes=int(input('number of bell boxes:1 \ 2( \ 3\n'))
        price:padel_court_cost(court_type) + recket_cost(recket_brand)+ padel_balls_cost(ball_bouxes)
    
    print(padel_game_cost())