#!/bin/python3

import math
def check_constraint(allLocations, numDeliveries):
    if numDeliveries <= len(allLocations):
        return allLocations      
    
def get_closest_location(loc_list, current_loc):
    new_list = []
    for x,y in loc_list:
        distance = math.sqrt(x**2 + y**2) - math.sqrt(current_loc[0] ** 2 + current_loc[1] ** 2)
        new_list.append(([x,y],distance))
    return sorted(new_list, key=lambda tup:tup[1])
        

def deliveryPlan(allLocations, numDeliveries):
    # this one can be done directly using return filter_by_constraint(allLocations, numDeliveries) 
    # i added it just for readability 
    print('Develery plan ', allLocations)
    print('num develeries', numDeliveries)
    delivery_list = []
    current_loc = [0,0]
    if check_constraint(allLocations, numDeliveries):
        for i in range(len(allLocations)):
            couple =  get_closest_location(allLocations, current_loc)[0]
            current_loc = couple
            delivery_list.append(couple)
            allLocations.remove(couple)
    print('this what we gonna deliver',delivery_list[:numDeliveries])
    return delivery_list[:numDeliveries]

