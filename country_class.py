'''
This is the class that will contain a country.
'''

class Country:
    '''
    Each country has a population, as well as several other factors that
    describe the country and which will affect how the disease interacts and
    infects the country.
    '''

    __init__(p, t, h, w, u, a, b):
        # the population in the country
        self.population = p

        # this is a temperature multiplier that will be from 0 to 1.
        # 0 is basically antartica and 1 will be the sahara
        self.temperature = t

        # this is the humidity multiplier that will be from 0 to 1.
        # 0 is basically really dry and 1 will be the rainforest
        self.humidity = h

        # this is a measure of the wealth in the country (0 to 1)
        # this determines how effective a disease will be in that country
        # a wealthier country will be less susceptible to disease due to 
        # antibiotics etc
        self.wealth = w

        # this is a measure of how urbanized a country is (0 to 1)
        self.urban = u

        # this is a list of airports
        self.airports = a

        # this is a list of sea ports for boats to leave from
        self.boatports = b


    get_population(self):
        return self.population

    get_temperature(self):
        return self.temperature

    get_humidity(self):
        return self.humidity
    
    get_wealth(self):
        return self.wealth

    get_urban(self):
        return self.urban

    get_airports(self):
        return self.airports

    get_boatports(self):
        return self.boatports
