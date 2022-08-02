from importlib.resources import path
import xml.etree.ElementTree as ET
import os
import pathlib
from tkinter import *
from tkinter import messagebox

from requests import delete



class Tela:
    def __init__(self, root):
        #Frames
        self.label_frame = Frame(root)
        self.label_frame.pack(side=LEFT)

        self.entry_frame = Frame(root)
        self.entry_frame.pack(side=LEFT)

        self.lista_frame = Frame(root)
        self.lista_frame.pack(side=RIGHT, fill='x')
        
        

        #TextBox
        self.lista_label = Label(self.lista_frame, text='Sequencia', font=('Arial',15))
        self.lista_label.pack()

        self.lista_button = Button(self.lista_frame, text='Ativar')
        self.lista_button.pack(side=BOTTOM)

        self.lista_text = Text(self.lista_frame, width=140, height=10)
        self.lista_text.pack(padx=10, pady=10, side=BOTTOM) 

        #Labels
        self.cnf_label = Label(self.label_frame, text='cNF')
        self.cnf_label.pack(pady=10)

        self.chave_label = Label(self.label_frame, text='Chave')
        self.chave_label.pack(pady=10)

        self.data_label = Label(self.label_frame, text='Data')
        self.data_label.pack(pady=10)

        self.valor_label = Label(self.label_frame, text='Valor')
        self.valor_label.pack(pady=10)

        #Entrys
        self.cnf_entry = Entry(self.entry_frame)
        self.cnf_entry.bind('<Return>', lambda event: self.VerificarNumByEntry())
        self.cnf_entry.pack(pady=11)

        self.chave_entry = Entry(self.entry_frame)
        self.chave_entry.pack(pady=11)

        self.data_entry = Entry(self.entry_frame)
        self.data_entry.pack(pady=11)

        self.valor_entry = Entry(self.entry_frame)
        self.valor_entry.pack(pady=11)

        #self.VerificarNum(['494791'])



    def Verifica(self, root):
        self.chave_entry.delete(0, END)
        self.data_entry.delete(0, END)
        self.valor_entry.delete(0, END) 

        cod = root.find('.//cNF').text

        #self.cnf_entry.insert(0, cod)


        chave = root.find('.//infCFe').attrib['Id']
        chave = chave[3:]

        self.chave_entry.insert(0, chave)


        data = root.find('.//dEmi').text
        dia = data[-2:]
        mes = data[4:-2]
        ano = data[:4]
        brdata = f'{dia}.{mes}.{ano}'

        self.data_entry.insert(0, brdata)


        valor = root.find('.//vMP').text

        self.valor_entry.insert(0, valor)

        sql = f"INSERT INTO sat_vendas (cod,chave,data,valor), VALUES({cod},{chave},{brdata},{valor})"
        print(sql)

    def VerificarNumByEntry(self):
        PATH = pathlib.Path(__file__).parent.resolve()
        for i in os.listdir(f'{PATH}/202206'):
            tree = ET.parse(f'{PATH}/202206/{i}')
            root = tree.getroot()
            data = root.find('.//cNF').text
            if data == self.cnf_entry.get():
                self.Verifica(root)
                return True
        
        messagebox.showerror("Erro", "Nenhum Valor Encontrado!")

    def VerificarNumByEntry(self):
        PATH = pathlib.Path(__file__).parent.resolve()
        for i in os.listdir(f'{PATH}'):
            if i[-3:] == 'xml':
                tree = ET.parse(f'{PATH}/{i}')
                root = tree.getroot()
                data = root.find('.//cNF').text
                if data == self.cnf_entry.get():
                    self.Verifica(root)
                    return True
        
        messagebox.showerror("Erro", "Nenhum Valor Encontrado!")





root = Tk()
root.title('XML SAT Finder')
Tela(root)
root.mainloop()