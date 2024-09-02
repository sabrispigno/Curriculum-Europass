# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 20:00:52 2024

@author: sbrin
"""

from fpdf import FPDF

class EuropassCV(FPDF):
    def __init__(self):
        super().__init__()
        self.add_page()
        self.set_auto_page_break(auto=True, margin=8)

    def header(self):
        self.set_font("Arial", "B", 8)
        self.cell(0, 8, "CURRICULUM VITAE", 0, 1, "C")
        self.ln(5)

    def add_photo(self, photo_path, x=10, y=10, width=30):
        self.image(photo_path, x=x, y=y, w=width)
        #self.ln(40)  # Aggiungi uno spazio dopo la foto

    def personal_info(self, name, address, phone, email, birth_date, nationality):
        self.set_font("Arial", "B", 8)
        self.cell(0, 8, "PERSONAL INFORMATION", 0, 1)
        self.set_font("Arial", "", 10)
        self.cell(0, 8, f"Name: {name}", 0, 1)
        self.cell(0, 8, f"Address: {address}", 0, 1)
        self.cell(0, 8, f"Phone: {phone}", 0, 1)
        self.cell(0, 8, f"Email: {email}", 0, 1)
        self.cell(0, 8, f"Date of Birth: {birth_date}", 0, 1)
        self.cell(0, 8, f"Nationality: {nationality}", 0, 1)
        self.ln(8)
        

    def work_experience(self, experiences):
        self.set_font("Arial", "B", 8)
        self.cell(0, 8, "WORK EXPERIENCE", 0, 1)
        self.set_font("Arial", "", 8)
        for exp in experiences:
            self.multi_cell(0, 8, f"{exp['position']} at {exp['company']}\n"
                                    f"From: {exp['start_date']} To: {exp['end_date']}\n"
                                    f"Main activities: {exp['activities']}\n")
            self.ln(5)

    def skills(self, skills):
        self.set_font("Arial", "B", 8)
        self.cell(0, 8, "PERSONAL SKILLS", 0, 1)
        self.set_font("Arial", "", 8)
        for skill, level in skills.items():
            self.cell(0, 8, f"{skill}: {level}", 0, 1)
        self.ln(8)

    def languages(self, languages):
        self.set_font("Arial", "B", 8)
        self.cell(0, 8, "LANGUAGE SKILLS", 0, 1)
        self.set_font("Arial", "", 8)
        for lang, level in languages.items():
            self.cell(0, 8, f"{lang}: {level}", 0, 1)
        self.ln(10)

    def output_cv(self, filename):
        self.output(filename)

# Esempio di utilizzo
if __name__ == "__main__":
    # Creazione del CV
    cv = EuropassCV()

    # Aggiunta della foto (specifica il percorso corretto)
    cv.add_photo("Christian.jpeg", x=160, y=10, width=30)  # Sposta la foto in alto a destra

    # Informazioni personali
    cv.personal_info(
        name="Christian Isaac Guerrero Lopez",
        address="Rampe San Marcellino,5, 80141 Napoli, Italia",
        phone="+39 3518059108",
        email="guerrerolopez.christian@gmail.com",
        birth_date="21/06/02",
        nationality="Messicana"
    )

    # Esperienza lavorativa
    cv.work_experience([
        {
            "position": "Cook",
            "company": "D'Alessandro",
            "start_date": "1/06/2024",
            "end_date": "15/08/2024",
            "activities": "Managing kitchen staff, cooking italian dishes, overseeing food preparation and presentation."
        },
        {
            "position": "Manager",
            "company": "Escape Holbox",
            "start_date": "1/04/2023",
            "end_date": "15/5/2024",
            "activities": "Interaction with suppliers, coordinating the staff work, assistant cook (mexican, italian and worldwide dishes), costumer services"
        },
        {
            "position": "Cook",
            "company": "Maiztro",
            "start_date": "18/12/2022",
            "end_date": "31/03/2023",
            "activities": "Cook specilized in mexican and worldwide dishes, preparing of dough (pizza, pasta, piadine), preparing of sauces, interaction with clients, costumer services."
        },
        {
            "position": "Waither",
            "company": "Custom Rock",
            "start_date": "05/06/2022",
            "end_date": "25/11/2022",
            "activities": "Costumer services, Take command, Menù suggestion, Cleaning of the restaurant"
        },
        {
            "position": "Cook",
            "company": "Buffalucas",
            "start_date": "15/07/2018",
            "end_date": "31/03/2020",
            "activities": "Preparing ingredients, cooking dishes according to recipes, and maintaining cleanliness in the kitchen."
        },
        {
            "position": "Griller",
            "company": "la castellana",
            "start_date": "12/09/2016",
            "end_date": "31/06/2018",
            "activities": "Grilling, Preparing street food dishes (panini, wraps, burgers)"
        }
        
    ])

    # Competenze personali
    cv.skills({
          "Communication": "Excellent",
        "Teamwork": "Advanced",
        "Leadership": "Advanced",
        "Time Management": "Excellent"
    })

    # Lingue
    cv.languages({
        "Spanish": "Native",
        "English": "Good",
        "Italian": "Basic"
    })

    # Esportazione del CV in un file PDF
    cv.output_cv("Europass_CV_Christian1.pdf")
