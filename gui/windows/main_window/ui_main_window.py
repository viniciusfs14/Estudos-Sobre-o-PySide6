from qt_core import *
from gui.pages.ui_pages import Ui_aplication_pages

class UI_MainWindow(object):
    def setup_ui(self, parent):
        if not parent.objectName():
            parent.setObjectName("MainWindow")
            
        #parametros iniciais    
        parent.resize(1200, 720) #tamanho padrão da janela
        parent.setMinimumSize(960, 540) #tamanho minimo da janela
        
        #Cria um widget central
        self.central_frame = QFrame()
        
        #Cria o layout principal
        self.main_layout = QHBoxLayout(self.central_frame) #frame na horizontal
        #self.main_layout = QVBoxLayout(self.central_frame) #frame na vertical
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_layout.setSpacing(0)
        
        #########################################################################################################################
        #Menu Esquerdo
        
        self.left_menu = QFrame()
        self.left_menu.setStyleSheet("background-color: #44475a")
        self.left_menu.setMinimumWidth(50) #tamanho minimo de largura
        self.left_menu.setMaximumWidth(50) #tamanho maximo de largura
        #self.left_menu.setMaximumHeight(50) #tamanho maximo de altura
        
        # label Menu esquerdo
        self.left_menu_layout = QVBoxLayout(self.left_menu)
        self.left_menu_layout.setContentsMargins(0,0,0,0)
        self.left_menu_layout.setSpacing(0)
        
        # Frame superior do menu
        self.left_menu_top_frame = QFrame()
        self.left_menu_top_frame.setMinimumHeight(40)
        self.left_menu_top_frame.setObjectName("left_menu_top_frame")
        
        # Layout frame superior
        self.left_menu_top_layout = QVBoxLayout(self.left_menu_top_frame)
        self.left_menu_top_layout.setContentsMargins(0,0,0,0)
        self.left_menu_top_layout.setSpacing(0)
        
        # Botões superiores
        self.toggle_button = QPushButton("Menu")
        self.toggle_button.setStyleSheet("color: white")
        self.button1 = QPushButton("1")
        self.button1.setStyleSheet("color: white")
        self.button2 = QPushButton("2")
        self.button2.setStyleSheet("color: white")
        
        # Adicionar os botões no layout
        self.left_menu_top_layout.addWidget(self.toggle_button)
        self.left_menu_top_layout.addWidget(self.button1)
        self.left_menu_top_layout.addWidget(self.button2)
        
        # Espaçador do menu
        self.left_menu_spacer = QSpacerItem(20, 20, QSizePolicy.Minimum, QSizePolicy.Expanding)
        
        # Frame inferior do menu
        self.left_menu_bottom_frame = QFrame()
        self.left_menu_bottom_frame.setMinimumHeight(50)
        self.left_menu_bottom_frame.setObjectName("left_menu_bottom_frame")
        
        self.left_menu_bottom_layout = QVBoxLayout(self.left_menu_bottom_frame)
        self.left_menu_bottom_layout.setContentsMargins(0,0,0,0)
        self.left_menu_bottom_layout.setSpacing(0)
        
        # Botão inferior
        self.settings_button = QPushButton("Settings")
        self.settings_button.setStyleSheet("color: white")
        
        # Adicionar os botões no layout
        self.left_menu_bottom_layout.addWidget(self.settings_button)
        
        # Versão da Label
        self.left_menu_label_version = QLabel("v1.0.1")
        self.left_menu_label_version.setStyleSheet("color: #c3ccdf")
        self.left_menu_label_version.setAlignment(Qt.AlignCenter)
        self.left_menu_label_version.setMaximumHeight(30)
        self.left_menu_label_version.setMinimumHeight(30)
        
        # Adicionar no layout
        self.left_menu_layout.addWidget(self.left_menu_top_frame)
        self.left_menu_layout.addItem(self.left_menu_spacer)
        self.left_menu_layout.addWidget(self.left_menu_bottom_frame)
        self.left_menu_layout.addWidget(self.left_menu_label_version)
        
        #Conteúdo
        self.content = QFrame()
        self.content.setStyleSheet("background-color: #282a36")
        
        #Layout do Conteúdo
        self.content_layout = QVBoxLayout(self.content)
        self.content_layout.setContentsMargins(0,0,0,0)
        self.content_layout.setSpacing(0)
        
        ###############################################################################################################
        #Barra de cima
        
        self.top_bar = QFrame()
        self.top_bar.setMinimumHeight(30)
        self.top_bar.setMaximumHeight(30)
        self.top_bar.setStyleSheet("background-color: #21232d; color: 6272a4")
        self.top_bar_layout = QHBoxLayout(self.top_bar)
        self.top_bar_layout.setContentsMargins(10,0,10,0)
        
        #coluna da esquerda
        self.top_label_left = QLabel("PYDAQ")
        self.top_label_left.setStyleSheet("font: 700 9pt 'Segoe UI'; color: white")
        
        #espaçador de cima
        self.top_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        
        #coluna da direita
        self.top_label_right = QLabel("| PÁGINA INICIAL")
        self.top_label_right.setStyleSheet("font: 700 9pt 'Segoe UI'; color: white")
        
        #Adicionar no layout
        self.top_bar_layout.addWidget(self.top_label_left)
        self.top_bar_layout.addItem(self.top_spacer)
        self.top_bar_layout.addWidget(self.top_label_right)
        
        #Páginas da aplicação
        self.pages = QStackedWidget()
        self.pages.setStyleSheet("font-size: 12pt; color: white") #se eu quiser adicionar uma cor de fundo, basta adicionar o background-color: alguma cor
        self.ui_pages = Ui_aplication_pages()
        self.ui_pages.setupUi(self.pages)       

        ###############################################################################################################
        #Barra de baixo
        
        self.bottom_bar = QFrame()
        self.bottom_bar.setMinimumHeight(30)
        self.bottom_bar.setMaximumHeight(30)
        self.bottom_bar.setStyleSheet("background-color: #21232d; color: 6272a4")
        self.bottom_bar_layout = QHBoxLayout(self.bottom_bar)
        self.bottom_bar_layout.setContentsMargins(10,0,10,0)
        
        #coluna da esquerda
        self.bottom_label_left = QLabel("Criado por: Vinícius Fernandes")
        self.bottom_label_left.setStyleSheet("font: 700 9pt 'Segoe UI'; color: white")
    
        #espaçador de cima
        self.bottom_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
    
        #coluna da direitas
        self.bottom_label_right = QLabel("2024")
        self.bottom_label_right.setStyleSheet("font: 700 9pt 'Segoe UI'; color: white")
    
        ###############################################################################################################
        
        #Adicionar no layout
        self.bottom_bar_layout.addWidget(self.bottom_label_left)
        self.bottom_bar_layout.addItem(self.bottom_spacer)
        self.bottom_bar_layout.addWidget(self.bottom_label_right)
        
        #Adicionar no Layout do Conteúdo
        self.content_layout.addWidget(self.top_bar)
        self.content_layout.addWidget(self.pages)
        self.content_layout.addWidget(self.bottom_bar)
        
        #Adicionar os widgets no app
        self.main_layout.addWidget(self.left_menu)
        self.main_layout.addWidget(self.content)
        
        
        #Seta o widget central
        parent.setCentralWidget(self.central_frame)