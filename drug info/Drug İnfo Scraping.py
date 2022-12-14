import imp
from logging import exception
import string
from tkinter import N
from unicodedata import category, name
from attr import attr, attrs
import click
from pyparsing import identbodychars
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import json
from pprint import pprint

class MedlineScraper:
    def __init__(self):
        self.base_url="https://medlineplus.gov/druginfo"
        self.drug_links=set()


    def get_categories(self):
        letters=string.ascii_uppercase
        result= list(map(lambda letter:self.base_url +"/drug_{}a.html".format(letter),letters))
        result.append("https://medlineplus.gov/druginfo/drug_00.html")
        return result
    
    def get_source(self,url):
        r=requests.get(url)
        if r.status_code==200:
            return BeautifulSoup(r.content,"lxml")
        return False

    def get_drug_links(self,source):
        drug_elements=source.find("ul",attrs={"id":"index"}).find_all("li")
        drug_links=list(map(lambda drug:self.base_url+drug.find("a").get("href").replace(".","",1),drug_elements))
        return set(drug_links)

    
    def find_all_drug_links(self):
        categories=self.get_categories()
        bar=tqdm(categories,unit="category link")
        for category_link in bar:
            bar.set_description(category_link)
            category_source=self.get_source(category_link)
            result=self.get_drug_links(category_source)
            self.drug_links=self.drug_links.union(result)

        return self.drug_links

    def get_name(self,source):
        try:
            return source.find("h1",attrs={"class":"with-also"}).text
        except Exception:
            return None

    def get_section_info(self,source,id_element):
        try:
           title= source.find("div",attrs={"id":id_element}).find("h2").text
           content=source.find("div",attrs={"id":id_element}).find("div",attrs={"class":"section-body"}).text
           return dict(
                title=title,
                content=content
            )
        except Exception:
            return None

    def scrape_drugs(self):      
        result=list()
        links=self.find_all_drug_links()
        bar=tqdm(links,unit="drug link")
        for link in bar:
            sections=list()
            bar.set_description(link)
            drug_source=self.get_source(link)
            name=self.get_name(drug_source)
            why=self.get_section_info(drug_source,"why")
            sections.append(why)            
            how=self.get_section_info(drug_source,"how")
            sections.append(how)
            other_uses=self.get_section_info(drug_source,"other-uses")
            sections.append(other_uses)            
            result.append(dict(
                name=name,
                url=link,
                section=sections
                
            ))
        return result

    def write_as_json(self,data,filename="result.json"):
        with open(filename,"w",encoding="utf-8") as f:
            f.write(json.dumps(data,indent=2))
            
if __name__=="__main__":


        scraper=MedlineScraper()
        data=scraper.scrape_drugs()
        #source=scraper.get_source("https://medlineplus.gov/druginfo/drug_Aa.html")
        #drugs=scraper.get_drug_links(source)
        scraper.write_as_json(data)