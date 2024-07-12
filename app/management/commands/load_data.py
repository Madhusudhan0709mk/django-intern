import json 
from django.core.management.base import BaseCommand

from app.models import DataEntry

class Command(BaseCommand):
    help = 'LOAD DATA FROM JSON FILE'
    
    def handle(self,*args,**kwargs):
        with open(r'C:\\Users\\madhu\\Desktop\\PROJECTS\\completed\\djangoblackcoffer_11072024\\jsondata.json', encoding='utf-8') as file:

         data = json.load(file)
        for entry in data:
            try:
                intensity = entry.get("intensity", 1)
                
                if not intensity:
                    intensity = 1 
                
                
                if 'likelihood' not in entry or 'relevance' not in entry or 'country' not in entry or 'region' not in entry:
                    raise KeyError("Required fields are missing in entry")

                # Convert likelihood to integer if it's a valid number
                try:
                    likelihood = int(entry['likelihood'])
                    relevance = float(entry['relevance'])
                except ValueError:
                    likelihood = 0
                    relevence = 0.0
                DataEntry.objects.create(
                    intensity=intensity,  # Default to 1 if 'intensity' key is missing or empty
                    likelihood=likelihood,
                    relevance=relevance,
                    year=entry.get('year', 1999),  # Default to 1999 if 'year' key is missing
                    country=entry['country'],
                    topics=entry.get('topics', []),  # Default to empty list if 'topics' key is missing
                    region=entry['region'],
                    city=entry.get('city', 'Unknown')  # Default to 'Unknown' if 'city' key is missing
                )
            except KeyError as e:
                print(f"Error creating DataEntry: Missing key - {e}")
            except ValueError as e:
                print(f"Error creating DataEntry: {e}")
            except Exception as e:
                print(f"Error creating DataEntry: {e}")
            except json.JSONDecodeError as e:
                print(f"Error decoding JSON: {e}")