from train import *

def test_TrainClass():
    '''
    tests Train class and inherited classes
    '''
    print('Testing Train class...')
    # Train has it's own number and capacity
    train = Train(1522, 250)
    assert str(train) == "The train № 1522 has a capacity of 250 people. \
It's ticket costs ... It has no destination yet."

    # We can set a cost of ticket for a train
    train.set_cost_of_ticket(180)
    # We can view what cost we set
    assert train.view_ticket_cost() == 180
    assert str(train) == "The train № 1522 has a capacity of 250 people. \
It's ticket costs 180 UAH. It has no destination yet."

    # Same with destination
    # We can set a destination for our train
    train.set_destination('Lviv-Kharkiv')
    # We can view what destination we set
    assert train.view_destination() == 'Lviv-Kharkiv'
    assert str(train) == "The train № 1522 has a capacity of 250 people. \
It's ticket costs 180 UAH. It's destination is 'Lviv-Kharkiv'."

    # We can also remove a cost of ticket
    train.remove_cost_of_ticket()
    try:
        train.view_ticket_cost()
    except UnknownCost as error:
        assert str(error) == "The train's № 1522 ticket cost is not defined yet."

    assert str(train) == "The train № 1522 has a capacity of 250 people. \
It's ticket costs ... It's destination is 'Lviv-Kharkiv'."
    # We can also remove a destination
    train.remove_destination()
    try:
        train.view_destination()
    except UnknownDestination as error:
        assert str(error) == "The train's № 1522 destination is not defined yet."


    # We also have passangers of our train
    passag_1 = Passanger('Alex')
    # We must validate whether the name of a passanger is set correctly
    # There must not be any digits or special characters
    assert Passanger.validate_name('Alex') is True
    assert Passanger.validate_name('Alex123') is False
    assert Passanger.validate_name('Al_ex') is False
    # Every passanger has his/her own sum of money. This attribute is private
    # But we can easily see how much money do we have because of property :)
    passag_1 = Passanger('Alex', 500)
    assert passag_1.money == 500

    # We can add passangers to our train(but we can not do it now)
    assert train.add_passanger(passag_1) == 'Passanger Alex does not have a ticket.'

    # Passanger must buy a ticket for a train
    assert train.buy_ticket(passag_1) == 'The cost of the ticket is not defined.'

    # We must set a price for ticket to buy it. Let's set a ticket, which is very expensive
    train.set_cost_of_ticket(800)
    assert train.buy_ticket(passag_1) == \
'Passanger Alex does not have enough money to buy a ticket.'

    train.set_cost_of_ticket(300)
    train.buy_ticket(passag_1)
    # The sum of money of our passanger must have changed
    assert passag_1.money == 200

    # Now we can add Alex to our train
    train.add_passanger(passag_1)
    # We can also view what passangers are on the train
    assert train.view_passangers() == "Passangers on the train :['Alex']"
    # Let's try to remove a passanger
    passag_2 = Passanger('Marko', 800)
    assert train.remove_passanger(passag_2) == 'Passanger Marko is not on the train.'
    train.remove_passanger(passag_1)
    assert train.view_passangers() == 'Passangers on the train :[]'

    # We also have another type of train - Coupe Train
    coupe_1 = CoupeTrain(4158, 340)
    # We can see how many coupe trains we have.
    assert CoupeTrain.coupe_count == 1

    # If the coupe train starts moving, you can not exit it
    coupe_1.start_moving()
    assert coupe_1.exit(passag_1) == 'Passanger Alex is not on the train.'
    coupe_1.add_passanger(passag_1)
    assert coupe_1.view_passangers() == "Passangers on the train :['Alex']"
    assert coupe_1.exit(passag_1) == 'Passanger Alex can not exit the train, \
because it is currently moving.'
    coupe_1.stop_moving()
    coupe_1.exit(passag_1)
    assert coupe_1.view_passangers() == 'Passangers on the train :[]'

    # We can compare coupe trains
    coupe_2 = CoupeTrain(num=1234, cap=50)
    coupe_3 = CoupeTrain(num=2678, cap=50)
    coupe_4 = CoupeTrain(num=1234, cap=50)
    coupe_5 = CoupeTrain(num=1234, cap=100)
    assert coupe_2 == coupe_4  # same number and capacity
    assert coupe_2 != coupe_3  # different number and same capacity
    assert coupe_2 != coupe_5  # same number and different capacity

    assert CoupeTrain.coupe_count == 5
    # Travel Train is a mix of Train and CoupeTrain
    travel_train = TravelTrain(3567, 300)
    assert travel_train.add_passanger(passag_2) == 'Passanger Marko does not have a ticket.'
    travel_train.set_cost_of_ticket(600)
    travel_train.buy_ticket(passag_2)
    travel_train.add_passanger(passag_2)
    assert travel_train.view_passangers() == "Passangers on the train :['Marko']"
    travel_train.start_moving()
    assert travel_train.exit(passag_2) == "Passanger Marko can not exit the train, \
because it is currently moving."
    travel_train.stop_moving()
    assert travel_train.remove_passanger(passag_1) == 'Passanger Alex is not on the train.'
    travel_train.remove_passanger(passag_2)
    assert travel_train.view_passangers() == "Passangers on the train :[]"

    # Travel Train is also special because
    # at each stop you can buy a souvenir
    # Passanger can not buy souvenir, when the train is moving
    travel_train.start_moving()
    assert travel_train.buy_souvenirs(passag_1) == 'Passanger Alex is not on the train.'
    travel_train.set_cost_of_ticket(100)
    travel_train.buy_ticket(passag_1)
    travel_train.add_passanger(passag_1)
    assert travel_train.buy_souvenirs(passag_1) == \
"Passanger Alex can not buy souvenirs, because the train is moving."
    travel_train.stop_moving()
    assert travel_train.buy_souvenirs(passag_1) == 'Passanger Alex successfully bought a souvenir.'

    # A railway station has a lot of trains
    railway_station = set()
    assert travel_train not in railway_station
    railway_station.add(travel_train)
    assert travel_train in railway_station
    assert coupe_1 not in railway_station
    railway_station.add(coupe_1)
    assert coupe_1 in railway_station
    print('Done!')
test_TrainClass()