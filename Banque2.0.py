# coding=utf-8
from tkinter import *

compte = open('fichier.rtf', 'r')
lst = []
for lig in compte:
    lst.append(int(lig))
argent = lst[0]


class Interface(Frame):
    def valide_income(self):
        # print(argent+var_texte)
        print("First Name: %s" % (ligne_texte.get()))

    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, **kwargs)
        self.pack(fill=BOTH)
        champ_label = Label(fenetre, text="bienvenue dans votre banque")
        champ_label.pack()
        fenetre.geometry("700x500")

        income = Button(fenetre, text="income", command=self.income)
        income.pack()

        outcome = Button(fenetre, text="outcome", command=self.outcome)
        outcome.pack()
        champ_label1 = Label(fenetre, text="Vous avez  {} €.".format(argent))
        champ_label1.pack()

    def income(self):
        champ_label = Label(fenetre, text='combien avez vous gagné?')
        champ_label.pack()

        ligne_texte = Entry(fenetre)
        ligne_texte.pack()

        valide = Button(fenetre, text="valider", command=self.valide_income)
        valide.pack()

    def outcome(self):
        outcomeF = Tk()
        champ_label = Label(outcomeF, text='combien avez vous depensé?')
        champ_label.pack()


fenetre = Tk()
interface = Interface(fenetre)
interface.mainloop()
