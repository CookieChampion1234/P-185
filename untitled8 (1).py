from tkinter import * 
import requests
import json

root=Tk()
root.title("Country Api")

root.geometry("500x600")
root.configure(background="lightslateblue")

city_name_label=Label(root, text="Capital City Name",font=("Helvetica", 18,'bold'))
city_name_label.place(relx=0.5,rely=0.15,anchor = CENTER)

city_entry=Entry(root)
city_entry.place(relx=0.5,rely=0.25,anchor=CENTER)

country_name_label=Label(root, text="Capital:")
country_name_label.place(relx=0.5,rely=0.45,anchor = CENTER)

region_name_label=Label(root, text="Region:")
region_name_label.place(relx=0.5,rely=0.55,anchor = CENTER)

language_name_label=Label(root, text="Language:")
language_name_label.place(relx=0.5,rely=0.65,anchor = CENTER)

population_name_label=Label(root, text="Population:")
population_name_label.place(relx=0.5,rely=0.75,anchor = CENTER)

area_name_label=Label(root, text="Area:")
area_name_label.place(relx=0.5,rely=0.85,anchor = CENTER)

def city_details():
    api_request = requests.get("https://restcountries.eu/rest/v2/capital/" + city_entry.get())
    
    api_output_json = json.loads(api_request.content)
    
    country=api_output_json[0]['name']
    print(country)
    
    reg = api_output_json[0]['region']
    print(reg)
    
    lang = api_output_json[0]['languages'][0]['name']
    print(lang)
    
    popn = api_output_json[0]['population']
    print(popn)
    
    country_area = api_output_json[0]['area']
    print(country_area)
    
    country_name["text"] = "Country:" + country 
    region_name["text"] = "Region:" + reg 
    language_name["text"] = "Language:" + lang 
    population_name["text"] = "Population:" + str(popn)
    area_name["text"] = "Area:" + str(country_area)
    
detail_btn=Button(root, text="City Detail",bg="yellow",command=city_details, relief=FLAT)
detail_btn.place(relx=0.5,rely=0.35,anchor=CENTER)

root.mainloop()

