#https://limewire.com/d/68099683-5270-4768-b464-670f7e531393#KmOV20N-Ehuyw8j45fZNel75Xkj4WtVegSCb6by-gBo


from kivymd.uix.list import MDList
from kivymd.uix.backdrop.backdrop import MDBoxLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.image import Image, AsyncImage, CoreImage
from kivymd.app import MDApp
from kivymd.uix.label import MDLabel
from kivy.uix.label import Label
from kivymd.uix.button import MDIconButton, MDFlatButton, MDFloatingActionButton, MDTextButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.progressbar import MDProgressBar
from kivymd.uix.list import IconLeftWidget, TwoLineAvatarListItem, OneLineAvatarListItem
from kivymd.uix.card import MDCard
from kivymd.toast import toast
from kivy.core.window import Window
from kivy.utils import platform
from kivymd.uix.pickers.datepicker.datepicker import MDTextField
import webbrowser
from kivy.core.clipboard import Clipboard
from kivymd.uix.bottomsheet import MDGridBottomSheet
from kivymd.uix.taptargetview import MDTapTargetView
from kivymd.uix.spinner import MDSpinner
from kivy.storage.jsonstore import JsonStore
from kivy.loader import Loader
from kivy.metrics import dp
from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.menu import MDDropdownMenu
from kivy.clock import Clock
from kivy.network.urlrequest import UrlRequest
import threading
import requests
import base64
from kivy.storage.jsonstore import JsonStore
import os
from pyDes import *
from kivymd.uix.list import OneLineAvatarIconListItem, MDList, IconLeftWidget, TwoLineAvatarIconListItem
import json
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.button import MDRaisedButton
from kivy.uix.screenmanager import Screen, ScreenManager,FadeTransition
from kivymd.uix.filemanager.filemanager import FitImage
#from kivymd.uix.screenmanager import MDScreen
import time
from kivy.uix.image import Image
from kivy.uix.popup import Popup
from kivy.core.window import Window
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.relativelayout import MDRelativeLayout
from kivymd.uix.filemanager import MDFileManager
from datetime import datetime
from kivymd.uix.slider import MDSlider
import firebase_admin
from firebase_admin import credentials, db
from pyfcm import FCMNotification
from firebase import firebase
from plyer import notification

from jnius import autoclass



firebase = firebase.FirebaseApplication("https://chat-app-d2935-default-rtdb.firebaseio.com/", None)

FIREBASE_URL = "https://chat-app-d2935-default-rtdb.firebaseio.com/chat.json"



import socketio


if platform == 'android':
    import android
 #   from android.permissions import request_permissions, Permission, check_permission
#    request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])
    from plyer import notification
    from jnius import autoclass
    MediaPlayer = autoclass('android.media.MediaPlayer')
    AudioManager = autoclass('android.media.AudioManager')

store = JsonStore("user_detail.json")

album_details_base_url = "https://www.jiosaavn.com/api.php?__call=content.getAlbumDetails&_format=json&cc=in&_marker=0%3F_marker=0&albumid="

lyrics_base_url = "https://www.jiosaavn.com/api.php?__call=lyrics.getLyrics&ctx=web6dot0&api_version=4&_format=json&_marker=0%3F_marker%3D0&lyrics_id="
    
search_base_url = "https://www.jiosaavn.com/api.php?__call=autocomplete.get&_format=json&_marker=0&cc=in&includeMetaTags=1&query="

homedata = "www.jiosaavn.com/api.php?_format=json&_marker=0&api_version=4&ctx=web6dot0__call=webapi.getLaunchData"

song_details_base_url = "https://www.jiosaavn.com/api.php?__call=song.getDetails&cc=in&_marker=0%3F_marker%3D0&_format=json&pids="
playlist_details_base_url = "https://www.jiosaavn.com/api.php?__call=webapi.get&token={}&type=playlist&p=1&n=20&includeMetaTags=0&ctx=web6dot0&api_version=4&_format=json&_marker=0"

json_path = os.path.join(os.path.dirname(__file__), "service_account.json")

cred = credentials.Certificate(json_path)
firebase_admin.initialize_app(cred, {"databaseURL": "https://chat-app-d2935-default-rtdb.firebaseio.com/"})


KV = '''

#:import SliverToolbar __main__.SliverToolbar
#: import WipeTransition kivy.uix.screenmanager.WipeTransition
#: import get_color_from_hex kivy.utils.get_color_from_hex
#:import SliverTool __main__.SliverTool

MDFloatLayout:
    MDNavigationLayout:
        ScreenManager:
            id: screen_manager
            
            
            MDScreen:
                MDLabel:
                    text: "Loading Message Please Wait A Second"
                    bold: True
                    halign:"center"
                    
            MDScreen:
                name:"user_detail"
                MDCard:
                    size_hint: None, None
                    pos_hint:{"center_x":.5,"center_y": .84}
                    size_hint: 0.9,.07
                    elevation: 2
                    radius: [25,]
                    border_radius: 4
                        
                    TextInput:
                        id: user
                        hint_text: "Enter Your Username"
                        helper_text: "Please Enter Correct Username"
                        size_hint: .7,None
                        mode: "fill"
                        pos_hint:{"center_x": .45,"center_y": .5}
                        height: self.minimum_height
                        multiline: False
                        cursor_color: 0,0,0,1
                        cursor_width:"2sp"
                        background_color: 0,0,0,0
                        padding: 15
                        font_size: "18sp" 
                        normal_color: app.theme_cls.bg_light
                        color_active: app.theme_cls.bg_light
                        icon_left: "magnify"
                        foreground_color: app.theme_cls.secondary_text_color
        
                                    
                    MDIconButton:
                        id: clo
                        icon: "magnify"
                        pos_hint:{"center_x":.85,"center_y":.5}
                        on_release:app.clear()
                        
                MDRaisedButton:
                    text: "Log In"
                    halign: "center"
                    on_release: app.save()
            
            MDScreen:
                name:"home"

                MDBottomNavigation:
                    MDBottomNavigationItem:
                        id:home
                        name: "screen 1"
                        text:"Home"
                        icon:"home"
                        badge_icon:""
                        
                        MDIconButton:
                            icon: 'menu'
                            pos_hint: {"center_x":0.05, "center_y":0.95}
                            on_press: nav_drawer.set_state("open")
                        MDRelativeLayout:
                            size_hint:.09,.11
                            pos_hint:{"center_x":.13,"center_y":.978}
                            radius:15
                            FitImage:
                                source:"topbarlogo.png"
                                size_hint: None,None 
                                size: "50dp","50dp"
                                
                        MDRelativeLayout:
                            size_hint:.4,.11
                            pos_hint:{"center_x":.455,"center_y":.954}
        
                            MDLabel:
                                text: "Ghost Comm"
                                bold:True
                                font_size: "20sp"
                                pos_hint: {"center_x":.37,"center_Y":.08}
        
                        
        
                        
        
                        MDRelativeLayout:
                            size_hint:.4,.11
                            pos_hint:{"center_x":.84,"center_y":.97}
                                
                            MDIconButton:
                                icon: "bell"
                                pos_hint: {"center_x":.77,"center_Y":.5}
                                theme_icon_size: "Custom"
                                icon_size:"35dp"
                                
                        
                                
                        MDCard:
                            size_hint: None, None
                            pos_hint:{"center_x":.5,"center_y": .87}
                            size_hint: 0.9,.07
                            elevation: 2
                            radius: [60,]
                            border_radius: 4
                            
                            MDIconButton:
                                icon: "magnify"
                                pos_hint:{"center_x":.85,"center_y":.5}
        
                            TextInput:
                                id: profile_search
                                hint_text: "Search Profile ..."
                                helper_text: "Please Enter Correct Username"
                                size_hint: .7,None
                                mode: "fill"
                                pos_hint:{"center_x": .45,"center_y": .5}
                                height: self.minimum_height
                                multiline: False
                                cursor_color: 0,0,0,1
                                cursor_width:"2sp"
                                background_color: 0,0,0,0
                                padding: 15
                                font_size: "18sp" 
                                normal_color: app.theme_cls.bg_light
                                color_active: app.theme_cls.bg_light
                                icon_left: "magnify"
                                foreground_color: app.theme_cls.secondary_text_color
        
                                    
                            MDIconButton:
                                id: clo
                                icon: "magnify"
                                pos_hint:{"center_x":.85,"center_y":.5}
                                on_release:app.clear()
                                        
                            
                                        
        
                        ScrollView:
                            size_hint:1,.82
                            MDBoxLayout:
                                orientation: "vertical"
                                size_hint_y: None
                                height: self.minimum_height
                                spacing: dp(10)
                                padding: dp(10)
                                
        
                                ScrollView:
                                    do_scroll_x: True
                                    do_scroll_y: False
                                    size_hint_y: None
                                    height: "120dp"
                                    bar_width:0
        
                                    MDBoxLayout:
                                        id: story_grid
                                        orientation: "horizontal"
                                        size_hint_x: None
                                        width: self.minimum_width
                                        spacing: dp(10)
                                        padding: dp(10)
                                       
                                            
                                        Image:
                                            source:"topbarlogo.png"
                                            size_hint: None,None
                                            size: "95dp", "95dp"
        
                                        Image:
                                            source:"topbarlogo.png"
                                            size_hint: None,None
                                            size: "95dp", "95dp"
        
                                        
                                
                                MDList:
                                    divider: "Inset"
                                    divider_color:1,1,1,1
                                    radius: [25,0,0,0]
                                    ThreeLineAvatarIconListItem:
                                        id:home_name
                                        text: "Abhay"
                                        secondary_text: "Secondary text here"
                                        tertiary_text:"Tertiary Text"
                                        on_release:app.chat_msg()
                                        ImageLeftWidget:
                                            id:home_image
                                            source: "https://media.istockphoto.com/id/517188688/photo/mountain-landscape.jpg?s=612x612&w=0&k=20&c=A63koPKaCyIwQWOTFBRWXj_PwCrR4cEoOw2S9Q7yVl8="
                                            radius: 24
                                            
                                        
        
                                        IconRightWidget:
                                            icon: 'dots-vertical'
                                            
                                        
        
                                    
        
                        MDIconButton:
                            size_hint: None, None
                            icon_size:"50sp"
                            on_release:app.ai_screen()
                            pos_hint: {"center_x":.9,"center_y":.15}
                            FitImage:
                                source:"https://swisscognitive.ch/wp-content/uploads/2020/09/the-4-top-artificial-intelligence-trends-for-2021.jpeg"
                                radius:24
                    
                    MDBottomNavigationItem:
                        name: "screen 2"
                        text:"Server"
                        icon:"server"
                        
                        MDSwiper:
                            size_hint_y: None
                            height: root.height - dp(40)
                            y: root.height - self.height - dp(20)
                            
                        MDCard:
                            size_hint: None, None
                            pos_hint:{"center_x":.5,"center_y": .95}
                            size_hint: 0.8,0.06
                            elevation: 2
                            radius: [10,]
                            border_radius: 10
                        
                            TextInput:
                                id: server_url
                                hint_text: "Enter Server Url"
                                helper_text: "Enter Server Url"
                                size_hint: .9,None
                                pos_hint:{"center_x": .2,"center_y": .5}
                                height: self.minimum_height
                                multiline: False
                                cursor_color: 0,0,0,1
                                cursor_width:"2sp"
                                background_color: 0,0,0,0
                                padding: 15
                                font_size: "18sp" 
                                normal_color: app.theme_cls.bg_light
                                color_active: app.theme_cls.bg_light
                                icon_left: "magnify"
                                foreground_color: app.theme_cls.secondary_text_color
                        
            
                            
                                    
                            MDIconButton:
                                icon: "cast-connected"
                                pos_hint:{"center_x": .93,"center_y": .5}
                                on_release:
                                    app.server()
                                    
                                    
                        
                            
                        
                    MDBottomNavigationItem:
                        name: "screen 3"
                        text:"Music"
                        icon:"music"
                  
                    
                        MDScreen:
                            name:"music"
                            ScrollView:
                                do_scroll_x:True
                                do_scroll_y:False
                                MDBoxLayout:
                                    orientation: "horizontal"
                                    size_hint_y: None
                                    height: "122dp"
                                    MDFlatButton:
                                        text:"Trending Song"
                                        bold: True
                                        on_release:app.trend()
    
                                    MDFlatButton:
                                        text:"Bhojpuri Song"
                                        bold: True
                                        on_release:app.bhojpuri()
    
                                    MDFlatButton:
                                        text:"Romantic Song"
                                        bold: True
                                        on_release:app.romantic()
    
                                    MDFlatButton:
                                        text:"Party Song"
                                        bold: True
                                        on_release:app.party()
    
                                    MDFlatButton:
                                        text:"Old Song"
                                        bold: True
                                        on_release:app.old()
    
                            MDLabel:
                                id: home_text
                                text: ""
                                pos_hint: {'center_x': .55, 'center_y': .5}
                                bold:True
    
                            MDSpinner:
                                id: music_spinner
                                size_hint: None, None
                                size: dp(46), dp(46)
                                pos_hint: {'center_x': .5, 'center_y': .5}
                                active: False
    
                            ScrollView:
                                size_hint_y:.85
                                MDList:
                                    id:home_music
    
                    
    
                            MDCard:
                                size_hint: None, None
                                pos_hint:{"center_x":.5,"center_y": .95}
                                size_hint: 0.8,0.06
                                elevation: 2
                                radius: [10,]
                                border_radius: 10
                            
                                TextInput:
                                    id: song_name
                                    hint_text: "Songs, artists or podcasts"
                                    helper_text: "Enter song name here"
                                    size_hint: .9,None
                                    pos_hint:{"center_x": .2,"center_y": .5}
                                    height: self.minimum_height
                                    multiline: False
                                    cursor_color: 0,0,0,1
                                    cursor_width:"2sp"
                                    background_color: 0,0,0,0
                                    padding: 15
                                    font_size: "18sp" 
                                    normal_color: app.theme_cls.bg_light
                                    color_active: app.theme_cls.bg_light
                                    icon_left: "magnify"
                                    foreground_color: app.theme_cls.secondary_text_color
                            
                
                                MDIconButton:
                                    id:clos
                                    icon: "magnify"
                                    pos_hint:{"center_x": .93,"center_y": .5}
                                    on_release:
                                        app.clear()
                                        
                                MDIconButton:
                                    icon: "magnify"
                                    pos_hint:{"center_x": .93,"center_y": .5}
                                    on_release:
                                        app.show_data(song_name.text)
                MDRelativeLayout:
                    id:home
                    size_hint:1,.1
                    pos_hint:{"center_x":.5,"center_y":.13}
                    radius:15
                    
                    MDCard:
                        id: home_image
                        size_hint: None, None
                        pos_hint:{"center_x":.1,"center_y": .5}
                        size_hint: 0.17,0.8
                        elevation: 1
                        radius: 30
                        border_radius: 10
                        
                        FitImage:
                            id:home_song_image_url
                            radius:15
                            source:"cover.jpg"
                    
                    MDIconButton:
                        id:home_play
                        icon: ""
                        icon_size:"48sp"
                        pos_hint:{"center_x":.8,"center_y":.5}
                        on_release:app.pause()
                        
            MDScreen:
                id:playscreen
                name:"playscreen"
                MDCard:
                    id: song_image
                    size_hint: None, None
                    pos_hint:{"center_x":.5,"center_y": .65}
                    size_hint: 0.9,0.4
                    elevation: 1
                    radius: 30
                    border_radius: 10
                    
                    FitImage:
                        id:song_image_url
                        radius:15
                        
                MDLabel:
                    id: songname
                    text:"Tum Kyu Chale Aate ho"
                    font_size:"20sp"
                    pos_hint:{"center_x":.55,"center_y": .4}
                    halign: "center"
                    
                MDLabel:
                    id: song_du
                    text:"00:00"
                    font_size:"20sp"
                    pos_hint:{"center_x":.93,"center_y": .32}
                    halign: "center"
                    
                MDLabel:
                    id: song_cu
                    text:"00:00"
                    font_size:"20sp"
                    pos_hint:{"center_x":.09,"center_y": .32}
                    halign: "center"
                    
                MDSlider:
                    id:progress
                    pos_hint:{"center_x": .5,"center_y": .35}
                    size_hint_x:.9
                    size_hint_y:.08
                    value:0
                    thumb_color_active: "red"
                    on_active:app.slide()
                    
                MDFloatingActionButton:
                    id:play
                    icon: "play"
                    icon_size: "50sp"
                    pos_hint:{"center_x": .5,"center_y": .25}
                    on_release:app.pause()
                    
            MDScreen:
                id: chat_screen
                name:"chat"
                MDRelativeLayout:
                    md_bg_color:210/255,212/255,217/255,1
                    size_hint:.9,.08
                    pos_hint:{"center_x":.5,"center_y":.94}
                    radius:15

                    MDIconButton:
                        icon: "arrow-left"
                        pos_hint:{"center_x":.05,"center_y":.5}
                        on_release:app.back()

                    FitImage:
                        id: image
                        size_hint:.14,.7
                        radius:12
                        pos_hint:{"center_x":.16,"center_y":.5}
                        source:"https://media.istockphoto.com/id/517188688/photo/mountain-landscape.jpg?s=612x612&w=0&k=20&c=A63koPKaCyIwQWOTFBRWXj_PwCrR4cEoOw2S9Q7yVl8="

                    MDLabel:
                        id:name
                        text: "Abhay"
                        bold:True
                        size_hint: None, None
                        font_size:"20dp"
                        pos_hint:{"center_x":.32,"center_y":.5}

                    


                MDRelativeLayout:
                    id:chat_layout
                    size_hint:1,.62
                    pos_hint:{"center_x":.5,"center_y":.56}
                    radius:15

                    ScrollView:
                        id: scrollview

                        MDBoxLayout:
                            id: chat_list
                            orientation: 'vertical'
                            adaptive_height: True
                            spacing: "10dp"
                            padding: "10dp"

                            MDRelativeLayout:
                                md_bg_color:210/255,212/255,217/255,1
                                size_hint:.9,.08
                                pos_hint:{"center_x":.5,"center_y":.94}
                                radius:15


                    
                    
                MDRaisedButton:
                    id: reply_label
                    text: ""
                    size_hint_x: 0.3
                    opacity: 0
                    pos_hint:{"center_x":.75,"center_y":.2}
                    on_release: app.cancel_reply()


                MDLabel:
                    id:typing_label
                    text:""
                    pos_hint:{"center_x":.55,"center_y":.2}
            

                MDCard:
                    id: chat_card
                    size_hint: None, None
                    pos_hint:{"center_x":.5,"center_y": .1}
                    size_hint: 0.9,.07
                    elevation: 1.5
                    radius: [10,]
                    border_radius: 10
                    MDIconButton:
                        icon: "sticker-emoji"
                        pos_hint:{"center_x":.05,"center_y":.5}

                    TextInput:
                        id: message_input
                        hint_text: "Type a message ..."
                        helper_text: "Please Enter a message"
                        size_hint: .7,None
                        mode: "fill"
                        pos_hint:{"center_x": .45,"center_y": .5}
                        height: self.minimum_height
                        multiline: False
                        cursor_color: 0,0,0,1
                        cursor_width:"2sp"
                        background_color: 0,0,0,0
                        padding: 15
                        on_text: app.on_typing()
                        font_size: "18sp" 
                        normal_color: app.theme_cls.bg_light
                        color_active: app.theme_cls.bg_light
                        icon_left: "magnify"
                        foreground_color: app.theme_cls.secondary_text_color

                    MDIconButton:
                        id: close
                        icon: "close"
                        pos_hint:{"center_x":.85,"center_y":.5}
                        on_release:app.clear()

                    MDIconButton:
                        icon: "attachment"
                        pos_hint:{"center_x":.85,"center_y":.5}
                        on_release:app.file_manager_open()

                    MDIconButton:
                        icon: "send"
                        pos_hint:{"center_x":.95,"center_y":.5}
                        on_release: app.send_message()

                
            MDScreen:
                name:"setting"
                MDLabel:
                    text: "Setting"
                    bold: True
                    halign: "center"
                    font_size: "30sp"
                    pos_hint:{"center_y":.95}
                        
                FloatLayout:
                    MDLabel:
                        text: "Dark Mode"
                        padding_x: "30dp"
                        theme_text_color: 'Primary'
                        pos_hint: {'center_y': .9}
                    MDSwitch:
                        id: dark_mode_switch
                        active: False
                        pos_hint: {'center_x': 0.9, 'center_y': .9}
                        on_active: app.change_theme()
                    
                    MDLabel:
                        text: "Current version"
                        padding_x: "30dp"
                        theme_text_color: 'Primary'
                        pos_hint: {'center_y': 0.5}
                    MDTextButton:
                        text: "v"+app.__version__ + "-alpha"
                        padding_x: "30dp"
                        custom_color: app.theme_cls.secondary_text_color
                        pos_hint: {'center_x':0.9, 'center_y': 0.5}
                        on_press: toast("Alpha v0.7")
                    MDLabel:
                        text: "Download location"
                        padding_x: "30dp"
                        theme_text_color: 'Primary'
                        pos_hint: {'center_y': 0.7}
                    MDTextButton:
                        text: "Abhay"
                        padding_x: "30dp"
                        custom_color: app.theme_cls.secondary_text_color
                        pos_hint: {'center_x':0.9, 'center_y': 0.7}
                        on_press: app.file_manager_open()
                    MDTextButton:
                        text: "Check for Update"
                        padding_x: "30dp"
                        custom_color: app.theme_cls.text_color
                        pos_hint: {'center_y': 0.3}
                        on_release: app.check_update()
                            
                            
                    MDRaisedButton:
                        text: "Log Out"
                        padding_x: "30dp"
                        custom_color: app.theme_cls.text_color
                        pos_hint: {'center_y': 0.2}
                        on_release: app.logout()
                
           
            MDScreen:
                name: "music_list"
                md_bg_color: 0,0,0,0.77
                        
                MDSliverAppbar:
                    max_height: "70dp"
                    toolbar_cls: SliverToolbar()
                    
                    MDSliverAppbarHeader:

                    MDSliverAppbarContent:
                        id: cont
                        orientation: "vertical"
                        padding: "12dp"
                        spacing: "12dp"
                        md_bg_color: 0,0,0,0.77
                        adaptive_height: True
                        
            # 
                    
                MDSpinner:
                    id: spinner
                    size_hint: None, None
                    size: dp(46), dp(46)
                    pos_hint: {'center_x': .5, 'center_y': .5}
                    active: False
                    
            
                MDSpinner:
                    id: spinner
                    size_hint: None, None
                    size: dp(46), dp(46)
                    pos_hint: {'center_x': .5, 'center_y': .5}
                    active: False

                MDIconButton:
                    icon: "arrow-left"
                    pos_hint:{"center_x": .05,"center_y": .95}
                    md_bg_color: 1,1,1,1
                    on_release: app.c()
                    
        MDNavigationDrawer:
            id: nav_drawer
            
                
            MDNavigationDrawerMenu:

                MDNavigationDrawerHeader:
                    title: "A.I Chat"
                    title_color: "#4a4939"
                    text: "bhagatabhay121@gmail.com"
                    spacing: "4dp"
                    padding: "12dp", 0, 0, "56dp"

                MDNavigationDrawerLabel:
                    text: "Setting"

                MDNavigationDrawerItem:
                    icon: "account"
                    text: "Profile"

                MDNavigationDrawerItem:
                    icon: "theme-light-dark"
                    text: "Outbox"

                MDNavigationDrawerDivider:

                MDNavigationDrawerLabel:
                    text: "Labels"

                MDNavigationDrawerItem:
                    icon: "information-outline"
                    text: "Label"

                MDNavigationDrawerItem:
                    icon: "information-outline"
                    text: "Label"
                    
                MDNavigationDrawerItem:
                    icon: "logout"
                    text: "Log Out"
                    

            
'''

class HomeScreen(Screen):
    pass


class Tab(MDFloatLayout, MDTabsBase):
    pass

class abhay(TwoLineAvatarIconListItem):
    pass

class MDLabel1(MDLabel):
    pass

class SliverTool(MDTopAppBar):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.shadow_color = (0, 0, 0, 0)
        self.title = "My Music"

class SliverToolbar(MDTopAppBar):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.shadow_color = (0, 0, 0, 0)
        self.title = "Results"

class Test(MDApp):

    global screen_manager
    screen_manager = ScreenManager()
    last_screen = []
    username = "Abhay"
    
    scroll = "False"
    song_url = ""
    trend_song = ""
    bhojpuri_song = ""
    romantic_song = ""
    party_song = ""
    old_song = ""
    selected_message = None 
    title = "A.I Chat"
    __version__ = "0.7"
    status = True
    play_status = 'stop'
    last_screen = []

    def build(self):
        
        Loader.loading_image = 'cover.jpg'
#        self.username = "User1" 
        self.title = "Ghost Comm - Silent.Stealthy.Secret" 
        self.icon = "topbarlogo.png"
        self.file_manager = MDFileManager(exit_manager=self.file_manager_close, select_path=self.upload_file)
        self.manager_open = False
        
       
        return Builder.load_string(KV)
        
    def chat_msg(self):
        self.change_screen("chat")
        
    def save(self):
        name = self.root.ids.user.text
        if name:
            store.put("user", name=name) 
            
            self.root.ids.screen_manager.current = "home"
            
            self.username = store.get("user")["name"]
            
    
    def server(self):
        try:
            ak = self.root.ids.server_url.text
            self.sio = socketio.Client()
            self.sio.connect(ak)
            self.sio.on("message", self.receive_message)
            self.sio.on("typing", self.show_typing)
            self.sio.on("play_music", self.play_received_music)
            self.sio.on("stopped_typing", self.hide_typing)
            self.sio.on("file_received", self.receive_file)
            self.sio.on("upload_progress", self.update_upload_progress)
            self.sio.on("reaction", self.update_reaction_ui)
            self.sio.on("delete_message", self.handle_delete_message)
            self.sio.on("edit_message", self.handle_edit_message)
            self.typing_timer = None
            self.change_screen("chat")
            self.root.ids.home.badge_icon = ""
            
        except:
            toast("Wrong Url")

    def play_received_music(self, data):
        """ Plays music when received from another user """
        user = data.get("user")
         # Ensure only other's music is played
        if user == self.username:
            print("True")

        else:
            song_url = data.get("url", "")
            print(song_url)
            try:
                self.stop()
                
            except:
                pass

            self.prepare(song_url)
            if self.sound:
                self.play()

    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.manager_open = False
        self.file.close()

    def handle_delete_message(self, data):
        """Handle message deletion from the server."""
        message_id = data["message_id"]
        Clock.schedule_once(lambda dt: self.remove_message_from_ui(message_id))


    def update_reaction_ui(self, data):
        message_id = data["message_id"]
        reactions = data["reactions"]

        chat_list = self.root.ids.chat_list
        for widget in chat_list.children:
            if hasattr(widget, "id") and widget.id == message_id:
                for child in widget.children:
                    if isinstance(child, MDLabel):  # Find the reaction label
                        child.text = "".join([f"{emoji} {count} " for emoji, count in reactions.items()])
                        return
        
    def file_manager_open(self):
        self.file_manager.show(os.path.expanduser("~"))

    def file_manager_close(self, *args):
        self.file_manager.close()

    def upload_file(self, path):
        self.file_manager_close()
        filename = os.path.basename(path)
        file_size = os.path.getsize(path)
        chunk_size = 1024 * 10  # 10 KB per chunk
        total_chunks = (file_size + chunk_size - 1) // chunk_size

        with open(path, "rb") as f:
            for chunk_index in range(total_chunks):
                chunk_data = f.read(chunk_size)
                self.sio.emit("file_chunk", {
                    "filename": filename,
                    "chunk": chunk_data,
                    "chunk_index": chunk_index,
                    "total_chunks": total_chunks
                })
        
        # Show upload progress in UI
        Clock.schedule_once(lambda dt: self.show_upload_progress(filename))

    def show_upload_progress(self, filename):
        progress_bar = MDProgressBar(value=0, max=100)
        progress_item = OneLineAvatarIconListItem(text=f"Uploading {filename}...")
        progress_item.add_widget(progress_bar)
        self.root.ids.chat_list.add_widget(progress_item)
        setattr(self, f"upload_progress_{filename}", progress_bar)

    def back(self):
        self.change_screen("home")

    def add_file_to_ui(self, filename, file_url):
        file_item = OneLineAvatarIconListItem(text=f"{self.username} :{filename}")
        file_item.add_widget(IconLeftWidget(icon="download"))
        file_item.bind(on_release=lambda x: self.download_file(file_url, filename))
        self.root.ids.chat_list.add_widget(file_item)

    def update_upload_progress(self, data):
        filename = data["filename"]
        progress = data["progress"]
        
        if hasattr(self, f"upload_progress_{filename}"):
            Clock.schedule_once(lambda dt: setattr(getattr(self, f"upload_progress_{filename}"), "value", progress))
    
    def receive_file(self, data):
        filename = data["filename"]
        file_url = data["url"]
        
        Clock.schedule_once(lambda dt: self.add_file_to_ui(filename, file_url))
        
    def post(self,sender,message_id,message):
        try:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            data = {
                "sender":sender,
                "message":message,
                "time":current_time,
                "message_id":message_id,
                "reply_to": self.selected_message if self.selected_message else None
            }
            requests.post(FIREBASE_URL, json=data)

            self.selected_message = None
            self.update_reply_ui(None)

        except:
            toast("You Are Offline")

    def send_message(self):
        msg = self.root.ids.message_input.text.strip()

        if msg:
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            message_id = str(time.time()) 
            data = {
                "sender": self.username,
                "message_id": message_id,
                "message": msg,
                "reply_to": self.selected_message if self.selected_message else None,
                "time": current_time
            }
            try:
                self.sio.emit("message", data)  # Send to server
                self.selected_message = None  # Reset after sending
                self.root.ids.message_input.text = ""  # Clear input
                self.update_reply_ui(None)

            except:
                chat_list = self.root.ids.chat_list
                sender = self.username
                message_id = message_id
                message = msg
                current_time = str(time)
                print(type(current_time))
                long_text = f"{sender}: {message}"
                ak = break_text(long_text, 75)
                self.root.ids.message_input.text = ""
                threading.Thread(target=self.post, daemon=True, args=(sender,message_id,message)).start()

                

                def show_menu(instance):
                    dropdown_menu.open()

            

                def delete_message_action():
                    self.delete_message(message_id)
                    dropdown_menu.dismiss()

                def reply_message_action():
                    self.select_message(message)
                    dropdown_menu.dismiss()

                def copy_message_action():
                    Clipboard.copy(message)
                    toast("Message is copied.")
                    dropdown_menu.dismiss()

                def reaction_message_action():
                    self.show_reaction_menu(message_id)
                    dropdown_menu.dismiss()

                menu_items = [
                    {"text": "Delete", "on_release": delete_message_action},
                    {"text": "Reply", "on_release": reply_message_action},
                    {"text": "Copy", "on_release": copy_message_action},
                    {"text": "Reaction", "on_release": reaction_message_action}
                ]

                if sender == self.username:
                    def edit_message_action():
                        self.show_edit_popup(message_id, message, sender)
                        dropdown_menu.dismiss()
                    menu_items.insert(0, {"text": "Edit", "on_release": edit_message_action})

                

                if sender == self.username:
                
                    bubble = MDCard(
                        size_hint_x=None,  # Let width be dynamically set
                        size_hint_y=None,
                        adaptive_size=True,
                        width=dp(100),
                        height=dp(50),
                        padding=dp(20),
                        pos=(dp(5100), dp(400)),
                        radius=[10, 10, 10, 0], 
                        md_bg_color=(66/255,135/255,245/255,1),
                        id=message_id 
                    )

                    now = datetime.now()
                    cu = now.strftime("%H:%M:%S")

                    label = MDLabel(
                        text=ak,
                        theme_text_color="Custom",
                        text_color=(1, 1, 1, 1),
                        size_hint_y=None,
                        size_hint_x=None,
                        adaptive_size=True,
                        text_size=(None, None),
                        halign="right",
                        pos_hint={'center_x': 0.02,'center_y': 0.9}
                    )

                    label_time = MDLabel1(
                        text=cu,
                        theme_text_color="Custom",
                        text_color=(0, 0, 0, 1),
                        size_hint_y=None,
                        adaptive_size=True,
                        pos_hint={'center_x': 0.1,'center_y': 0.0001}
                    )
                    bubble.bind(on_release=show_menu)
                    bubble.add_widget(label)
                    bubble.add_widget(label_time)
                    bubble.width = label.texture_size[0] + dp(30)

                else:
                    bubble = MDCard(
                        size_hint_x=None,  # Let width be dynamically set
                        size_hint_y=None,
                        adaptive_size=True,
                        width=dp(100),
                        height=dp(50),
                        padding=dp(20),
                        pos=(dp(50), dp(400)),
                        radius=[10, 10, 10, 0],  # Rounded edges
                        md_bg_color=(210/255,212/255,217/255,1),
                        id=message_id 
                    )

                

                    label = MDLabel(
                        text=ak,
                        theme_text_color="Custom",
                        text_color=(1, 1, 1, 1),
                        size_hint_y=None,
                        size_hint_x=None,
                        adaptive_size=True,
                        text_size=(None, None),
                        halign="left",
                        pos_hint={'center_x': 0.02,'center_y': 0.9}
                    )

                    # label_time = MDLabel1(
                    #     text=current_time,
                    #     theme_text_color="Custom",
                    #     text_color=(0, 0, 0, 1),
                    #     size_hint_y=None,
                    #     adaptive_size=True,
                    #     pos_hint={'center_x': 0.92,'center_y': 0.0001}
                    # )     

                    bubble.bind(on_release=show_menu)
                    bubble.add_widget(label)
                    #bubble.add_widget(label_time)
                    bubble.width = label.texture_size[0] + dp(30)
                #bubble.width = label.texture_size[0] + ("20dp")

                dropdown_menu = MDDropdownMenu(
                    caller=bubble,
                    items=menu_items,
                    width_mult=3
                )

                
                
                chat_list.add_widget(bubble)
                self.root.ids.scrollview.scroll_y = 0
                
    def receive_message(self,data):
        sender = data["sender"]
        ak = data["message"]
        if sender == self.username:
            pass
        else:
            if self.root.ids.screen_manager.current == 'chat':
                pass
                
            else:
                self.message(sender, ak)
        reply_to = data.get("reply_to", None)
        Clock.schedule_once(lambda dt: self.add_message_to_ui(data, reply_to))
        
    def message(self,status, title):
        notification.notify(title=f"Message From - {status}",message=f"{title}",app_name="A.I Chat",timeout=5)
        
        self.root.ids.home.badge_icon = "numeric-1"

    def on_typing(self):
        """ Detects user typing and notifies others """
        
        try:
            self.sio.emit("typing", {"user": self.username})
            
            

            # Cancel any previous timer and restart it
            if self.typing_timer:
                self.typing_timer.cancel()
            self.typing_timer = Clock.schedule_once(self.user_stopped_typing, 2)

        except:
            pass

    def user_stopped_typing(self, dt):
        """ Called when user stops typing for 2 seconds """
        self.sio.emit("stopped_typing", {"user": self.username})

    def show_typing(self, data):
        """ Show 'User is typing...' only if another user is typing """
        if data["user"] != self.username:  # Avoid showing own typing status
            Clock.schedule_once(lambda dt: setattr(
                self.root.ids.typing_label, 'text', f"{data['user']} is typing..."
            ))

    def hide_typing(self, data):
        """ Hide 'User is typing...' when typing stops """
        if data["user"] != self.username:  # Ensure only other's typing is hidden
            Clock.schedule_once(lambda dt: setattr(self.root.ids.typing_label, 'text', ""))

    def update_reply_ui(self, message):
        """Updates the UI to show the selected message for reply."""
        reply_label = self.root.ids.reply_label

        if message:
            reply_label.text = f"Replying to: {message}"
            reply_label.opacity = 1
        else:
            reply_label.text = ""
            reply_label.opacity = 0

    def cancel_reply(self):
        """Cancels reply mode"""
        self.selected_message = None
        self.update_reply_ui(None)

    def delete_message(self, message_id):
        """Send delete request to the server and remove the message from UI."""
        self.remove_message_from_ui(message_id)
        try:
            self.sio.emit("delete_message", {"message_id": message_id})
        except:
            #threading.Thread(target=self.delete, daemon=True, args=(ak)).start()
            Clock.schedule_once(lambda dt: self.delete(message_id))
            
    def delete(self, message_id):
        try:
            message_id = message_id
            if message_id:
                messages_ref = db.reference("chat")  # Adjust if needed
                messages = messages_ref.get()

                if messages:
                    for key, msg in messages.items():
                        if msg.get("message_id") == message_id:
                            messages_ref.child(key).delete()  # Remove from Firebase
                            break

        except:
            toast("You Are Offline")
        
            
    def remove_message_from_ui(self, message_id):
        """Find and remove the message from the UI."""
        chat_list = self.root.ids.chat_list
        for widget in chat_list.children[:]:  
            if hasattr(widget, "id") and widget.id == message_id:
                chat_list.remove_widget(widget)
                break

    def select_message(self, message):
        """Selects a message to reply to."""
        self.selected_message = message
        self.update_reply_ui(message)

    def update_reply_ui(self, message):
        """Updates the UI to show the selected message for reply."""
        reply_label = self.root.ids.reply_label

        if message:
            reply_label.text = f"Replying to: {message}"
            reply_label.opacity = 1
        else:
            reply_label.text = ""
            reply_label.opacity = 0

    def cancel_reply(self):
        """Cancels reply mode"""
        self.selected_message = None
        self.update_reply_ui(None)

    def show_edit_popup(self, message_id, old_message, sender):
        
        """Open a popup to edit a message."""
        content = MDBoxLayout(orientation='vertical', spacing=10, padding=10)

        text_input = MDTextField(
            text=old_message,
            hint_text="Edit your message..."
        )
        content.add_widget(text_input)

        save_button = MDRaisedButton(
            text="Save",
            on_release=lambda x: self.edit_message(message_id, text_input.text,sender)
        )
        content.add_widget(save_button)

        self.edit_popup = Popup(
            title="Edit Message",
            content=content,
            size_hint=(None, None),
            size=("400dp", "200dp"),
            background_color=(1,1,1,1)
        )
        self.edit_popup.open()
        
    def edit(self,sender, message_id, new_message):
        try:
            if message_id and new_message:
            # Locate the message in Firebase using message_id
                messages_ref = db.reference("chat")  # Adjust this if your messages are stored differently
                messages = messages_ref.get()

                if messages:
                    for key, msg in messages.items():
                        if msg.get("message_id") == message_id:
                            # Update the message content in Firebase
                            messages_ref.child(key).update({"message": new_message})
                            break

        except:
            toast("You Are Offline")

    def edit_message(self, message_id, new_message, sender):
        self.edit_popup.dismiss()
        try:
            self.sio.emit("edit_message", {"message_id": message_id, "new_message": new_message, "user": sender})
            
        except:
            threading.Thread(target=self.edit, daemon=True, args=(sender,message_id,new_message)).start()
        print("pressed")
        chat_list = self.root.ids.chat_list
        for widget in chat_list.children:
            if hasattr(widget, "id") and widget.id == message_id:
                labels = [child for child in widget.children if isinstance(child, MDLabel)]
                if len(labels) >= 2:
                    labels[1].text = f"{sender}: {new_message}"

                return

        

        #self.update_message_in(message_id, new_message)

    def handle_edit_message(self, data):
        """Handle an edited message from the server."""
        message_id = data["message_id"]
        new_message = data["new_message"]
        user = data["user"]
        Clock.schedule_once(lambda dt: self.update_message_in(message_id, new_message, user))

    

    def update_message_in(self, message_id, new_message, user):
        chat_list = self.root.ids.chat_list
        for widget in chat_list.children:
            if hasattr(widget, "id") and widget.id == message_id:
                labels = [child for child in widget.children if isinstance(child, MDLabel)]
                if len(labels) >= 2:
                    labels[1].text = f"{user}: {new_message}"

                return

    def add_message_to_ui(self, data, reply_to=None):
        chat_list = self.root.ids.chat_list
        sender = data["sender"]
        message_id = data["message_id"]
        message = data["message"]
        current_time = data["time"]
        reactions = data.get("reactions", {})
        reply_to = data.get("reply_to", None)
        long_text = f"{sender}: {message}"
        ak = break_text(long_text, 75)
           

        def show_menu(instance):
            dropdown_menu.open()

       

        def delete_message_action():
            self.delete_message(message_id)
            dropdown_menu.dismiss()

        def reply_message_action():
            self.select_message(message)
            dropdown_menu.dismiss()

        def copy_message_action():
            Clipboard.copy(message)
            toast("Message is copied.")
            dropdown_menu.dismiss()

        def reaction_message_action():
            self.show_reaction_menu(message_id)
            dropdown_menu.dismiss()

        menu_items = [
            {"text": "Delete", "on_release": delete_message_action},
            {"text": "Reply", "on_release": reply_message_action},
            {"text": "Copy", "on_release": copy_message_action},
            {"text": "Reaction", "on_release": reaction_message_action}
        ]

        if sender == self.username:
            def edit_message_action():
                self.show_edit_popup(message_id, message, sender)
                dropdown_menu.dismiss()
            menu_items.insert(0, {"text": "Edit", "on_release": edit_message_action})

        

        if sender == self.username:
        
            bubble = MDCard(
                size_hint_x=None,  # Let width be dynamically set
                size_hint_y=None,
                adaptive_size=True,
                width=dp(100),
                height=dp(50),
                padding=dp(20),
                pos=(dp(5100), dp(400)),
                radius=[10, 10, 10, 0], 
                md_bg_color=(66/255,135/255,245/255,1),
                id=message_id 
            )

            

            label = MDLabel(
                text=ak,
                theme_text_color="Custom",
                text_color=(1, 1, 1, 1),
                size_hint_y=None,
                size_hint_x=None,
                adaptive_size=True,
                text_size=(None, None),
                halign="right",
                pos_hint={'center_x': 0.02,'center_y': 0.9}
            )

            label_time = MDLabel1(
                text=current_time,
                theme_text_color="Custom",
                text_color=(0, 0, 0, 1),
                size_hint_y=None,
                adaptive_size=True,
                pos_hint={'center_x': 0.1,'center_y': 0.0001}
            )
            bubble.bind(on_release=show_menu)
            bubble.add_widget(label)
            bubble.add_widget(label_time)
            bubble.width = label.texture_size[0] + dp(30)

        else:
            bubble = MDCard(
                size_hint_x=None,  # Let width be dynamically set
                size_hint_y=None,
                adaptive_size=True,
                width=dp(100),
                height=dp(50),
                padding=dp(20),
                pos=(dp(50), dp(400)),
                radius=[10, 10, 10, 0],  # Rounded edges
                md_bg_color=(210/255,212/255,217/255,1),
                id=message_id 
            )

        

            label = MDLabel(
                text=ak,
                theme_text_color="Custom",
                text_color=(1, 1, 1, 1),
                size_hint_y=None,
                size_hint_x=None,
                adaptive_size=True,
                text_size=(None, None),
                halign="left",
                pos_hint={'center_x': 0.02,'center_y': 0.9}
            )

            label_time = MDLabel1(
                text=current_time,
                theme_text_color="Custom",
                text_color=(0, 0, 0, 1),
                size_hint_y=None,
                adaptive_size=True,
                pos_hint={'center_x': 0.92,'center_y': 0.0001}
            )     

            bubble.bind(on_release=show_menu)
            bubble.add_widget(label)
            bubble.add_widget(label_time)
            bubble.width = label.texture_size[0] + dp(30)
        #bubble.width = label.texture_size[0] + ("20dp")

        dropdown_menu = MDDropdownMenu(
            caller=bubble,
            items=menu_items,
            width_mult=3
        )

        if reply_to:
            reply_bubble = MDCard(
                size_hint_x=None,
                size_hint_y=None,
                adaptive_size=True,
                padding=[15, 5],
                radius=[10, 10, 10, 10],
                md_bg_color=(0.5, 0.5, 0.5, 1)  # Gray for reply
            )
            reply_label = MDLabel(
                text=f"Replying to: {reply_to}",
                theme_text_color="Custom",
                text_color=(1, 1, 1, 1),
                size_hint_y=None,
                adaptive_size=True,
            )
            reply_bubble.add_widget(reply_label)
            bubble.add_widget(reply_bubble)

        
        chat_list.add_widget(bubble)
        self.root.ids.scrollview.scroll_y = 0
    

    def change_screen(self, screen, *args):
        
        if args:
            self.root.ids.screen_manager.transition.direction = args[0]
            if args[0] != 'right':
                self.last_screen.append(self.root.ids.screen_manager.current)
                
        else:
            self.root.ids.screen_manager.transition.direction = 'left'
            self.last_screen.append(self.root.ids.screen_manager.current)
        self.root.ids.screen_manager.current = screen

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Window.bind(on_keyboard=self.events)

    def events(self, instance, keyboard, keycode, text, modifiers):
        if keyboard == 13:
            if self.root.ids.screen_manager.current == 'music':
                self.show_data(self.root.ids.song_name.text)
            else:
                pass
      
        if keyboard in (1001, 27):   
            self.back_screen()
            
        else:
            pass
 
        return True
        
    def back_screen(self):
        if self.root.ids.screen_manager.current != 'MainScreen':
            self.change_screen(self.last_screen[-1], 'right')
            self.last_screen.pop(-1)

    def back(self):
        self.change_screen("home")
    
    def ai_screen(self):
        self.change_screen("ai")

    def change(self):
        self.change_screen("chat")

    def c(self):
        self.change_screen("chat")

    def music(self):
        self.change_screen("music")

    def show_data(self, query):
       # close_btn = MDFlatButton(text="Close", on_release=self.close_dialog)
        if query == '':
            self.dia = MDDialog(title="Invalid Name", text="Please enter a song name", size_hint=(0.7,1))
            self.dia.open()
            
        else:
            #self.trend()
          #  self.root.ids.screen_manager.transition = WipeTransition()
            self.change_screen('music_list')
            self.root.ids.cont.clear_widgets()
            
            self.root.ids.spinner.active = True
            req = UrlRequest(search_base_url+query.replace(' ','+'), self.show_list)


    def show_list(self, req, result):
        self.root.ids.song_name.text = ""
        self.search_data = json.loads(result.replace("&quot;","'").replace("&amp;", "&").replace("&#039;", "'"))['songs']['data']
        
        
        for i in range(len(self.search_data)):
            print(self.search_data[i]["title"])
            
            self.image_url = self.search_data[i]['image'].replace('50x50', '500x500').replace('150x150', '500x500')
            
        
            
            lst = abhay(text=self.search_data[i]['title'].replace("&quot;","'").replace("&amp;", "&").replace("&#039;", "'"),theme_text_color="Custom",text_color=(1,1,1,1), secondary_text=self.search_data[i]['more_info']['primary_artists'].replace("&quot;","'").replace("&amp;", "&").replace("&#039;", "'"), secondary_theme_text_color="Custom",secondary_text_color=(220/255,86/255,219/255,0.74/1),on_press=lambda x,y=i: self.song_detail(y))
            sk = IconLeftWidget(icon="",theme_text_color="Custom",text_color=(1,1,1,1))
            
            sl = FitImage(source=self.image_url, radius=20)
            
            sk.add_widget(sl)
            lst.add_widget(sk)
            
      
         
            self.root.ids.cont.add_widget(lst)
            
        self.root.ids.spinner.active = False

    def trend(self, *args):
        self.root.ids.music_spinner.active = True
        self.root.ids.home_text.text = "Song Is Searching ..."
        threading.Thread(target=self.trend_s, daemon=True).start()

    def trend_s(self):
        Clock.schedule_once(lambda dt: self.trend_so())

    def trend_so(self):
        try:
            self.root.ids.home_music.clear_widgets()
            
            response = requests.get(playlist_details_base_url.format("I3kvhipIy73uCJW60TJk1Q__")+"&lyrics=true")
            if response.status_code == 200:
                songs_json = response.text.encode().decode()
                songs_json = json.loads(songs_json)
                self.search_data = songs_json['list']
                self.trend_song = self.search_data
    
                for i in range(len(self.search_data)):
                    print(self.search_data[i]["title"])
                        
                    self.image_url = self.search_data[i]['image'].replace('50x50', '500x500').replace('150x150', '500x500')
                        
                    
                        
                    lst = abhay(text=self.search_data[i]['title'].replace("&quot;","'").replace("&amp;", "&").replace("&#039;", "'"),on_press=lambda x,y=i: self.song_detail(y))
                    sk = IconLeftWidget(icon="",theme_text_color="Custom",text_color=(1,1,1,1))
                        
                    sl = FitImage(source=self.image_url, radius=20)
                        
                    sk.add_widget(sl)
                    lst.add_widget(sk)
                        
                
                    
                    self.root.ids.home_music.add_widget(lst)
    


        except:
            toast("You are Offline")
            self.root.ids.home_text.text = "You are offline"
            
        self.root.ids.music_spinner.active = False
        self.root.ids.home_text.text = ""


    def bhojpuri(self,*args):
        self.root.ids.home_music.clear_widgets()
        self.root.ids.music_spinner.active = True
        self.root.ids.home_text.text = "Song Is Searching ..."
        threading.Thread(target=self.bhojpuri_s, daemon=True).start()

    def bhojpuri_s(self):
        Clock.schedule_once(lambda dt: self.bhojpuri_so())

    def bhojpuri_so(self):
        try:
            self.search_data = self.bhojpu
            for i in range(len(self.search_data)):
                print(self.search_data[i]["title"])
                
                self.image_url = self.search_data[i]['image'].replace('50x50', '500x500').replace('150x150', '500x500')
                
            
                
                lst = abhay(text=self.search_data[i]['title'].replace("&quot;","'").replace("&amp;", "&").replace("&#039;", "'"),on_press=lambda x,y=i: self.song_detail(y))
                sk = IconLeftWidget(icon="",theme_text_color="Custom",text_color=(1,1,1,1))
                
                sl = FitImage(source=self.image_url, radius=20)
                
                sk.add_widget(sl)
                lst.add_widget(sk)
                
        
            
                self.root.ids.home_music.add_widget(lst)

        except:

            response = requests.get(playlist_details_base_url.format("8c-UE,,iBhN8497ZNqIDKA__")+"&lyrics=true")
            if response.status_code == 200:
                songs_json = response.text.encode().decode()
                songs_json = json.loads(songs_json)
                self.search_data = songs_json['list']
                self.bhojpuri_song = self.search_data
                for i in range(len(self.search_data)):
                    print(self.search_data[i]["title"])
                    
                    self.image_url = self.search_data[i]['image'].replace('50x50', '500x500').replace('150x150', '500x500')
                    
                
                    
                    lst = abhay(text=self.search_data[i]['title'].replace("&quot;","'").replace("&amp;", "&").replace("&#039;", "'"),on_press=lambda x,y=i: self.song_detail(y))
                    sk = IconLeftWidget(icon="",theme_text_color="Custom",text_color=(1,1,1,1))
                    
                    sl = FitImage(source=self.image_url, radius=20)
                    
                    sk.add_widget(sl)
                    lst.add_widget(sk)
                    
            
                
                    self.root.ids.home_music.add_widget(lst)

        self.root.ids.music_spinner.active = False
        self.root.ids.home_text.text = ""

    def romantic(self,*args):
        self.root.ids.home_music.clear_widgets()
        self.root.ids.music_spinner.active = True
        self.root.ids.home_text.text = "Song Is Searching ..."
        threading.Thread(target=self.romantic_s, daemon=True).start()

    def romantic_s(self):
        Clock.schedule_once(lambda dt: self.romantic_so())

    def romantic_so(self):
        response = requests.get(playlist_details_base_url.format("SBKnUgjNeMIwkg5tVhI3fw__")+"&lyrics=true")
        if response.status_code == 200:
            songs_json = response.text.encode().decode()
            songs_json = json.loads(songs_json)
            self.search_data = songs_json['list']

            for i in range(len(self.search_data)):
                print(self.search_data[i]["title"])
                
                self.image_url = self.search_data[i]['image'].replace('50x50', '500x500').replace('150x150', '500x500')
                
            
                
                lst = abhay(text=self.search_data[i]['title'].replace("&quot;","'").replace("&amp;", "&").replace("&#039;", "'"),on_press=lambda x,y=i: self.song_detail(y))
                sk = IconLeftWidget(icon="",theme_text_color="Custom",text_color=(1,1,1,1))
                
                sl = FitImage(source=self.image_url, radius=20)
                
                sk.add_widget(sl)
                lst.add_widget(sk)
                
        
            
                self.root.ids.home_music.add_widget(lst)

        self.root.ids.music_spinner.active = False
        self.root.ids.home_text.text = ""

    def party(self,*args):
        self.root.ids.home_music.clear_widgets()
        self.root.ids.music_spinner.active = True
        self.root.ids.home_text.text = "Song Is Searching ..."
        threading.Thread(target=self.party_s, daemon=True).start()

    def party_s(self):
        Clock.schedule_once(lambda dt: self.party_so())

    def party_so(self):
        response = requests.get(playlist_details_base_url.format("qVvfieICUY5ieSJqt9HmOQ__")+"&lyrics=true")
        if response.status_code == 200:
            songs_json = response.text.encode().decode()
            songs_json = json.loads(songs_json)
            self.search_data = songs_json['list']

            for i in range(len(self.search_data)):
                print(self.search_data[i]["title"])
                
                self.image_url = self.search_data[i]['image'].replace('50x50', '500x500').replace('150x150', '500x500')
                
            
                
                lst = abhay(text=self.search_data[i]['title'].replace("&quot;","'").replace("&amp;", "&").replace("&#039;", "'"),on_press=lambda x,y=i: self.song_detail(y))
                sk = IconLeftWidget(icon="",theme_text_color="Custom",text_color=(1,1,1,1))
                
                sl = FitImage(source=self.image_url, radius=20)
                
                sk.add_widget(sl)
                lst.add_widget(sk)
                
        
            
                self.root.ids.home_music.add_widget(lst)

        self.root.ids.music_spinner.active = False
        self.root.ids.home_text.text = ""

    def old(self,*args):
        self.root.ids.home_music.clear_widgets()
        self.root.ids.music_spinner.active = True
        self.root.ids.home_text.text = "Song Is Searching ..."
        threading.Thread(target=self.old_s, daemon=True).start()

    def old_s(self):
        Clock.schedule_once(lambda dt: self.old_so())

    def old_so(self):
        response = requests.get(playlist_details_base_url.format("qaou266p,04va8qgomsMOw__")+"&lyrics=true")
        if response.status_code == 200:
            songs_json = response.text.encode().decode()
            songs_json = json.loads(songs_json)
            self.search_data = songs_json['list']

            for i in range(len(self.search_data)):
                print(self.search_data[i]["title"])
                
                self.image_url = self.search_data[i]['image'].replace('50x50', '500x500').replace('150x150', '500x500')
                
            
                
                lst = abhay(text=self.search_data[i]['title'].replace("&quot;","'").replace("&amp;", "&").replace("&#039;", "'"),on_press=lambda x,y=i: self.song_detail(y))
                sk = IconLeftWidget(icon="",theme_text_color="Custom",text_color=(1,1,1,1))
                
                sl = FitImage(source=self.image_url, radius=20)
                
                sk.add_widget(sl)
                lst.add_widget(sk)
                
        
            
                self.root.ids.home_music.add_widget(lst)
        self.root.ids.music_spinner.active = False
        self.root.ids.home_text.text = ""
        
    def song_detail(self,i):
        self.change_screen("playscreen")
        
        threading.Thread(target=self.song_det(i), daemon=True).start()
        
        #self.song_details(i)
        
    def song_det(self,i):
        time.sleep(1)
        Clock.schedule_once(lambda dt: self.song_details(i))
        

    def song_details(self,i):
        try:
            self.stop()
        except:
            pass
        self.song_id = self.search_data[i]['id']
        home = self.root.ids.home
        
        self.fetch_thread = threading.Thread(target=self.fetch_details)
        self.fetch_thread.start()
        ak = self.root.ids.playscreen
        self.image_url = self.search_data[i]['image'].replace('50x50', '500x500').replace('150x150', '500x500')
        self.root.ids.song_image_url.source = self.image_url
        self.root.ids.home_song_image_url.source = self.image_url
        self.song_name = self.search_data[i]['title'].replace("&quot;","'").replace("&amp;", "&").replace("&#039;", "'")
        self.root.ids.songname.text = self.song_name
        self.next_button = MDIconButton(icon="skip-next", pos_hint={"center_x": .68, "center_y": .25}, icon_size="48sp", on_release=lambda x: self.song_details(i+1))
        
        next_button = MDIconButton(icon="skip-next", pos_hint={"center_x": .9, "center_y": .5}, icon_size="48sp", on_release=lambda x: self.song_details(i+1))
        
        ak.add_widget(self.next_button)
        home.add_widget(next_button)
        
        self.pre_button = MDIconButton(icon="skip-previous", pos_hint={"center_x": .32, "center_y": .25}, icon_size="45sp", on_release=lambda x: self.song_details(i-1))
        
        pre_button = MDIconButton(icon="skip-previous", pos_hint={"center_x": .7, "center_y": .5}, icon_size="45sp", on_release=lambda x: self.song_details(i-1))
        ak.add_widget(self.pre_button)
        
        home.add_widget(pre_button)
        
        self.root.ids.home.md_bg_color = (50/255,99/255,80/255,1)
        
        self.root.ids.playscreen.add_widget(MDIconButton(icon="rewind-10", pos_hint={"center_x": .14, "center_y": .25}, icon_size="30sp", on_release=lambda x: self.rewind()))
        self.root.ids.playscreen.add_widget(MDIconButton(icon="fast-forward-10", pos_hint={"center_x": .86, "center_y": .25}, icon_size="30sp", on_release=lambda x: self.forward()))
        
        self.root.ids.play.icon = "pause"
        self.root.ids.home_play.icon = "pause"
        self.play_song_online(i)
    
    def play_song_online(self,i):
        self.fetch_thread.join()
        if self.sound:
            
            self.play()
            lnth = self.sound.getDuration()
            Clock.schedule_interval(lambda dt: self.online_play_bar(i),1)
             #   t2 = threading.Thread(target=self.online_play_bar, args=(lnth,))
         #       t2.start()
            
        else:
            time.sleep(0.5)
            self.play_song_online(i)
            
            
    def online_play_bar(self,i):
        lnth = self.sound.getDuration()
        self.root.ids.progress.value = 100*(self.sound.getCurrentPosition())/lnth
        ak = self.convert_sec(self.sound.getCurrentPosition())
        self.root.ids.song_cu.text = ak
        
        if self.root.ids.song_cu.text == self.root.ids.song_du.text:
            self.song_details(i+1)

    def fetch_details(self):

        print('started fetching details')
        data = json.loads(requests.get(song_details_base_url+self.song_id).text.replace("&quot;","'").replace("&amp;", "&").replace("&#039;", "'"))[self.song_id]
        try:
            data['media_url'] = self.decrypt_url(data['encrypted_media_url'])
            if data['320kbps'] != "true":
                data['media_url'] = data['media_url'].replace(
                    "_320.mp4", "_160.mp4")
            data['media_preview_url'] = data['media_url'].replace(
                "_320.mp4", "_96_p.mp4").replace("_160.mp4", "_96_p.mp4").replace("//aac.", "//preview.")
        except KeyError or TypeError:
            url = data['media_preview_url']
            url = url.replace("preview", "aac")
            if data['320kbps'] == "true":
                url = url.replace("_96_p.mp4", "_320.mp4")
            else:
                url = url.replace("_96_p.mp4", "_160.mp4")
            data['media_url'] = url
        print(data['media_url'])

        song_url = data['media_url']
        self.prepare(song_url)
        ak = self.convert_sec(self.sound.getDuration())
        bk = self.convert_sec(self.sound.getCurrentPosition())
        
        self.root.ids.song_du.text = ak
        self.root.ids.song_cu.text = bk
        
        try:
            self.sio.emit("play_music", {"url":song_url,"user":self.username})
            
        except:
            pass
        
        
    def convert_sec(self, lnth):
        lnth = lnth/1000
        try:
            if int(lnth-(60*(lnth//60))) < 10:
                return("{}:0{}".format(int(lnth//60), int(lnth-(60*(lnth//60)))))
            else:
                return("{}:{}".format(int(lnth//60), int(lnth-(60*(lnth//60)))))
        except:
            print('Error: Length is {}'.format(lnth))


    def decrypt_url(self,url):
        des_cipher = des(b"38346591", ECB, b"\0\0\0\0\0\0\0\0",
                        pad=None, padmode=PAD_PKCS5)
        enc_url = base64.b64decode(url.strip())
        dec_url = des_cipher.decrypt(enc_url, padmode=PAD_PKCS5).decode('utf-8')
        dec_url = dec_url.replace("_96.mp4", "_320.mp4")
        return dec_url
        
    

    def move(self, *args):
        if self.root.ids.message_input.focus:
            Clock.schedule_once(lambda dt: setattr(self.root.ids.chat_card, "pos_hint", {"center_x": .5, "center_y": .41}), 0.1)
            
            Clock.schedule_once(lambda dt: setattr(self.root.ids.typing_label, "pos_hint", {"center_x": .5, "center_y": .48}), 0.1)
            
            Clock.schedule_once(lambda dt: setattr(self.root.ids.reply_label, "pos_hint", {"center_x": .75, "center_y": .48}), 0.1)
            
            Clock.schedule_once(lambda dt: (
                setattr(self.root.ids.chat_layout, "pos_hint", {"center_x": .5, "center_y": .7}),
                setattr(self.root.ids.chat_layout, "size_hint_y", 0.35)  # Increase size when typing
            ), 0.1)
                
            
           # Clock.schedule_once(lambda dt: setattr(self.root.ids.chat_layout, "pos_hint", {"center_x": .5, "center_y": .8}), 0.1)
            
        else:
            Clock.schedule_once(lambda dt: setattr(self.root.ids.chat_card, "pos_hint", {"center_x": .5, "center_y": .1}), 0.1)
            
            Clock.schedule_once(lambda dt: setattr(self.root.ids.typing_label, "pos_hint", {"center_x": .5, "center_y": .2}), 0.1)
            
            Clock.schedule_once(lambda dt: setattr(self.root.ids.reply_label, "pos_hint", {"center_x": .75, "center_y": .2}), 0.1)
            
            Clock.schedule_once(lambda dt: (
                setattr(self.root.ids.chat_layout, "pos_hint", {"center_x": .5, "center_y": .55}),
                setattr(self.root.ids.chat_layout, "size_hint_y", 0.6)  # Increase size when typing
            ), 0.1)
            
            
     #       Clock.schedule_once(lambda dt: setattr(self.root.ids.chat_layout, "pos_hint", {"center_x": .5, "center_y": .55}), 0.1)

        
    def set(self):
        self.change_screen("setting")
        
    def check_update(self):
        webbrowser.open_new('https://github.com/bhagatabhay121/chat_ai')
        
    def change_theme(self):
        if self.root.ids.dark_mode_switch.active == True:
            self.theme_cls.theme_style = "Dark"
        else:
            self.theme_cls.theme_style = "Light"
            
    def fetch_msg(self):
        response = requests.get(FIREBASE_URL)
        if response.status_code == 200 and response.text != "null":
            messages = json.loads(response.text)
            print(messages)
            for msg_id, msg_data in messages.items():
                print(msg_data)
                chat_list = self.root.ids.chat_list
                sender = msg_data["sender"]
                message_id = msg_data["message_id"]
                message = msg_data["message"]
                current_time = msg_data["time"]
                reactions = msg_data.get("reactions", {})
                reply_to = msg_data.get("reply_to", None)
                long_text = f"{sender}: {message}"
                ak = break_text(long_text, 75)

                def show_menu(instance):
                    dropdown_menu.open()

            

                def delete_message_action():
                    self.delete_message(message_id)
                    dropdown_menu.dismiss()

                def reply_message_action():
                    self.select_message(message)
                    dropdown_menu.dismiss()

                def copy_message_action():
                    Clipboard.copy(message)
                    toast("Message is copied.")
                    dropdown_menu.dismiss()

                def reaction_message_action():
                    self.show_reaction_menu(message_id)
                    dropdown_menu.dismiss()

                menu_items = [
                    {"text": "Delete", "on_release": delete_message_action},
                    {"text": "Reply", "on_release": reply_message_action},
                    {"text": "Copy", "on_release": copy_message_action},
                    {"text": "Reaction", "on_release": reaction_message_action}
                ]

                if sender == self.username:
                    def edit_message_action():
                        self.show_edit_popup(message_id, message, sender)
                        dropdown_menu.dismiss()
                    menu_items.insert(0, {"text": "Edit", "on_release": edit_message_action})

                

                if sender == self.username:
                
                    bubble = MDCard(
                        size_hint_x=None,  # Let width be dynamically set
                        size_hint_y=None,
                        adaptive_size=True,
                        width=dp(100),
                        height=dp(50),
                        padding=dp(20),
                        pos=(dp(5100), dp(400)),
                        radius=[10, 10, 10, 0], 
                        md_bg_color=(66/255,135/255,245/255,1),
                        id=message_id 
                    )

                    

                    label = MDLabel(
                        text=ak,
                        theme_text_color="Custom",
                        text_color=(1, 1, 1, 1),
                        size_hint_y=None,
                        size_hint_x=None,
                        adaptive_size=True,
                        text_size=(None, None),
                        halign="right",
                        pos_hint={'center_x': 0.02,'center_y': 0.9}
                    )

                    label_time = MDLabel1(
                        text=current_time,
                        theme_text_color="Custom",
                        text_color=(0, 0, 0, 1),
                        size_hint_y=None,
                        adaptive_size=True,
                        pos_hint={'center_x': 0.1,'center_y': 0.0001}
                    )
                    bubble.bind(on_release=show_menu)
                    bubble.add_widget(label)
                    bubble.add_widget(label_time)
                    bubble.width = label.texture_size[0] + dp(30)

                else:
                    bubble = MDCard(
                        size_hint_x=None,  # Let width be dynamically set
                        size_hint_y=None,
                        adaptive_size=True,
                        width=dp(100),
                        height=dp(50),
                        padding=dp(20),
                        pos=(dp(50), dp(400)),
                        radius=[10, 10, 10, 0],  # Rounded edges
                        md_bg_color=(210/255,212/255,217/255,1),
                        id=message_id 
                    )

                

                    label = MDLabel(
                        text=ak,
                        theme_text_color="Custom",
                        text_color=(1, 1, 1, 1),
                        size_hint_y=None,
                        size_hint_x=None,
                        adaptive_size=True,
                        text_size=(None, None),
                        halign="left",
                        pos_hint={'center_x': 0.02,'center_y': 0.9}
                    )

                    label_time = MDLabel1(
                        text=current_time,
                        theme_text_color="Custom",
                        text_color=(0, 0, 0, 1),
                        size_hint_y=None,
                        adaptive_size=True,
                        pos_hint={'center_x': 0.92,'center_y': 0.0001}
                    )     

                    bubble.bind(on_release=show_menu)
                    bubble.add_widget(label)
                    bubble.add_widget(label_time)
                    bubble.width = label.texture_size[0] + dp(30)
                #bubble.width = label.texture_size[0] + ("20dp")

                dropdown_menu = MDDropdownMenu(
                    caller=bubble,
                    items=menu_items,
                    width_mult=3
                )

                if reply_to:
                    reply_bubble = MDCard(
                        size_hint_x=None,
                        size_hint_y=None,
                        adaptive_size=True,
                        padding=[15, 5],
                        radius=[10, 10, 10, 10],
                        md_bg_color=(0.5, 0.5, 0.5, 1)  # Gray for reply
                    )
                    reply_label = MDLabel(
                        text=f"Replying to: {reply_to}",
                        theme_text_color="Custom",
                        text_color=(1, 1, 1, 1),
                        size_hint_y=None,
                        adaptive_size=True,
                    )
                    reply_bubble.add_widget(reply_label)
                    bubble.add_widget(reply_bubble)

                
                chat_list.add_widget(bubble)
                self.root.ids.scrollview.scroll_y = 0

    
    def fetch_message(self, *args):
        
        """Fetch messages from Firebase and update the UI."""
        response = requests.get(FIREBASE_URL)
        if response.status_code == 200 and response.text != "null":
            messages = json.loads(response.text)
            print(messages)
            for msg_id, msg_data in messages.items():
                print(msg_data)
                chat_list = self.root.ids.chat_list
                sender = msg_data["sender"]
                message_id = msg_data["message_id"]
                message = msg_data["message"]
                current_time = msg_data["time"]
                reactions = msg_data.get("reactions", {})
                reply_to = msg_data.get("reply_to", None)
                long_text = f"{sender}: {message}"
                ak = break_text(long_text, 75)

                def show_menu(instance):
                    dropdown_menu.open()

            

                def delete_message_action():
                    self.delete_message(message_id)
                    dropdown_menu.dismiss()

                def reply_message_action():
                    self.select_message(message)
                    dropdown_menu.dismiss()

                def copy_message_action():
                    Clipboard.copy(message)
                    toast("Message is copied.")
                    dropdown_menu.dismiss()

                def reaction_message_action():
                    self.show_reaction_menu(message_id)
                    dropdown_menu.dismiss()

                menu_items = [
                    {"text": "Delete", "on_release": delete_message_action},
                    {"text": "Reply", "on_release": reply_message_action},
                    {"text": "Copy", "on_release": copy_message_action},
                    {"text": "Reaction", "on_release": reaction_message_action}
                ]

                if sender == self.username:
                    def edit_message_action():
                        self.show_edit_popup(message_id, message, sender)
                        dropdown_menu.dismiss()
                    menu_items.insert(0, {"text": "Edit", "on_release": edit_message_action})

                

                if sender == self.username:
                
                    bubble = MDCard(
                        size_hint_x=None,  # Let width be dynamically set
                        size_hint_y=None,
                        adaptive_size=True,
                        width=dp(100),
                        height=dp(50),
                        padding=dp(20),
                        pos=(dp(5100), dp(400)),
                        radius=[10, 10, 10, 0], 
                        md_bg_color=(66/255,135/255,245/255,1),
                        id=message_id 
                    )

                    

                    label = MDLabel(
                        text=ak,
                        theme_text_color="Custom",
                        text_color=(1, 1, 1, 1),
                        size_hint_y=None,
                        size_hint_x=None,
                        adaptive_size=True,
                        text_size=(None, None),
                        halign="right",
                        pos_hint={'center_x': 0.02,'center_y': 0.9}
                    )

                    label_time = MDLabel1(
                        text=current_time,
                        theme_text_color="Custom",
                        text_color=(0, 0, 0, 1),
                        size_hint_y=None,
                        adaptive_size=True,
                        pos_hint={'center_x': 0.1,'center_y': 0.0001}
                    )
                    bubble.bind(on_release=show_menu)
                    bubble.add_widget(label)
                    bubble.add_widget(label_time)
                    bubble.width = label.texture_size[0] + dp(30)

                else:
                    bubble = MDCard(
                        size_hint_x=None,  # Let width be dynamically set
                        size_hint_y=None,
                        adaptive_size=True,
                        width=dp(100),
                        height=dp(50),
                        padding=dp(20),
                        pos=(dp(50), dp(400)),
                        radius=[10, 10, 10, 0],  # Rounded edges
                        md_bg_color=(210/255,212/255,217/255,1),
                        id=message_id 
                    )

                

                    label = MDLabel(
                        text=ak,
                        theme_text_color="Custom",
                        text_color=(1, 1, 1, 1),
                        size_hint_y=None,
                        size_hint_x=None,
                        adaptive_size=True,
                        text_size=(None, None),
                        halign="left",
                        pos_hint={'center_x': 0.02,'center_y': 0.9}
                    )

                    label_time = MDLabel1(
                        text=current_time,
                        theme_text_color="Custom",
                        text_color=(0, 0, 0, 1),
                        size_hint_y=None,
                        adaptive_size=True,
                        pos_hint={'center_x': 0.92,'center_y': 0.0001}
                    )     

                    bubble.bind(on_release=show_menu)
                    bubble.add_widget(label)
                    bubble.add_widget(label_time)
                    bubble.width = label.texture_size[0] + dp(30)
                #bubble.width = label.texture_size[0] + ("20dp")

                dropdown_menu = MDDropdownMenu(
                    caller=bubble,
                    items=menu_items,
                    width_mult=3
                )

                if reply_to:
                    reply_bubble = MDCard(
                        size_hint_x=None,
                        size_hint_y=None,
                        adaptive_size=True,
                        padding=[15, 5],
                        radius=[10, 10, 10, 10],
                        md_bg_color=(0.5, 0.5, 0.5, 1)  # Gray for reply
                    )
                    reply_label = MDLabel(
                        text=f"Replying to: {reply_to}",
                        theme_text_color="Custom",
                        text_color=(1, 1, 1, 1),
                        size_hint_y=None,
                        adaptive_size=True,
                    )
                    reply_bubble.add_widget(reply_label)
                    bubble.add_widget(reply_bubble)

                
                chat_list.add_widget(bubble)
                self.root.ids.scrollview.scroll_y = 0

    def on_start(self):
        Clock.schedule_interval(self.cle,0.1)
        Clock.schedule_interval(self.move,0.1)
        if store.exists("user"):
            self.root.ids.screen_manager.current = "home"
            self.username = store.get("user")["name"]
            
        else:
            self.root.ids.screen_manager.current = "user_detail"
        
        threading.Thread(target=self.ro, daemon=True).start()

    def ro(self):
        Clock.schedule_once(lambda dt: self.fetch_message())
        Clock.schedule_once(lambda dt: self.trend())
        
        
        
    def cle(self,*args):
        if self.root.ids.profile_search.text == "":
            self.root.ids.clo.icon = ""
            
        else:
            self.root.ids.clo.icon = "close"
            
        if self.root.ids.message_input.text == "":
            self.root.ids.close.icon = ""
            
        else:
            self.root.ids.close.icon = "close"
            
        if self.root.ids.song_name.text == "":
            self.root.ids.clos.icon = ""
            
        else:
            self.root.ids.clos.icon = "close"
            
    def clear(self):
        self.root.ids.message_input.text = ""
        self.root.ids.profile_search.text = ""
        self.root.ids.song_name.text = ""
        
    def change(self):
        self.change_screen("chat")
    
    
    def prepare(self, link):
        
         try:
             self.sound = MediaPlayer()
             self.sound.setDataSource(link)
             self.sound.prepare()
             self.sound.setLooping(False)
         except Exception as e:
             print(e)
             time.sleep(0.25)
             self.prepare(link)
         
    def play(self):
        self.sound.start()
        self.play_status = 'play'
        ak = self.root.ids.songname.text
        self.show_notification("Playing", ak)
    def pause(self):
        if self.root.ids.play.icon == "pause":
            self.sound.pause()
            self.root.ids.play.icon = "play"
            self.root.ids.home_play.icon = "play"
            
        else:
            self.play()
            self.root.ids.play.icon = "pause"
            self.root.ids.home_play.icon = "pause"
        self.play_status = 'pause'
        ak = self.root.ids.songname.text
        self.show_notification("Paused", ak)
        
    def c(self):
        self.change_screen("music")
    def stop(self):
        self.sound.stop()
        self.sound.release()
        self.play_status = 'stop'
        
    def forward(self):
       # self.sound.seekTo(50*1000)
        self.sound.seekTo(self.sound.getCurrentPosition() + 10000)
    def rewind(self):
        self.sound.seekTo(self.sound.getCurrentPosition() - 10000)
        
    def slide(self):
        ak = self.sound.getDuration()
        bk = self.root.ids.progress.value
        print(bk*ak/100)
        self.sound.seekTo(bk*ak/100)
        
    def show_notification(self,status, title):
        notification.notify(title=f"Music Player - {status}",message=f"Now {status}: {title}",app_name="Music App",timeout=5)
        
def break_text(text, limit):
    return '\n'.join([text[i:i+limit] for i in range(0, len(text), limit)])


Test().run()
