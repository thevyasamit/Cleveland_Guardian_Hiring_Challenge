import requests
import csv
import schedule
import time

class planetsApi:
    def __init__(self,link)-> None:
        '''
        param: link (string)
        rtype: None
        '''
        try:
            # Making a GET request to the API to retrieve the data
            self.response = requests.get(link)
            self.response.raise_for_status()
        # Handling Exceptions
        except requests.exceptions.HTTPError as err1:
            print(err1)
        except requests.exceptions.ConnectionError as err2:
            print(err2)
        except requests.exceptions.Timeout as err3:
            print(err3)
        except requests.exceptions.RequestException as err4:
            print(err4)
        self.planets = self.response.json()['results']


    def dataCleaning(self) -> None:
        '''
        param: self
        rtype: None
        '''

        #Appending cleaned data in list
        self.cleaned_data = []

        # Using the flag to check if we have reached the end of the pages where data was available.
        flag = 1  
        while flag:

        # Iterate over the planets
            try:
                for planet in self.planets:
                    # Checking if the planet has values for diameter, gravity, climate, and population
                    if all(value in planet.keys() for value in ['diameter', 'gravity', 'climate', 'population']):

                        # Checkingif the values are not missing or unknown
                        if all(planet[value] not in ['unknown', 'n/a'] for value in ['diameter', 'gravity', 'climate', 'population']):
                            self.cleaned_data.append([planet['name'], planet['diameter'], planet['gravity'], planet['climate'], planet['population']])
                
                url = self.response.json()['next']
                self.response = requests.get(url)
                self.planets = self.response.json()['results']

                if self.response.json()['next'] == None:
                    flag = 0
            except Exception as e:
                print(e.message, e.args)

    def writeCsv(self)-> None:        
        '''
        param: self
        rtype: None
        '''

        # Writing the cleaned data to a csv file
        try:
            with open('planets.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Name', 'Diameter', 'Gravity', 'Climate', 'Population'])
                writer.writerows(self.cleaned_data)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    obj = planetsApi('https://swapi.dev/api/planets/')
    obj.dataCleaning()
    obj.writeCsv()


'''
If more planets were added to the API, this code would still work without issue. 
The API's next property would allow the script to iterate through all pages of the API until the next property is null.
'''

