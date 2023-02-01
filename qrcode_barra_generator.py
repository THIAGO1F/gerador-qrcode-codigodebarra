import png
import pyqrcode
from barcode.writer import ImageWriter
from barcode import EAN13
from PySimpleGUI import PySimpleGUI as sg
from PySimpleGUI import Column, VSeparator
from PIL import Image
class code_barra():
    def menu1(self):
        menu_layout = [
        ['Information',['doubt?']],
        ]
        sg.theme('BrightColors')#LightBrown6
        layout = [[sg.Menu(menu_layout)],
            [sg.Text('                    Informe sua escolha', size=(40,1))],
            [sg.Button('QRcode',size=(10,1)),sg.Button('Codigo de barra'), sg.Button('CANCELAR',size=(10,1))]
        ]
        return sg.Window('GERADOR DE SENHAS', layout=layout, finalize=True,size=(320,80))

    def qrcode(self):
        layout1 = [
            [sg.Image(filename='',key='qrcodeimg')]
        ]
        layout2 = [
            [sg.Text('Nome:',size=(5,1)),sg.Input('',key='nomeqr')],
            [sg.Text('Link:',size=(5,1)),sg.Input('',key='link')],
            [sg.Button('CRIAR',size=(10,1)),sg.Button('VOLTAR',size=(10,1))],
        ]
        layout = [
            [Column(layout1),VSeparator(),Column(layout2)]
        ]
        return sg.Window('QRcode',layout=layout, finalize=True,size=(500,120))

    def criar_qrcode(self):

        nome = self.values['nomeqr']
        link = self.values['link']

        if nome == '':
            sg.popup_auto_close('Nome do produto não pode ser vazio!!')
        if link == '':
            sg.popup_auto_close('O "link/valor" do qrcode não pode ser vazio!!!')

        else:
            cria_code = pyqrcode.create(f'{link}')
            cria_code.png(f'{nome}.png', scale=2)
            sg.popup(f'QRcode criado com sucesso!!\narquivo criado como {nome}.png')
            nome = self.values['nomeqr']
            self.window['qrcodeimg'].update(filename=f'{nome}.png')

    def codigo_barra(self):

        layout = [
            [sg.Text('Nome do Cd Barra: ',size=(13,1)),sg.Input('',key='nome')],
            [sg.Text('Id do Cd Barra: ',size=(13,1)),sg.Input('',key='id_produto')],
            [sg.Button('CRIAR',size=(10,1)),sg.Button('VOLTAR')],
        ]
        return sg.Window('Codigo de barra', layout=layout,finalize=True,size=(280,100))

    def criar_cdbarra(self):
        nome = self.values['nome']
        id_produto = self.values['id_produto']

        num = len(str(id_produto))
        
        if num < 12: 
            sg.popup_auto_close('ID tem quer ser 12 digitos!!!')
        if nome == '':
            sg.popup_auto_close('O nome do produto não pode ser vazio!!')

        else:
            codigo_barra = EAN13(f'{id_produto}', writer=ImageWriter())
            codigo_barra.save(f'{nome}')
            sg.popup_auto_close(f'CRiado com sucesso, {nome}.png')

    def start(self):
        janela1,janela2,janela3,janela4 = self.menu1(),None,None,None
        while True:
            self.window, event, self.values = sg.read_all_windows() 
            #COMANDO PARA SAIR DO PORGRAMA 
            if self.window == janela1 and event == sg.WIN_CLOSED or event == 'CANCELAR':
                break
            if self.window == janela2 and event == sg.WIN_CLOSED or event == 'CANCELAR':
                break
                
            if self.window == janela1:
                if event in 'QRcode':
                    janela1.hide()
                    janela2 = self.qrcode()

                if event in 'Codigo de barra':
                    janela1.hide()
                    janela3 = self.codigo_barra()

            if self.window == janela2:
                if event in 'VOLTAR':
                    janela2.hide()
                    janela1.un_hide()
                if event in 'CRIAR':
                    self.criar_qrcode()
                    

            if self.window == janela3:
                if event in 'VOLTAR':
                    janela3.hide()
                    janela1.un_hide() 
                if event in 'CRIAR':
                    self.criar_cdbarra()
                    
code_barra().start()